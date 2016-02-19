//RockPaperScissors.java
//Colin Fausnaught, 3/14/13

import java.util.Random; //needed for the random class
import java.util.Scanner; //needed for the scanner class

public class RockPaperScissors
{
	public static void main(String args[])
	{
		//variables
		/* the following are for method returns */
		int compAnswer, userAnswer, entryCheck;
		int test = 0;
		
		/* the following are constants holding the
			string references of each choice, used 
			for display at the end of the program.*/
		final String ROCK = "Rock";
		final String PAPER = "Paper";
		final String SCISSORS = "Scissors";
		
		/* the following are String's used to hold
			the appropriate constant based on the
			user's numerical choice, used for 
			display at the end of the program.   */
		String comString = ""; 
		String useString = "";
		
		//a loop to make sure if that if it's a tie it's played again		
		/** 
			I put the loop in the main instead of a method
			because the main is the easiest place to have all the
			return values changed if needed. It serves a 
			duel purpose, valid checking the user's answer and
			allowing the program to automatically run again if there 
			a tie
		*/
		do
		{
			//if statement that is shown if the do while loop
			//is repeated, explaining why the user has to input again.
			if(test == 3)
				System.out.println("There was a tie! Please play again. \n");
			
			//call method to find the computer's choice
			compAnswer = getCompChoice();
		
			//call method to find the user's choice
			userAnswer = getUserChoice();
		
			//call method to check if entry is valid
			entryCheck = checkEntry(userAnswer);
		
			//call method to decide who won
			test = getWinner(compAnswer, entryCheck);
		}
		while(test == 3); //do while will repeat if it's a tie
		
		//assign the choices with their appropriate string names
		
		/**
			For the following code, i didn't use a method.
			I decided that the amount of coding it would take pass,		
			make parameters, and return the answer depending on
			it's choices would require more effort by
			passing then it was worth, and it looks more organized
			like this.
		*/
		if(compAnswer == 1)
			comString = ROCK;
		else if(compAnswer == 2)
			comString = PAPER;
		else if(compAnswer == 3)
			comString = SCISSORS;
		
		if(entryCheck == 1)
			useString = ROCK;
		else if(entryCheck == 2)
			useString = PAPER;
		else if(entryCheck == 3)
			useString = SCISSORS;
		
		//display the results based on the outcome from variable test
		if(test == 1)
		{
			System.out.println("Computer chose " + comString + " \nUser chose "
			+ useString + " \nComputer won.");
		}
		else if(test == 2)
		{
			System.out.println("Computer chose " + comString + " \nUser chose "
			+ useString + " \nUser won.");
		}
		
	}
	
	/**
		getCompChoice uses a random number
		generator to decide what choice the
		computer will make in Rock Paper Scissors
		(numerically).
		
		@return the computer's choice
	*/
	public static int getCompChoice()
	{
		//variable to store the computer's choice
		int compChoice = 0;
		
		//Create a random class object
		Random randomNumbers = new Random();
		
		//get a random number from 0-3. Loop makes sure
		//that the number won't be 0 or anything higher
		//than 3, thus in the range of 1-3.
			
		while(compChoice == 0)
		{
			compChoice = randomNumbers.nextInt(3);
		}
		
		return compChoice;
	}
	
	/**
		getUserChoice allows the user to input
		their choice numerically
		
		@return the user's choice
	*/
	public static int getUserChoice()
	{
		//variable to store the user's choice
		int userChoice = 0;
				
		//create a scanner
		Scanner keyboard = new Scanner(System.in);

		//print a menu for the user to choice from
		System.out.println("******** Rock Paper Scissors *******");
		System.out.println("Please choose an option from the menu");
		System.out.println("---------- For Rock enter 1 ---------");
		System.out.println("--------- For Paper enter 2 ---------");
		System.out.println("-------- For Scissors enter 3 --------");
		System.out.println("Choice: ");
		userChoice = keyboard.nextInt();
		
		return userChoice;
	}
	
	/**
		checkEntry checks the user's input to 
		make sure that the entry is valid. If
		it's not it prompts the user to enter 
		a different value
		
		@param userAns is the user's input
		
		@return valid, the valid new input of the user
				  if it was not valid already.
	*/
	public static int checkEntry(int userAns)
	{
		//variable to hold the valid answer
		int valid = userAns;
		
		//create a scanner
		Scanner keyboard2 = new Scanner(System.in);
		
		//constants that the user needs to be in the range of
		final int CROCK = 1;
		final int CSCISSOR = 3;
		
		/** input validation. The if statement first sees if the
		user's input is a valid one. If it isn't, a while statement
		prompts the user to enter a correct answer and continues to
		prompt until a valid input is entered.
		The else statement says that the user's input is valid
		because it must be if it's within the range.
		*/
		if(userAns < CROCK || userAns > CSCISSOR)
		{
			while(valid < CROCK || valid > CSCISSOR)
			{
				System.out.println("Invalid input! Please input a value from 1-3: ");
				valid = keyboard2.nextInt();	
			}
		}
		else 
			valid = userAns;
			
		return valid;
	}
	
	/**
		getWinner compares the user and
		the computer's choices to see who
		won numerically
		
		@param comp is the computer's choice
		@param user is the user's choice
		
		@return code, which will decide whether
		the loop needs to reiterate or which outcome
		will be displayed.
	*/

	public static int getWinner(int comp,int user)
	{
		int code = 0;
		
		//variables to stand for rock and scissors,
		//since they don't work as well together 
		//and need a special exception to work correctly
		
		final int RO = 1;
		final int SC = 3;
		
		/**
			The following if and else if statements
			are used to decide who will win the match 
			up. It makes special exceptions for Rock
			and Scissors, since the value for rock is
			1 and scissors is 3. It allows rock to
			beat scissors.
		*/
		if(comp > user)
			code = 1;
		else if(comp < user)
			code = 2;
		else if(comp == RO && user == SC)
			code = 1;
		else if(comp == SC && user == RO)
			code = 2;
		else if(comp == user)
			code = 3;
		
		return code;
	}
}