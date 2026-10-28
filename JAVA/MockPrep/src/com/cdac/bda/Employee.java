package com.cdac.bda;

public class Employee {
	
	// Instance Variables
	int empId;
	String empName;
	float empBaseSal;
	
	Employee(int empId, String empName, float empBaseSal){
		this.empId = empId;
		this.empName = empName;
		this.empBaseSal = empBaseSal;
	}
	
	public float calculateSalary() {
		return empBaseSal;
	}
	
	public void display() {
		System.out.println("Employee ID: " + empId);
		System.out.println("Employee Name: " + empName);
		System.out.println("Employee Base Salary: " + empBaseSal);
	}
	
}
