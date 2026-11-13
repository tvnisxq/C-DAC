package book_arraylist;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class BookMain {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		ArrayList<Book> books = new ArrayList<>();
		
		int choice;
		
		do {
			System.out.println("\n==== MENU ====");
			System.out.println("1. Add books");
			System.out.println("2. Display Books");
			System.out.println("3. Search Books");
			System.out.println("4. Update Books");
			System.out.println("5. Delete Books");
			System.out.println("6. Total Books");
			System.out.println("7. Exit");
			System.out.println("================");
			
			
			System.out.print("Enter your Choice: ");
			choice = sc.nextInt();

			
			switch(choice) {
			// Add
			case 1:
				System.out.print("Enter Book ID: ");
				int id = sc.nextInt();
				boolean found = false;
				
				for(Book b: books) {
					if (b.bookid == id) {
						found = true;
						break;
					}
				}
				if (found) {
					System.out.println("Book Already exists!");
					break;
				}
				
				sc.nextLine();
				
				System.out.print("Enter Book title: ");
				String title = sc.nextLine();
				
				
				System.out.print("Enter author Name: ");
				String author = sc.nextLine();
				
				System.out.print("Enter the Price: ");
				double price = sc.nextDouble();
				
				books.add(new Book(id, title, author, price));
				System.out.println("Book added successfully!");
				break;
				
			// Display
			case 2:
				if (books.isEmpty()) {
					System.out.println("NO books available!");
				}else {
					System.out.println("\n==== BOOKD DETAILS ====");
					
					for(Book b: books) {
						b.display();
					}
				}
				break;
				
			// Search
			case 3:
				System.out.print("Enter Book ID to search");
				id = sc.nextInt();
				found = false;
				
				for (Book b: books) {
					if (b.bookid == id) {
						b.display();
					}
				}
				break;	
				
						
				
			// Update
			case 4:
				System.out.println("Enter Book id to be updated: ");
				id = sc.nextInt();
				found = false;
				
				for (Book b: books) {
					if (b.bookid == id) {
						System.out.print("Enter new Price: ");
						b.price = sc.nextDouble();
						
						System.out.println("Price Updated Successfully!");
						found = true;
						break;
						
					}
				}
				if (!found) {
					System.out.println("Book not found!");
				}
				break;
				
			// Delete
			case 5:
				System.out.print("Enter Book id to be deleted: ");
				id = sc.nextInt();
				found = false;
				
				for(Book b: books) {
					if (b.bookid == id) {
						books.remove(b);
						
						System.out.println("Book deleted successfully!");
						found = true;
						break;
					}
				}
				if (!found) {
					System.out.println("Book doesn't exists!");
				}
				break;
				
				
			// Total books
			case 6:
				System.out.println("Total Books: " + books.size());
				break;
				
			// Exit
			case 7:
				System.out.println("Thankyou! Exiting Program!");
				break;
				
			default:
				System.out.println("Invalid Choice! Please try again");
				
			} // switch closed here
			
			
		} // do closed here
		while (choice != 7);
		sc.close(); // close the scanner
	}
}
