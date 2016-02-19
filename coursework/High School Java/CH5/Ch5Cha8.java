//Ch5Cha8

import java.text.DecimalFormat; //needed for DecimalFormat
import java.util.Scanner; //needed for the scanner class

public class Ch5Cha8
{
	public static void main(String args[])
	{
		//method to create a menu
	 	menu();
	}
	
	public static void menu()
	{
		//variables	
		double meters = 0;
		int sentinal = 0;
		
		//create a scanner
		Scanner keyboard = new Scanner(System.in);
		
		//first prompt
		System.out.println("Please enter a distance in meters: ");
		meters = keyboard.nextDouble();
	
		while(meters < 0)
		{
			System.out.println("Please enter a positive number: ");
			meters = keyboard.nextDouble();
		}
	
		while (sentinal != 4)
		{	
			System.out.println("1. Convert to kilometers");
			System.out.println("2. Convert to inches");
			System.out.println("3. Convert to feet");
			System.out.println("4. Exit");
			System.out.println("Please make a selection: ");
			
			sentinal = keyboard.nextInt();
			
			switch(sentinal)
			{
				case 1:
				showKilometers(meters);
				break;
				
				case 2:
				showInches(meters);
				break;
				
				case 3:
				showFeet(meters);
				break;
				
				case 4:
				break;
				
				default:
				System.out.println("Invalid input! Try again");
				break;
			}
		}

	}
	
	/**
		showKilometers calculates and displays meters
		to kilometers
		
		@param m is meters.
	*/
	public static void showKilometers(double m)
	{
		double kilometers = m * 0.001;
		
		//create decimal format
		DecimalFormat formatter = new DecimalFormat("###.##");

		System.out.println(formatter.format(m) + " meters is " + 
		formatter.format(kilometers) + " kilometers.");
	}
	/**
		showInches calculates and displays meters
		to inches
		
		@param met is meters.
	*/

	public static void showInches(double met)
	{
		double inches = met * 39.37;
		
		//create decimal format
		DecimalFormat formatter = new DecimalFormat("###.##");

		System.out.println(formatter.format(met) + " meters is " + 
		formatter.format(inches) + " inches.");
	}
	/**
		showFeet calculates and displays meters
		to feet
		
		@param me is meters.
	*/

	public static void showFeet(double me)
	{
		double feet = me * 3.281;
		
		//create decimal format
		DecimalFormat formatter = new DecimalFormat("###.##");

		System.out.println(formatter.format(me) + " meters is " + 
		formatter.format(feet) + " feet.");
	}
}
