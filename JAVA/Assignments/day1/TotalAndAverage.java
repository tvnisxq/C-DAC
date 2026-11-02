package day1;

public class TotalAndAverage {
	public static void main(String[] args) {
		int m1 = 50;
		int m2 = 57;
		int m3 = 60;
		
		System.out.println("Total Marks: " + total(50, 57, 60));
		System.out.println("Average Marks: " + average(m1, m2, m3));
		
	}
	
	public static int total(int m1, int m2, int m3) {
		int total = m1 + m2 + m3;
		return total;
	}
	
	public static float average(int m1, int m2, int m3) {
		float avg = (m1 + m2 + m3) / 3;
		return avg;
	}
		
}
