package day4;

public class StudentMain {
	public static void main(String[] args) {
		Student s1 = new Student();
		s1.read();
		System.out.println("==== STUDENT DETAILS ====");
		s1.display();
		
		Student s2 = new Student();
		s2.read();
		System.out.println("==== STUDENT DETAILS ====");
		s2.display();
		
		Student s3 = new Student();
		s3.read();
		System.out.println("==== STUDENT DETAILS ====");
		s3.display();
	}
}
