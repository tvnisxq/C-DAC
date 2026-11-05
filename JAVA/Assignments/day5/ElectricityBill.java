package day5;

public class ElectricityBill {
	int consNum;
	String consName;
	int unitCons;
	int costPerUnit;
	
	static int consCount = 0;
	static String electricityBoard = "CSPDCL";
	
	public ElectricityBill(int consNum, String consName, int unitCons, int costPerUnit) {
		this.consNum = consNum;
		this.consName = consName;
		this.unitCons = unitCons;
		this.costPerUnit = costPerUnit;
		
		consCount++;
	}
	
	public float calculateBill() {
		return unitCons * costPerUnit;
	}
	
	public void display() {
		System.out.println("Consumer Number:" + consNum);
		System.out.println("Consumer Name: " + consName);
		System.out.println("Units Consumed: " + unitCons);
		System.out.println("Total Bill: " + calculateBill());
	}
	
	
}
