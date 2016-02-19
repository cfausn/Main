//Ch3Cha7.java

import java.util.Scanner; //needed for scanner

public class Ch3Cha7
{
	public static void main(String args[])
	{
		//variable
		String name1, name2, name3;
		
		//create scanner
		Scanner keyboard = new Scanner(System.in);
		
		//prompt
		System.out.println("Enter name 1: ");
		name1 = keyboard.nextLine();
		System.out.println("Enter name 2: ");
		name2 = keyboard.nextLine();
		System.out.println("Enter name 3: ");
		name3 = keyboard.nextLine();
		System.out.println("\n");
		
		//decision structure
		if(name1.compareTo(name2) < 0 && name1.compareTo(name3) < 0)
		{
			if(name2.compareTo(name3) < 0)
			System.out.println(name1 + "\n" + name2 + "\n" + name3);
			
			else if(name2.compareTo(name3) > 0)
			System.out.println(name1 + "\n" + name3 + "\n" + name2);
			
			else
			System.out.println(name1 + "\n" + name2 + "\n" + name3);
		}
		else if(name1.compareToIgnoreCase(name2) > 0 && name1.compareToIgnoreCase(name3) > 0)
		{
			if(name2.compareToIgnoreCase(name3) < 0)			
			System.out.println(name2 + "\n" + name3 + "\n" + name1);
			
			else if(name2.compareToIgnoreCase(name3) > 0)
			System.out.println(name3 + "\n" + name2 + "\n" + name1);
			
			else
			System.out.println(name2 + "\n" + name3 + "\n" + name1);
		}
		else if(name1.compareToIgnoreCase(name2) < 0 && name1.compareToIgnoreCase(name3) > 0)
		{
			if(name2.compareToIgnoreCase(name3) < 0)
			System.out.println(name1 + "\n" + name2 + "\n" + name3);
		
			else if(name2.compareToIgnoreCase(name3) > 0)
			System.out.println(name3 + "\n" + name1 + "\n" + name2);
			
			else
			System.out.println(name1 + "\n" + name2 + "\n" + name3);
		}
	}
		
}