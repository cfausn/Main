//Ch3Cha14.java

import java.text.DecimalFormat; //needed for DecimalFormat
import java.util.Scanner; //needed for scanner

public class Ch3Cha14
{
	public static void main(String args[])
	{
		//variables
		String pack;
		char packChar;
		double hours, nHours, total, bHours, bTotal;
	
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
							if(total > 18.95)
								{					
									bHours = hours - 20;
									bTotal = 13.95 +(bHours * 1);
									System.out.println("You could have saved $" + formatter.format(total - bTotal) + 
									" if you used package B.");
									if(total > 19.95)
										System.out.println("You could have saved $" + formatter.format(total - 19.95) + 
										" if you used package C.");
								}
							
						}
					else
					{
						total = 9.95;
						System.out.println("Your total is: $" +  formatter.format(total) + ".");
					}
					break;
				case 'b':
				case 'B':
					if(hours > 20)
						{
							nHours = hours - 20;
							total = 13.95 +(nHours * 1);
							System.out.println("Your total is: $" +  formatter.format(total) + ".");
							if(total > 19.95)
								{
										System.out.println("You could have saved $" + formatter.format(total - 19.95) + 
										" if you used package C.");
								}
						}
					else
					{
						total = 13.95;
						System.out.println("Your total is: $" +  formatter.format(total) + ".");
					}
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