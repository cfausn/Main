//GreensDepartmentStore.java

import java.text.DecimalFormat; //needed for DecimalFormat
import java.util.Scanner; //needed for scanner

public class GreensDepartmentStore
{
	public static void main(String args[])
	{
		//variables
		double purchase = 0.0, 
					 total = 0.0,
					 cDiscount = 0.0, 
					 cTotal = 0.0,
					 sTotal = 0.0,
					 tTotal = 0.0;
		final double tax = .07;
		String senior = ""; 
		String coupon = "";
		final String yes = "Yes";
		final String no  = "No";
	
		//decimal format
   	DecimalFormat formatter = new DecimalFormat("##,##0.00");
		
		//create scanner
		Scanner keyboard = new Scanner(System.in);

		//prompt
		System.out.println("Are you over 55?");
		senior = keyboard.nextLine();

		System.out.println("Do you have a coupon?");
		coupon = keyboard.nextLine();

		System.out.println("What's the price of your purchase?");
		purchase = keyboard.nextDouble();
		


		//decide if senior
		if(senior.equals(yes))
		{
			sTotal = purchase * 0.2;	
			total = purchase - sTotal;
		}
		else if(senior.equals(no))
			total = purchase;

		
		//decide if coupon
		if(coupon.equals(yes))
		{
			System.out.println("How much is the discount of the coupon (in decimal format)?");
			cDiscount = keyboard.nextDouble();
			cTotal = cDiscount * total;
			total -= cTotal;
		}
		else if(coupon.equals(no))
			total = total;
			//just to give the else if something to do
			
		//tax
		tTotal = tax * total;
		total = total + tTotal;
		if(total == 0)
			total = purchase;
		
		//display time
		System.out.println("Senior Discount: $" +	formatter.format(sTotal) +"\nCoupon Discount: $" +
								formatter.format(cTotal) + "\nTax Amount: $" + formatter.format(tTotal) + 
								"\nTotal due: $" + formatter.format(total));
	}
}