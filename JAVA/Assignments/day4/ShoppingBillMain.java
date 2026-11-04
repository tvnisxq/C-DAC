package day4;

public class ShoppingBillMain {
	public static void main(String[] args) {
		ShoppingBill s1 = new ShoppingBill();
		s1.read();
		System.out.println("==== ONLINE SHOPPING DETAILS ====");
		s1.display();
		System.out.println("=================================");
		
		ShoppingBill s2 = new ShoppingBill();
		s2.read();
		System.out.println("==== ONLINE SHOPPING DETAILS ====");
		s2.display();
		System.out.println("=================================");
		
		
		ShoppingBill s3 = new ShoppingBill();
		s3.read();
		System.out.println("==== ONLINE SHOPPING DETAILS ====");
		s3.display();
		System.out.println("=================================");
		
	}
}
