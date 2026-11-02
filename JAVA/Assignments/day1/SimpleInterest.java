package day1;
import java.util.Scanner;

public class SimpleInterest {
	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		
		System.out.print("Enter Principal Amount: ");
		double pa = s.nextDouble();
		
		System.out.print("Enter Rate of Interest: ");
		double rate = s.nextFloat();
		
		System.out.print("Enter the Time: ");
		int time = s.nextInt();
		
		double si = (pa * rate * time) / 100;
		System.out.println("Simple Interest: "+ si);
		
		double amount = pa + si;
		System.out.println("Total Amount: " + amount);
	}
}
