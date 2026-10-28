package com.cdac.bda;

public class PaymentMain {
	public static void main(String[] args) {
		
		Payment p1 = new CreditCardPayment(1, 1000, "9800AEF23456", 300);
		
		Payment p2 = new UPIPayment(2, 3000, "9300REGH1234", "Asha", "Ravi");
		
		
		Payment[] payments = {p1, p2};
		
		for (Payment p: payments) {
			System.out.println("Transaction Details: " );
			p.processPayment();
			System.out.println("-----------------------");
			
		}
	}
}
