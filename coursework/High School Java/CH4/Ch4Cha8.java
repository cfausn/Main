//Ch4Cha8

import java.text.DecimalFormat; //needed for DecimalFormat
import java.util.Scanner; //needed for scanner

public class Ch4Cha8
{
	public static void main(String args[])
	{
		//variables
		double years = 0;
		double rainfall = 0; 
		double rainTotal = 0;
		double rainfallAcc = 0;
		final int MONTHS = 12;
		
		//decimal format
   	DecimalFormat formatter = new DecimalFormat("##,##0.00");
		DecimalFormat formatter2 = new DecimalFormat("###");

		//create scanner
		Scanner keyboard = new Scanner(System.in);

		//verification
		System.out.println("Enter years: ");
		years = keyboard.nextInt();
		while(years < 1)
			{
				System.out.println("Invalid input. Please enter positive years: ");
				years = keyboard.nextInt();
				
			}
	
		//loop
		for(int yCount = 1; yCount <= years; yCount++)
		{
			for(int month = 1; month < 13; month++)
				{
				System.out.println("Enter rainfall for year " + yCount + ", month " + month + ".");
				
				rainfall = keyboard.nextInt();
					while(rainfall < 0)
					{	
					System.out.println("Invalid input. Please enter positive rainfall: ");
					rainfall = keyboard.nextInt();
					}
				rainfallAcc += rainfall;
				}
		}
		
		//average calculator
		rainTotal = rainfallAcc / (MONTHS * years);
		
		//display
		System.out.println("There were " + formatter2.format(MONTHS * years) + " months, a total of " + formatter2.format(rainfallAcc) + " inches of rain, \n"+
		"and " + formatter.format(rainTotal) + " inches on average.");
	}
}