package student_hash_map;

import java.util.Scanner;

public class StudentMain {
	
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        StudentManagement sm = new StudentManagement();

        int choice;

        do {

            System.out.println("\n===== STUDENT MANAGEMENT SYSTEM =====");
            System.out.println("1. Add Student");
            System.out.println("2. Display All Students");
            System.out.println("3. Search Student");
            System.out.println("4. Update Student Marks");
            System.out.println("5. Delete Student");
            System.out.println("6. Check Student ID");
            System.out.println("7. Display Total Students");
            System.out.println("8. Exit");
            System.out.println("=======================================");
            

            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {

                case 1:
                    System.out.print("Enter Student ID: ");
                    int id = sc.nextInt();

                    sc.nextLine();

                    System.out.print("Enter Student Name: ");
                    String name = sc.nextLine();

                    System.out.print("Enter Course: ");
                    String course = sc.nextLine();

                    System.out.print("Enter Marks: ");
                    double marks = sc.nextDouble();

                    Student s = new Student(id, name, course, marks);

                    sm.addStudent(s);
                    break;

                case 2:
                    sm.displayStudents();
                    break;

                case 3:
                    System.out.print("Enter Student ID: ");
                    id = sc.nextInt();

                    sm.searchStudent(id);
                    break;

                case 4:
                    System.out.print("Enter Student ID: ");
                    id = sc.nextInt();

                    System.out.print("Enter New Marks: ");
                    marks = sc.nextDouble();

                    sm.updateMarks(id, marks);
                    break;

                case 5:
                    System.out.print("Enter Student ID: ");
                    id = sc.nextInt();

                    sm.deleteStudent(id);
                    break;

                case 6:
                    System.out.print("Enter Student ID: ");
                    id = sc.nextInt();

                    sm.checkStudent(id);
                    break;

                case 7:
                    sm.totalStudents();
                    break;

                case 8:
                    System.out.println("Exiting Program...");
                    break;

                default:
                    System.out.println("Invalid Choice!");
            }

        } while (choice != 8);

        sc.close();
    }
}

