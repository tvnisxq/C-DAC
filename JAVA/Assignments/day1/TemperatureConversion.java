package day1;
import java.util.Scanner;

public class TemperatureConversion {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		
		System.out.print("Enter Temperature in Celsius: ");
		float temp_cel = s.nextFloat();
		
		float fahrenheit = (temp_cel * 9/5) + 32;
		System.out.print("Temperature in Fahrenheit: " + fahrenheit);
		
	}
}
