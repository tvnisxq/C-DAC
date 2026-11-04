package day4;

import java.util.Scanner;

public class BankAccount {
	int bankAcc;
	String accName;
	float accBal;
	
	Scanner s = new Scanner(System.in);
	
	public void read() {
		System.out.print("Enter the Account Number: ");
		bankAcc = s.nextInt();
		
		System.out.print("Enter the Account Holder Name: ");
		accName = s.next();
		
		System.out.print("Enter the Account Balance: ");
		accBal = s.nextFloat();
	}
	
	public void display() {
		System.out.println("Account Number: " + bankAcc);
		System.out.println("Account Holder Name: " + accName);
		System.out.println("Account Balance: " + checkCategory());
	}

	public String checkCategory() {
		if (accBal >= 1_00_000) {
			return "Premium";
		}
		else if (accBal >= 25000) {
			return "Standard";
		}
		
		else
			return "Basic";
		
	}
}
