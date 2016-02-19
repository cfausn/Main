//Ch5Cha5

import java.text.DecimalFormat; //needed for DecimalFormat

public class Ch5Cha5
{
	public static void main(String args[])
	{
		//variables
		double d = 0;
		final double GRAVITY = 9.8;
		
		//create decimal format
		DecimalFormat formatter = new DecimalFormat("###.#");
		
		for(double time = 1; time <= 10; time++)
		{
			d = fallingDistance(GRAVITY, time);
			
			System.out.println("Distance fallen at "+ formatter.format(time) + " seconds "+
			"is " + formatter.format(d) + " meters.");
		}
	}
	
	public static double fallingDistance(final double G, double t)
	{
		double distance = 0.5 * (G *(t*t));
		
		return distance;
	}
}

