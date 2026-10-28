package com.cdac.bda;

public class EmployeeMain {
	public static void main(String[] args) {
		// Overriding Employee to include HRA and DA
		Employee e1 = new PermanentEmployee(101, "Asha", 30_000, 6000, 3000);
		
		// Overriding Employee to include Allowance
		Employee e2 = new ContractEmployee(102, "Ravi", 25_000, 5000);
		
		Employee[] emps = {e1 ,e2};
		
		for (Employee e: emps) {
			e.display();
			
			System.out.println("Total Salary: " + e.calculateSalary());
			System.out.println("-------------------------------------");
		}
		
		
		
		
		
	}
}
