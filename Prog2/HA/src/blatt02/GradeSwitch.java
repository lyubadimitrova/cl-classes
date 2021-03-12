package blatt02;

import java.util.Scanner;


public class GradeSwitch {

	public static int getGrade() {
		int grade;
		System.out.println("Please enter a valid German grade (1-5): ");
		do {
			Scanner scanner = new Scanner(System.in);
			System.out.print("German grade: ");
			grade = Integer.parseInt(scanner.next());
		}while(grade<1||grade>5);
		return grade;
	}
	public static void main(String[] args) {
		int note = getGrade();
		switch(note) {
		case 1:
			System.out.print("Amerikanische Note: "+"A"); break;
		case 2:
			System.out.print("Amerikanische Note: "+"B"); break;
		case 3: 
			System.out.print("Amerikanische Note: "+"C"); break;
		case 4:
			System.out.print("Amerikanische Note: "+"D"); break;
		case 5:
			System.out.print("Amerikanische Note: "+"F"); break;
		default:
		}
	}

}
