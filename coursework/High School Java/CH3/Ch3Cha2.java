//Ch3Cha2.java

import java.util.Scanner; //needed for scanner

public class Ch3Cha2
{
	public static void main(String args[])
	{
		//variables
		int day, month,year;
		
		//create scanner
		Scanner keyboard = new Scanner(System.in);
		
		//prompt
		System.out.println("Enter day of month: ");
		day = keyboard.nextInt();
		System.out.println("Enter month in numerals: ");
		month = keyboard.nextInt();
		System.out.println("Enter last two digits of year: ");
		year = keyboard.nextInt();
		
		//decision statement
		if((day * month) == year)
			System.out.println("Date is magic!");
		else
			System.out.println("Date is not magic.");
			
	}
}