package com.cdac.bda;

public class PermanentEmployee extends Employee{
	// Instance Variables
	float hra;
	float da;
	
	PermanentEmployee(int empId, String empName, float empBaseSal, float hra, float da){
		super(empId, empName, empBaseSal);
		this.hra = hra;
		this.da = da;
	}
	
	public float calculateSalary() {
		return empBaseSal + hra + da;
	}
	
	public void display() {
		super.display();
		System.out.println("HRA: " + hra);
		System.out.println("DA: " + da);
	}
}
