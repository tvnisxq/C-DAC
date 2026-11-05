package day5;

public class ElectricityBillMain {
	public static void main(String[] args) {
		ElectricityBill b1 = new ElectricityBill(101, "Aditya", 10, 10);
		ElectricityBill b2 = new ElectricityBill(102, "Dushyant", 18, 10);
		ElectricityBill b3 = new ElectricityBill(103, "Robin", 13, 10);
		
		ElectricityBill[] bill = {b1, b2, b3};
		
		
		System.out.println("==== ELECTRICITY BILL DETAILS ====");
		for (ElectricityBill b: bill) {
			b.display();
			System.out.println("--------------------------");
		}
		
		System.out.println("Total Number of Consumers: " + ElectricityBill.consCount);
		System.out.println("Electricity Board Name: " + ElectricityBill.electricityBoard);
		
		
	}
}
