package day4;

import java.util.Scanner;

public class Employee {
	int empId;
	String empName;
	float basicSal;
	
	Scanner s = new Scanner(System.in);
	
	public void read() {
		System.out.print("Enter Employee ID: ");
		empId = s.nextInt();
		
		System.out.print("Enter Employee Name: ");
		empName = s.next();
		
		System.out.print("Enter Basic Salary: ");
		basicSal = s.nextFloat();
	}
	
	public void display() {
		System.out.println("Employee ID: " + empId);
		System.out.println("Employee Name: " + empName);
		System.out.println("Total Salary: " + calculateSalary());
	}
	
	public float calculateSalary() {
		float hra = (float) 20/100 * basicSal;
		float da = (float) 10/100 * basicSal;
		
		float totalSal = basicSal + hra + da;
		return totalSal;
	}
}
