//Ch5Cha6

import java.text.DecimalFormat; //needed for DecimalFormat

public class Ch5Cha6
{
	public static void main(String args[])
	{
		//variables
		double c = 0;

		//create decimal format
		DecimalFormat formatter = new DecimalFormat("###.##");
		
		for(double farenheit = 0; farenheit <= 20; farenheit++)
		{
			c = celsius(farenheit);
			
			System.out.println("Temp in Farenheit: "+ formatter.format(farenheit) +
			" Temp in Celsius: " + formatter.format(c));
		}
	}
	
	public static double celsius(double f)
	{
		double cTotal = 0.55555555 * (f-32);
		return cTotal;
	}

}