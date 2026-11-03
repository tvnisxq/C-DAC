package day1;

import java.util.Scanner;

public class Voting {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Enter the age: ");
		int age = sc.nextInt();
		
		String result = voting(age);
		System.out.println(result);
		
		sc.close();
	}
	
	public static String voting(int age) {
		if (age < 18) {
			return "You are not eligible for voting!";
		}
		
		else
			return "You are eligible for voting!";
	}
	
	
	
}
