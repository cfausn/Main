//CallRainFall.java
import java.util.Scanner; //needed for the scanner class
import java.text.DecimalFormat; //needed for DecimalFormat

public class CallRainFall
{
	public static void main(String[] args)
	{	
		//basic info for array
		final int MONTHS = 12;
		double[] rainFall = new double[MONTHS];
		double total = 0.0;
		double average = 0.0;
		String most;
		String least;
		
		//create decimal format
		DecimalFormat formatter = new DecimalFormat("###.##");

		//create a scanner
		Scanner keyboard = new Scanner(System.in);

		//call the class to store the array
		RainFall rain = new RainFall();
		
		
		//get rainFall and place in array
		for(int index = 0; index < MONTHS;index++)
		{
			System.out.println("Enter rainfall for month " + (index +1)+".");
			rainFall[index] = keyboard.nextDouble();			
		}
		
		//store array in class
		for(int ind = 0; ind < MONTHS; ind++)
			rain.storeRain(rainFall[ind]);
		
		//call the class to calculate total, average, most and least rain
		total = rain.Total();
		average = rain.Average(total);
		most = rain.Most();
		least = rain.Least();
		
		//print
		System.out.println("Total rainfall is: " + formatter.format(total)+" inches" + "\nMonthley Average is: " + 
		formatter.format(average) + " inches" + "\nMonth with most rain was: " + most + "\nMonth with least rain was: " +least);
	}
}
