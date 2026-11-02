package day1;
import java.util.Scanner;

public class PosNegZero {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		System.out.print("Enter a number: ");
		int digit = s.nextInt();
		
		String result = posnegzero(digit);
		
		System.out.println(result);
		
		s.close();
		
	}
	
	public static String posnegzero(int digit) {
		if (digit > 0) {
			return digit + " is Positive!";
		}
		
		else if (digit < 0) {
			return digit + " is Negative!";
		}
		
		else
			return digit + " is Zero!";
		
		
	}
}
