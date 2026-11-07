package day5;

public class Product {
	int productId;
	String productName;
	float unitPrice;
	int quantity;
	static int productCount=0;
	static String storeName = "Walmart";
		
	public Product(int productId, String productName, float unitPrice, int quantity) {
		this.productId = productId;
		this.productName = productName;
		this.unitPrice = unitPrice;
		this.quantity = quantity;
		
		productCount++;
	}
	
	public float stockValue() {
		float stockvalue = unitPrice * quantity;
		return stockvalue;
	}
	
	public void display() {
		System.out.println("Product ID: " + productId);
		System.out.println("Product Name: " + productName);
		System.out.println("Product Unit Price: " + unitPrice);
		System.out.println("Stock Value of Product: " + stockValue());
	}
}