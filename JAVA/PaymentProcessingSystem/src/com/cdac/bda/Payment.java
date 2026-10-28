package com.cdac.bda;

public class Payment {
	// Instance variables
	int paymentId;
	float paymentAmt;
	
	Payment(int paymentId, float paymentAmt){
		this.paymentId = paymentId;
		this.paymentAmt = paymentAmt;
	}
	
	public void processPayment() {
		System.out.println("Payment ID: " + paymentId);
		System.out.println("Payment Amount: " + paymentAmt);
	}
}
