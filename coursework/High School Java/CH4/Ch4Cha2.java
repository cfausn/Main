//Ch4Cha2

import java.io.*; //needed for file and ioexception
import java.util.Scanner; //needed for scanner

public class Ch4Cha2
{
	public static void main(String args[])
	{
		//variables
		int distance, speed, time,num;
		
		//create scanner
		Scanner keyboard = new Scanner(System.in);
		
		//prompt
		System.out.println("Enter Speed: ");
		speed = keyboard.nextInt();
		while(speed < 0)
			{
				System.out.println("Invalid input. Please enter a positive speed: ");
				speed = keyboard.nextInt();
			}
			
		System.out.println("Enter Hours: ");
		time = keyboard.nextInt();
		while(time < 0)
			{
				System.out.println("Invalid input. Please enter positive hour(s): ");
				time = keyboard.nextInt();
			}
			
		//output
		System.out.println("\nHour      Distance Traveled");
		System.out.println("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
				
		for(num = 1; num <= time; num++)
			{
				distance = speed * num;
				
				System.out.println(num + "                " + distance);
			}
		}
	}