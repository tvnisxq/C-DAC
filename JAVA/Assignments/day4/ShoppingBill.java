package day4;

import java.util.Scanner;

public class ShoppingBill {
	int orderId;
	String customerName;
	float amount;
	
	Scanner s = new Scanner(System.in);
	
	public void read() {
		System.out.print("Enter Order ID: ");
		orderId = s.nextInt();
		
		System.out.print("Enter Customer Name: ");
		customerName = s.next();
		
		System.out.print("Enter the Purchase Amount: ");
		amount = s.nextFloat();
		
		}
	
	public float calculateDiscount() {
		float discount;
		if (amount >= 10000) {
			discount  = (float) 15/100 * amount;
		}
		else if (amount >= 5000) {
			discount = (float) 10/100 * amount;
		}
		else
			discount = (float) 5/100 * amount;
		
		return discount;
		
	}
	
	
	public void display() {
		System.out.println("Order Id: " + orderId);
		System.out.println("Customer Name: " + customerName);
		System.out.println("Discount Amount: " + calculateDiscount());
		System.out.println("Total Payable Amount: "  + (amount - calculateDiscount() ));
	}
	
}
