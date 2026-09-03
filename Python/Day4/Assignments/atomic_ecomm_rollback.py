import os
import copy

class AccountNotFoundError(Exception):
    """Raised when an account ID is missing from the registry."""
    pass


class OverdraftError(Exception):
    """Raised when a withdrawal amount exceeds the account balance."""
    pass


class InvalidTransactionError(Exception):
    """Raised when the transaction type is unrecognized or if transaction amounts are non-positive."""
    pass


def process_transaction_batch(accounts: dict, batch_list: list, log_path: str) -> dict:
    """
    Processes a batch of transactions atomically. If any error occurs, 
    reverts all account modifications, logs the failure, and re-raises the exception.
    """
    backup_accounts = copy.deepcopy(accounts)
    
    try:
        for tx in batch_list:
            acc = tx.get("acc")
            tx_type = tx.get("type")
            amt = tx.get("amt")
            
            if acc not in accounts:
                raise AccountNotFoundError(f"Account '{acc}' not found.")
            
            if tx_type not in ("deposit", "withdraw"):
                raise InvalidTransactionError(f"Invalid transaction type '{tx_type}'.")
            
            if amt is None or amt <= 0:
                raise InvalidTransactionError("Transaction amount must be positive.")
            
            if tx_type == "withdraw":
                if accounts[acc] < amt:
                    raise OverdraftError(
                        f"Insufficient funds. Account {acc} has balance {accounts[acc]}, requested {amt}."
                    )
                accounts[acc] -= amt
            elif tx_type == "deposit":
                accounts[acc] += amt
        
        with open(log_path, "a") as log_file:
            log_file.write(f"[SUCCESS] Batch completed. {len(batch_list)} transaction(s) processed.\n")
            
        return accounts

    except (AccountNotFoundError, OverdraftError, InvalidTransactionError) as e:
        accounts.clear()
        accounts.update(backup_accounts)
        
        with open(log_path, "a") as log_file:
            log_file.write(f"[ROLLBACK] Batch aborted: {type(e).__name__} - {e}\n")
            
        raise


# --- Test Execution Script ---
if __name__ == "__main__":
    # Clean up old log file if it exists from previous runs
    log_file = "transactions.log"
    if os.path.exists(log_file):
        os.remove(log_file)

    accounts = {"ACC01": 100.0, "ACC02": 50.0}

    # Batch 1: Valid transactions
    batch_1 = [
        {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
        {"acc": "ACC02", "type": "deposit", "amt": 20.0}
    ]
    accounts = process_transaction_batch(accounts, batch_1, log_file)

    # Batch 2: Invalid transaction (triggers rollback due to overdraft on ACC02)
    batch_2 = [
        {"acc": "ACC01", "type": "deposit", "amt": 50.0},
        {"acc": "ACC02", "type": "withdraw", "amt": 200.0} 
    ]
    
    try:
        accounts = process_transaction_batch(accounts, batch_2, log_file)
    except OverdraftError as e:
        print(f"Caught: {e}")

    # Verify Rollback: ACC01 remains 70.0, and was NOT updated to 120.0 during batch_2 partial execution
    print("Final Accounts State:", accounts) 
    
    # Print log file contents to verify logs
    print("\n--- Contents of transactions.log ---")
    with open(log_file, "r") as f:
        print(f.read(), end="")