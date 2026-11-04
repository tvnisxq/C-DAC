package day4;

public class BankAccountMain {
	public static void main(String[] args) {
		BankAccount acc1 = new BankAccount();
		acc1.read();
		System.out.println("==== BANK ACCOUNT DETAILS ====");
		acc1.display();
		System.out.println("==============================");
		
		BankAccount acc2 = new BankAccount();
		acc2.read();
		System.out.println("==== BANK ACCOUNT DETAILS ====");
		acc2.display();
		System.out.println("==============================");
		
		
		BankAccount acc3 = new BankAccount();
		acc3.read();
		System.out.println("==== BANK ACCOUNT DETAILS ====");
		acc3.display();
		System.out.println("==============================");
		
		
	} 
}
