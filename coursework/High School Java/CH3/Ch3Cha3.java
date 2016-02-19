//Ch3Cha3.java

import java.util.Scanner; //needed for scanner

public class Ch3Cha3
{
	public static void main(String args[])
	{
		//variables
		double weight, height, BMI;
		
		//create scanner
		Scanner keyboard = new Scanner(System.in);
		
		//prompt
		System.out.println("Enter weight: ");
		weight = keyboard.nextDouble();
		System.out.println("Enter height: ");
		height = keyboard.nextDouble();
		
		//calculate 
		BMI = weight * 703 / (height * height);
		
		if(BMI >= 18.5 && BMI <= 25)
			System.out.println("BMI is " + BMI + ". Optimal BMI.");
		else if (BMI > 25)
			System.out.println("BMI is " + BMI + ". Overweight.");
		else
			System.out.println("BMI is " + BMI + ". Underweight.");
		
		}
	}