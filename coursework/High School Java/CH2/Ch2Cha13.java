//Ch2Cha13.java
import java.util.Scanner;

public class Ch2Cha13
{
	public static void main(String[] args)
	{
		//variables
		double meal, fTax, fTip, total;
		final double TAX = 0.0675;
		final double TIP = 0.15;
		
		//scanner
		Scanner keyboard = new Scanner(System.in);
		
		//input
		System.out.print("Enter the price of your meal: ");
		meal = keyboard.nextDouble();
		
		//calculate
		fTax = meal * TAX;
		fTip = (fTax + meal) * TIP;
		total = fTip + fTax + meal;
		
		//output
		System.out.print("\nMeal Charge: " + meal);
		System.out.print("\nTax: " + fTax);
		System.out.print("\nTip: " + fTip);
		System.out.print("\nTotal: " + total);
	}
	
}