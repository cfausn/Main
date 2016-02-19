//CallDriverExam.java

import java.util.Scanner; //needed for the scanner class

public class CallDriverExam
{
	public static void main(String[] args)
	{
		//basic info and variables
		final int QUESTIONS = 20;
		String hold = " ";
		char cStore = ' ';
		int correct = 0;
		int incorrect = 0;
		boolean passed;
		
		//call the class
		DriverExam exam = new DriverExam();
		
		//create a scanner
		Scanner keyboard = new Scanner(System.in);
		
		
		System.out.println("Enter your answers in Upper Case: ");
		//get answers and store them in class
		for(int index = 0; index < QUESTIONS; index++)
		{
			System.out.println((index+1) + ": ");
			hold = keyboard.nextLine();
			
			cStore = hold.charAt(0);
			
			//input validation
			while(cStore != 'A' && cStore != 'B' && cStore != 'C' && cStore != 'D')			
			{
				System.out.println("Error. Please Enter a valid answer: ");
				hold = keyboard.nextLine();
				
				cStore = hold.charAt(0);
			}
			
			
			exam.store(cStore);
		}
		
		//call function to grade the test
		exam.grade();
		
		//call function to return the total correct
		correct = exam.totalCorrect();
		
		//call function to return the total incorrect
		incorrect = exam.totalIncorrect();
		
		//call function to see if student passed
		passed = exam.passed();
		
		
		//display the results
		if(passed == true)
			System.out.println("Student passed.");
		else if(passed == false)
			System.out.println("Student did not pass.");
			
			
		System.out.println("Total correct was: " + correct);
		System.out.println("Total incorrect was: " + incorrect);
		
		
		//call questionsMissed, which displays by itself
		exam.questionsMissed();
			
	}
}