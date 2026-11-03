package day1;
import java.util.Scanner;
public class PassOrFail {
	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		System.out.print("Enter Student's Marks: ");
		float marks = s.nextFloat();
		
		String result = passorfail(marks);
		System.out.println(result);
	}
	
	public static String passorfail(float marks) {
		if (marks < 40) {
			return "Student has failed the Exam";
		}
		else
			return "Student has passed the Exam";
	}
}
