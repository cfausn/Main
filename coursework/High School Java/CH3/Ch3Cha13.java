//Ch3Cha13.java

import java.text.DecimalFormat; //needed for DecimalFormat
import java.util.Scanner; //needed for scanner

public class Ch3Cha13
{
	public static void main(String args[])
	{
		//variables
		String pack;
		char packChar;
		double hours, nHours, total;
	
		//decimal format
   	DecimalFormat formatter = new DecimalFormat("##,##0.00");
		
		//create scanner
		Scanner keyboard = new Scanner(System.in);

		//prompt
		System.out.println("Enter Package letter: "); 
		pack = keyboard.nextLine();
		packChar = pack.charAt(0);
		System.out.println("Enter hours: ");
		hours = keyboard.nextDouble();
		
		//decision structure
		switch(packChar)
			{
				case 'a':
				case 'A':
					if(hours > 10)
						{
							nHours = hours - 10;
							total = 9.95 +(nHours * 2);
							System.out.println("Your total is: $" +  formatter.format(total) + ".");
						}
					else
						total = 9.95;
						System.out.println("Your total is: $" +  formatter.format(total) + ".");
					break;
				case 'b':
				case 'B':
					if(hours > 20)
						{
							nHours = hours - 20;
							total = 13.95 +(nHours * 1);
							System.out.println("Your total is: $" +  formatter.format(total) + ".");
						}
					else
						total = 13.95;
						System.out.println("Your total is: $" +  formatter.format(total) + ".");
					break;
				case 'c':
				case 'C':
					total = 19.95;
					System.out.println("Your total is: $" +  formatter.format(total) + ".");			
					break;
				default:
					System.out.println("Error");
			}
			
	}
		
}