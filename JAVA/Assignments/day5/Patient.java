package day5;

public class Patient {
	
	// Instance Variables
	int patientId;
	String patientName;
	int daysAdmitted;
	float roomCharges;
	
	
	// Static variables
	static int patientCount = 0;
	static String hospitalName = "CIMS";
	
	
	// Parameterized Constructor
	public Patient(int patientId, String patientName, int daysAdmitted, float roomCharges){
		this.patientId = patientId;
		this.patientName = patientName;
		this.daysAdmitted = daysAdmitted;
		this.roomCharges = roomCharges;
		patientCount++;
	}
	
	public float calculateRoomCharges() {
		float total_room_charges = daysAdmitted * roomCharges;
		return total_room_charges;
	}
	
	
	public void display() {
		System.out.println("==== PATIENT DETAILS ====");
		System.out.println("Patient ID: " + patientId);
		System.out.println("Patient Name: " + patientName);
		System.out.println("Total Room Charges: " + calculateRoomCharges());
		System.out.println("Hospital: " + hospitalName);
	}
	
}
