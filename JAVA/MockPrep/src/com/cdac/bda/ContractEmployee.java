package com.cdac.bda;

public class ContractEmployee extends Employee{
	// Instance Variables
	float allowance;
	
	ContractEmployee(int empId, String empName, float empBaseSal, float allowance){
		super(empId, empName, empBaseSal);
		this.allowance = allowance;
	}
	
	public float calculateSalary() {
		return empBaseSal + allowance;
	}
	
	public void display() {
		super.display();
		System.out.println("Allowance: " + allowance);
	}
}