package com.cdac.bda;

public class UPIPayment extends Payment{
	// Instance Variables
	String transactionRef;
	String sender;
	String recipient;
	
	
	UPIPayment(int paymentId, float paymentAmt, String transactionRef, String sender, String recipient){
		super(paymentId, paymentAmt);
		this.transactionRef = transactionRef;
		this.sender = sender;
		this.recipient = recipient;
	}
	
	public void processPayment() {
		System.out.println("Payment Amount: " + paymentAmt);
		System.out.println("UPI Transaction Reference: " + transactionRef);
		System.out.println("Sender: " + sender);
		System.out.println("Recipient: " + recipient);
	}
	
}
