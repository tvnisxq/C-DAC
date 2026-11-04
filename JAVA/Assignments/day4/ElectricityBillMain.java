package day4;

public class ElectricityBillMain {
	public static void main(String[] args) {
		ElectricityBill c1 = new ElectricityBill();
		c1.read();
		System.out.println("==== ELECTRICITY DETAILS ====");
		c1.display();
		System.out.println("===============================");
		
		ElectricityBill c3 = new ElectricityBill();
		c3.read();
		System.out.println("==== ELECTRICITY DETAILS ====");
		c3.display();
		System.out.println("===============================");
		
		
		ElectricityBill c2 = new ElectricityBill();
		c2.read();
		System.out.println("==== ELECTRICITY DETAILS ====");
		c2.display();
		System.out.println("===============================");
		
	}
}
