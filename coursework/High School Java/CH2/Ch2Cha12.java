//Ch2Cha12.java

import java.util.Scanner;

public class Ch2Cha12
{
	public static void main(String args[])
	{
		//variables
		String city, cUp, cLow;
		char cChar;
		int number;
		
		//scanner
		Scanner keyboard = new Scanner(System.in);
		
		//inputs
		System.out.print("Enter favorite city: ");
		city = keyboard.nextLine();
		
		//convert and store into variables
		number = city.length();
		cUp = city.toUpperCase();
		cLow = city.toLowerCase();
		cChar = city.charAt(0);
		
		//display
		System.out.print("\nNumber of Characters: " + number);
		System.out.print("\nUppercase: " + cUp);
		System.out.print("\nLowercase: " + cLow);
		System.out.print("\nName of city: " + city);
		System.out.println("\nFirst letter: " + cChar);
		
	}
}