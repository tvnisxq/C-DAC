package com.cdac.day1;
import java.util.Scanner;

public class Area {
	public static void main(String[] args) {
				
		// Creating Scanner Class ref
		Scanner s = new Scanner(System.in);
		
		// Taking input radius from the console
		System.out.print("Enter the radius: ");
		
		float radius = s.nextFloat();
		
		float area = (float) (Math.PI * radius * radius);
		float cir = (float) (2 * Math.PI * radius);
		
		System.out.printf("Area = %.2f\n", area);
		System.out.printf("Circumference = %.2f", cir);
		
	}	
	
}
