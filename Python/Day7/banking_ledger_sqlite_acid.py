from datetime import datetime
import sqlite3


class TransactionError(Exception):
  """Custom exception raised when a banking transaction fails validation or execution."""
  pass


class BankingLedger:

  def __init__(self, db_path):
    self.db_path = db_path
    self._create_tables()

  def _create_tables(self):

    with sqlite3.connect(self.db_path) as conn:
      cursor = conn.cursor()
      cursor.execute("""
                CREATE TABLE IF NOT EXISTS accounts (
                    account_id TEXT PRIMARY KEY,
                    holder_name TEXT,
                    balance REAL
                )
            """)
      cursor.execute("""
                CREATE TABLE IF NOT EXISTS audit_log (
                    tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    from_acc TEXT,
                    to_acc TEXT,
                    amount REAL,
                    timestamp TEXT
                )
            """)
      conn.commit()

  def create_account(self, account_id, holder_name, initial_deposit):

    if initial_deposit < 0:
      raise ValueError("Initial deposit cannot be negative.")

    with sqlite3.connect(self.db_path) as conn:
      cursor = conn.cursor()
      cursor.execute(
          "INSERT INTO accounts (account_id, holder_name, balance) VALUES (?,"
          " ?, ?)",
          (account_id, holder_name, initial_deposit),
      )
      conn.commit()

  def get_balance(self, account_id):
    with sqlite3.connect(self.db_path) as conn:
      cursor = conn.cursor()
      cursor.execute(
          "SELECT balance FROM accounts WHERE account_id = ?", (account_id,)
      )
      row = cursor.fetchone()
      return row[0] if row else None


  def transfer_funds(self, from_acc, to_acc, amount):
    if amount <= 0:
      raise TransactionError("Transfer amount must be strictly positive.")

    conn = sqlite3.connect(self.db_path)
    cursor = conn.cursor()


    try:
      cursor.execute(
          "SELECT balance FROM accounts WHERE account_id = ?", (from_acc,)
      )
      from_row = cursor.fetchone()
      if not from_row:
        raise TransactionError(f"Source account {from_acc} not found.")

      from_balance = from_row[0]
      if from_balance < amount:
        raise TransactionError(f"Insufficient funds in account {from_acc}")

      cursor.execute(
          "SELECT balance FROM accounts WHERE account_id = ?", (to_acc,)
      )
      to_row = cursor.fetchone()
      if not to_row:
        raise TransactionError(f"Destination account {to_acc} not found.")

      cursor.execute(
          "UPDATE accounts SET balance = balance - ? WHERE account_id = ?",
          (amount, from_acc),
      )
      cursor.execute(
          "UPDATE accounts SET balance = balance + ? WHERE account_id = ?",
          (amount, to_acc),
      )

      timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      cursor.execute(
          """
                INSERT INTO audit_log (from_acc, to_acc, amount, timestamp) 
                VALUES (?, ?, ?, ?)
            """,
          (from_acc, to_acc, amount, timestamp),
      )

      conn.commit()


    except (TransactionError, Exception) as e:
      conn.rollback()
      if isinstance(e, TransactionError):
        raise e
      else:
        raise TransactionError(f"An unexpected database error occurred: {e}")
    finally:
      conn.close()