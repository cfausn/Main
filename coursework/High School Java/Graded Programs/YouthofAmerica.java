//YouthofAmerica.java
//Colin Fausnaught, 2/5/13
import java.io.*; //needed for file and ioexception
import java.util.Scanner; //needed for scanner

public class YouthofAmerica
{
	public static void main(String args[]) throws IOException
	{
		//variables
		String name;
		int budget = 0; 
		int runTotal = 0; 
		int sentinal = 0;
		
		//create scanner
		Scanner keyboard = new Scanner(System.in);

		//prompt
		System.out.println("Enter your name: ");
		name = keyboard.nextLine();
		System.out.println("Enter Budget: ");
		budget = keyboard.nextInt();
		
		while(sentinal != -999)
		{
			System.out.println("Enter Money used: ");
			//only give exit message if it hasn't been run yet
			if(sentinal == 0)
				System.out.println("Input -999 to finish entering money used at any time: ");
			sentinal = keyboard.nextInt();
			
			//check to make sure it isn't -999, if it is just ends loop
			if(sentinal != -999)
				runTotal += sentinal;
		}
		
			
		//open the file and filewriter
		FileWriter fwriter = new FileWriter("U:\\14faucol\\Java\\CH4\\YouthofAmerica.txt");
		PrintWriter outputFile = new PrintWriter(fwriter);
		
		//write information to file
		outputFile.println("Colin Fausnaught");
		outputFile.println(name);
		outputFile.println("Budget is $" +budget);
		//check budget
		if(runTotal > budget)
			outputFile.println("Over budget by $" + (runTotal - budget) + ".");			
		else if(runTotal == budget)
			outputFile.println("Exact budget");
		else if(runTotal < budget)
			outputFile.println("Under budget by $" + (budget - runTotal) + ".");
		
		//close the file
		outputFile.close();
	}
}