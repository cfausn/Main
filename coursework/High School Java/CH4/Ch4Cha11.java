//Ch4Cha11

import java.text.DecimalFormat; //needed for DecimalFormat

public class Ch4Cha11
{
	public static void main(String args[])
	{
		//variables
		double fValue = 0.0;
		
		//header
		System.out.println("  Celsius				Fahrenheit");
		System.out.println("-----------------------------------------------------");
		
		//decimal format
   	DecimalFormat formatter = new DecimalFormat("##0.0");
		DecimalFormat formatter2 = new DecimalFormat("##");
 		
		for(double cValue = 0.0; cValue <= 20; cValue++)
		{
			fValue = (1.8) * cValue + 32;
			
			System.out.println("  " +formatter2.format(cValue)+" degree(s)			" +formatter.format(fValue)+ " degree(s)");
		}
	}
}