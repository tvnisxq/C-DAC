package day5;

public class BankAccountMain {
	public static void main(String[] args) {
		
		BankAccount b1 = new BankAccount(101, "Raju", 5000);
		BankAccount b2 = new BankAccount(102, "Bheem", 10_000);
		BankAccount b3 = new BankAccount(103, "Kalia", 15_000);
		BankAccount[] accounts = {b1, b2, b3};
		
		
		// Finding Account Highest Balance 
		float highestBal = b1.accBal;
		int accNumHighest = b1.accNum;
		String accNameHighest = b1.accName;
		
		// Displaying Details of the Bank Accounts
		System.out.println("==== BANK ACCOUNT DETAILS ====");
		for (BankAccount b : accounts) {
			b.display();
			System.out.println("=================================================");
		}

		
		for (BankAccount b: accounts) {
			if (b.accBal > highestBal) {
				accNumHighest = b.accNum;
				accNameHighest = b.accName;
				highestBal = b.accBal;
			}
		}
		
		float combinedBal = 0;
		for (BankAccount b: accounts) {
			combinedBal += b.accBal;
		}
		System.out.println("==== Highest Balance Account ====");
		System.out.println("Account Number: " + accNumHighest);
		System.out.println("Account Holder Name: " + accNameHighest);
		System.out.println("Account Balance: " + highestBal);
		
		
		System.out.println("=================================================");
		
		System.out.println("==== COMBINED ACCOUNT BALANCE ====");
		System.out.println("Bank Name: " + BankAccount.bankName);
		System.out.println("Total Number of Accounts: " + BankAccount.accCount);
		System.out.println("Combined Balance of All Accounts: " + combinedBal);
	
	
	}
	
	
	
}
