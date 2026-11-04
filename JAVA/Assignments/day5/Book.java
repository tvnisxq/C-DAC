package day5;

public class Book {
	
	// Non-static Instance variables
	int bookId;
	String bookTitle;
	String authName;
	float price;
	
	// Static instance variables
	static int bookcount = 0;
	static String storename = "Fakirchand Book Store";
	
	Book(int bookId, String bookTitle, String authName, float price){
		this.bookId = bookId;
		this.bookTitle = bookTitle;
		this.authName = authName;
		this.price = price;
		
		bookcount++;
		
	}
	public void display() {
		System.out.println("Book ID: " + bookId);
		System.out.println("Book Title: " + bookTitle);
		System.out.println("Author Name: " + authName);
		System.out.println("Book Price: " + price);
	}
	
	
}
