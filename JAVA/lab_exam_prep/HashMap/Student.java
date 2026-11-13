package student_hash_map;

public class Student {
	int studentId;
	String studentName;
	String course;
	double marks;
	
	// Parameterized Constructor
	Student(int studentId, String studentName, String course, double marks){
		this.studentId = studentId;
		this.studentName = studentName;
		this.course = course;
		this.marks = marks;
	}
	
	void display() {
		System.out.println("Student ID: " + studentId);
		System.out.println("Student Name: " + studentName);
		System.out.println("Course Enrolled: " + course);
		System.out.println("Marks Acquired: " + marks);
		System.out.println("-----------------------------");
	}
	
}
