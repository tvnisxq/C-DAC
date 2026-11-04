package day4;

import java.util.Scanner;

public class ElectricityBill {
	int consNumber;
	String consName;
	int unitCons;
	
	Scanner s = new Scanner(System.in);
	
	
	public void read() {
		System.out.print("Enter the Consumer Number: ");
		consNumber = s.nextInt();
		
		System.out.print("Enter the Consumer Name: ");
		consName = s.next();
		
		System.out.print("Enter the Units Consumed: ");
		unitCons = s.nextInt();
	}
	
	public void display() {
		System.out.println("Consumer Number: " + consNumber);
		System.out.println("Consumer Name: " + consName);
		System.out.println("Total Bill: " + calculateBill());
	}

	public float calculateBill() {
		float totalBill;
		if (unitCons <= 100) {
			totalBill = unitCons * 3;
		}
		
		else if (unitCons <= 200) {
			totalBill = (100 * 3) + (unitCons -100) * 5;
		}
		
		else {
			totalBill = (100 * 3) + (100 * 5) + (unitCons - 200) * 8; 
		}
		
		
		return totalBill;
	}
	
}
