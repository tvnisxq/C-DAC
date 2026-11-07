package day5;

public class ProductMain {
	public static void main(String[] args) {
		Product p1 = new Product(101, "Asus TUF Laptop", 1_50_000, 2);
		Product p2 = new Product(102, "Acer Predator Laptop", 1_60_000, 5);
		Product p3 = new Product(103, "Dell Alienware", 4_00_000, 1);
		
		Product[] products = {p1, p2, p3};
		
		// Displaying all products
		System.out.println("==== PRODUCT INVENTORY ====");
		for (Product p: products) {
			p.display();
			System.out.println("===========================");
		}
				
		// Calculating the total inventory value
		float totalInvValue = 0;
		for (Product p: products) {
			totalInvValue += p.stockValue();
		}
		
		// Finding the product with the highest stock value
		int highestProductId = p1.productId;
		String highestProductName = p1.productName;
		float highestStockValue = p1.stockValue();
		
		for (Product p: products) {
			if (p.stockValue() > highestStockValue) {
				highestStockValue = p.stockValue();
				highestProductId = p.productId;
				highestProductName = p.productName;
				
			}
		}
		System.out.println("==== PRODUCT WITH HIGHEST STOCK VALUE ====");
		System.out.println("Product ID: " + highestProductId);
		System.out.println("Product Name: " + highestProductName);
		System.out.println("Product Stock Value: " + highestStockValue);
		
		System.out.println("===========================================");
		
		
		System.out.println("==== TOTAL INVETORY VALUE ====");
		System.out.println("Total: " + totalInvValue);
		
		System.out.println("===========================================");
		
		System.out.println("Store Name: " + Product.storeName);
		System.out.println("Total Products Created: " + Product.productCount);
		
	}
}
