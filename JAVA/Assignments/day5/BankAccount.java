package day5;

public class BankAccount {
	int accNum;
	String accName;
	float accBal;
	
	static int accCount = 0;
	static String bankName = "HDFC";
	
	public BankAccount(int accNum, String accName, float accBal) {
		this.accNum = accNum;
		this.accName = accName;
		this.accBal = accBal;
		
		accCount++;
	}
	
	public void display() {
		System.out.println("Account Number: " + accNum);
		System.out.println("Account Name: " + accName);
		System.out.println("Account Balance: " + accBal);
	}
	
	
}
