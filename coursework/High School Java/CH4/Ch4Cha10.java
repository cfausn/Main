//Ch4Cha10

import java.text.DecimalFormat; //needed for DecimalFormat
import java.util.Scanner; //needed for scanner

public class Ch4Cha10
{
	public static void main(String args[])
	{
		//variables
		int max = 0; 
		int min = 0; 
		int min2 = 0;
		int input = 0;		
		
		//create scanner
		Scanner keyboard = new Scanner(System.in);
		
		//loop
		while(input != -99)		
		{
			System.out.println("Enter an interger: ");
			input = keyboard.nextInt();
			
			//if/else
			if(input != -99 && max == 0)
				max = input;
			else if(input < max && input != -99)
			{
				min2 = input;
				
				if(min > min2 && min != 0)
				{
					min = min2;
					min2 = 0;
				}
				else if(min == 0)
				{
					min = min2;
					min2 = 0;
				}
				else
					min2 = 0;
			}
			else if(input > max && input != -99)
				max = input;


			
		}
		
		//output
		if(min == 0 && max == 0)
			System.out.println("Error: Not enough values! Please run again.");
		else
			System.out.println("Max: " +max+"\nMin: " +min);
	}
}
			