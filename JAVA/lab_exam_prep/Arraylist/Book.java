package book_arraylist;

public class Book {
	// instance vars
	int bookid;
	String title;
	String author;
	double price;
	
	
	// param const
	Book(int bookid, String title, String author, double price){
		this.bookid = bookid;
		this.title = title;
		this.author = author;
		this.price = price;
	}
	
	// Method to display books
	void display() {
		System.out.println("Book ID: " + bookid);
		System.out.println("Book Title: " + title);
		System.out.println("Book Author: " + author);
		System.out.println("Book Price: " + price);
	}
}
