package day5;

public class PatientMain {
	public static void main(String[]  args) {
		Patient p1 = new Patient(101, "Rahul Sharma", 3, 2500);
		Patient p2 = new Patient(102, "Priya Verma", 5, 3000);
		Patient p3 = new Patient(103, "Amit Kumar", 2, 1800);
		
		Patient[] patients = {p1, p2, p3};
		
		for (Patient p: patients) {
			p.display();
			
		}
		
		System.out.println("Hospital Name: " + Patient.hospitalName);
		System.out.println("Total Patient Count:" + Patient.patientCount);
		
 	}
}
