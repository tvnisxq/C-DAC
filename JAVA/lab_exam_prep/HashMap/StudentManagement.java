package student_hash_map;

import java.util.HashMap;
import java.util.Map;

public class StudentManagement {
	HashMap<Integer, Student> students = new HashMap<>();
	
	// Add Student
	void addStudent(Student s) {
		students.put(s.studentId, s);
		System.out.println("Student Added Successfully!");
						
	}
	
	// Display all students
	void displayStudents() {
		if (students.isEmpty()) {
			System.out.println("No student records found!");
			return;
		}
		
		for (Map.Entry<Integer, Student> entry: students.entrySet()) {
			entry.getValue().display();
		}
	}
	
	// Search Students
	void searchStudent(int id) {
		if (students.containsKey(id)) {
			students.get(id).display();
		}
		else {
			System.out.println("Student Id not found!");
		}
	}
	
	// Update Students marks
	void updateMarks(int id, double marks) {
		
		if (students.containsKey(id)) {
			students.get(id).marks = marks;
			System.out.println("Marks Updated Successfully!");
		}
		else {
			System.out.println("Student ID not found!");
		}
	}
	
	
	// Delete Student records
	void deleteStudent(int id) {
		if (students.containsKey(id)) {
			students.remove(id);
			System.out.println("Student ID deleted Successfully!");
		}
		else {
			System.out.println("Student ID does not exist!");
		}
	}
	
	
	// Check Student id
	void checkStudent(int id) {
		if (students.containsKey(id)) {
			System.out.println("Student ID Exists!");		
		}
		else {
			System.out.println("Student ID does not exists!");
		}
	}
	
	// Count Total Students
	void totalStudents() {
		System.out.println("Total Students: " + students.size());
	}
	
}
