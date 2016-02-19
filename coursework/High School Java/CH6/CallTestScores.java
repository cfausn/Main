//call TestScores Class
import java.util.Scanner;
import java.text.DecimalFormat; //needed for DecimalFormat

public class CallTestScores
{
	public static void main(String[] args)
	{
		double test1 = 0.0;
		double test2 = 0.0;
		double test3 = 0.0;
		double average = 0.0;
		
		//create decimal format
		DecimalFormat formatter = new DecimalFormat("##.##");
		Scanner keyboard = new Scanner(System.in);
		
		System.out.println("Enter Test Score 1: ");
		test1 = keyboard.nextDouble();
		System.out.println("Enter Test Score 2: ");
		test2 = keyboard.nextDouble();
		System.out.println("Enter Test Score 3: ");
		test3 = keyboard.nextDouble();
		
		TestScores scores = new TestScores(test1, test2, test3);
		
		scores.setTest1(test1);
		scores.setTest2(test2);
		scores.setTest3(test3);
		average = scores.average(test1,test2,test3);
		System.out.println("Average is: " +formatter.format(average));
	}
}