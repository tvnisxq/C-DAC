package com.cdac.bda;

public class CreditCardPayment extends Payment{
	// Instance Variables
	String transactionRef;
	float processingFee;
	
	CreditCardPayment(int paymentId, float paymentAmt, String transactionRef, float processingFee){
		super(paymentId, paymentAmt);
		
		this.transactionRef = transactionRef;
		this.processingFee = processingFee;
	}
	
	public void processPayment() {
		System.out.println("Payment Amount: " + paymentAmt);
		System.out.println("Card Transaction Reference: " + transactionRef);
		System.out.println("Processing Fee: " + processingFee);
	}
}
