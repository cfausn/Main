//Rainfall class

public class RainFall
{
	//fields
	private final int MON = 12;
	private double total = 0.0;
	private double average = 0.0;
	private int counter = 0;
	private double[] rain = new double[MON];
	private String[] months = {"January", "February", "March",
										"April", "May", "June", "July",
										"August", "September", "October",
										"November", "December" };
	
	
	/** Used Default Constructor **/
	
	/**
		storeRain stores info from the call
		program into the class
		
		@param rainF is the input from the other program
	*/
	public void storeRain(double rainF)
	{
		rain[counter] = rainF;
		counter++;
	}
	
	/**
		Total calculates the total with information given
		
		@return total returns total to the program
	*/
	public double Total()
	{
		double total = 0.0;
		
		for(int index = 0; index < MON; index++)
			total += rain[index];
			
		return total;
	}
	
	/**
		Average calculates the average of the information given
		
		@return average returns average to the program
	*/
	public double Average(double tot)
	{
		double average = tot / MON;
		
		return average;
	}
	/**
		Most decides which month had the highest rain fall and 
		assigns it with it's string counterpart
		
		@return highestString is the most rain fall month in word format
	*/
	public String Most()
	{
		double highest = rain[0];
		String highestString = months[0];
		
		for(int index = 0; index < MON; index++)
		{
			if(rain[index] > highest)
			{
				highest = rain[index];
				highestString = months[index];
			}
		}
		
		return highestString;
	}
	
	/**
		Least decides which month had the lowest rain fall and
		assigns it with it's string counterpart
		
		@return lowestString is the least rainfall month in word format
	*/
	
	public String Least()
	{
		double lowest = rain[0];
		String lowestString = months[0];
		
		for(int index = 0; index < MON; index++)
		{
			if(rain[index] < lowest)
			{
				lowest = rain[index];
				lowestString = months[index];
			}
		}
		
		return lowestString;
	}

}	