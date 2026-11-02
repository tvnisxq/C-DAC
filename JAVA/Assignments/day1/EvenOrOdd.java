package day1;

import java.util.Scanner;

public class EvenOrOdd {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		System.out.print("Enter a digit: ");
		int digit = s.nextInt();
		
		String result = evenorodd(digit);
		System.out.println(result);
		
		s.close();
			
	}
	
	public static String evenorodd(int digit) {
		if (digit % 2 == 0) {
			return digit + " is an Even Number!";
		}
		else 
			return digit + " is an Odd Number!";
	}
}
