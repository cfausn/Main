//Ch4Cha15

import java.text.DecimalFormat; //needed for DecimalFormat
import java.io.*; //needed for file and ioexception
import java.util.Scanner; //needed for scanner

public class Ch4Cha15
{
	public static void main(String args[]) throws IOException
	{
		//variables
		String filenameIn, filenameOut;
	
		//create scanner
		Scanner keyboard = new Scanner(System.in);

		//prompt
		System.out.println("Enter input file name: ");
		filenameIn = keyboard.nextLine();
		System.out.println("Enter output file name: ");
		filenameOut = keyboard.nextLine();
		
		//create the input file and open for reading
		File file = new File(filenameIn);
		Scanner inputFile = new Scanner(file);
				
		//open the file and filewriter
		PrintWriter outputFile = new PrintWriter(filenameOut);
		
		//read the values from file
		while(inputFile.hasNext())
		{	
			String tempString ="";
			String tempStringUp ="";
			
			tempString = inputFile.nextLine();
			tempStringUp = tempString.toUpperCase();
			outputFile.println(tempStringUp);
		}
		
		//close the files
		outputFile.close();
		inputFile.close();
		
		 
	}
}