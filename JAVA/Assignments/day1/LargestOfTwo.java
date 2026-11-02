package day1;

import java.util.Scanner;

public class LargestOfTwo {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		System.out.print("Enter the 1st Number: ");
		int n1 = s.nextInt();
		
		System.out.print("Enter the 2nd Number: ");
		int n2 = s.nextInt();
		
		String result = largest(n1, n2);
		
		System.out.println(result);
		
	}
	
	public static String largest(int n1, int n2) {
		if (n1 > n2) {
			return n1 + " is Larger than " + n2;
		}
		
		else
			return n2 + " is Larger than " + n1; 
	}
}
