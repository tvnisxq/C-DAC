package day5;

public class BookMain {
	public static void main(String[] args) {
		Book b1 = new Book(201, "The Alchemist", "Paulo Coelho", 350);
		Book b2 = new Book(202, "Atomic Habits", "James Clear", 550);
		Book b3 = new Book(203, "Rich Dad Poor Dad", "Robert Kiyosaki", 450); 
		
		Book[] books = {b1, b2, b3};
		
		// Iterate over book objects and call display function using each book object reference
		for (Book b: books) {
			b.display();
			
		}
		
		float max_price = b1.price;
		String book_name = b1.bookTitle;
		
		for (Book b: books) {
			if (b.price > max_price) {
				max_price = b.price;
				book_name = b.bookTitle;
			
			}
		}
		System.out.println("Book With the Highest Price: " + book_name);
		
		
		System.out.println("Bookstore Name: " + Book.storename);
		System.out.println("Book Count: " + Book.bookcount);
				
	}
}
