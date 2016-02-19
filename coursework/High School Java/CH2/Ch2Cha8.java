//Ch2Cha8.java

public class Ch2Cha8
{
	public static void main(String args[])
	{
		//variables
		double purchase, sTax, cTax, tTax, total;
		final double STATE = .04;
		final double COUNTY = .02;
		
		//scanner
		Scanner keyboard = new Scanner(system.in);
		
		//inputs
		System.out.print("Enter amount of purchase: ");
		purchase = keyboard.nextLine();
		
		//calculate
		sTax = STATE * purchase;
		cTax = COUNTY * purchase;
		tTax = cTax + sTax;
		total = purchase + cTax + sTax;
		
	}
}
