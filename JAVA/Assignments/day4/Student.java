package day4;
import java.util.Scanner;

public class Student {
	
	int id;
	String name;
	int marks;
	
	Scanner s = new Scanner(System.in);
		
	public void read() {
		
		System.out.print("Enter student's ID: ");
		id = s.nextInt();
		
		System.out.print("Enter Student's name: ");
		name = s.next();
		
		System.out.print("Enter Student's marks: ");
		marks = s.nextInt();
	}
	
	public void display() {
		System.out.println("ID: " + id);
		System.out.println("Name: " + name);
		System.out.println("Marks: " + marks);
		System.out.println("Result: " + findResult());
		System.out.println("=========================");
	}
	
	public String findResult() {
		if (marks >= 50) {
			return "Pass!";
		}
		else
			return "Fail!";
	}
	
}
