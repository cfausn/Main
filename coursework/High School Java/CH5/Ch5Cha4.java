//Ch5Cha4
import javax.swing.JOptionPane; //needed for jOptionPane
import java.text.DecimalFormat; //needed for DecimalFormat

public class Ch5Cha4
{
	public static void main(String args[])
	{
		//global variables
		final double SQRFTPERRUN = 115;  /*how many square feet can be covered in 8 hours
														and how much a gallon of paint can cover*/
		final double HOURSPERRUN = 8;		//how many hours it takes to use a gallon
		final double COSTPERHOUR = 18.00;//how much they're paid per hour
		String mainInput;
		double roomsReturn, perGallonReturn, wallspaceReturn,
		 totalPrice;
		double sqrftReturn = 0;
		double galReq = 0;
		double laborReq = 0;
		double paintCost = 0;
		double laborPrice = 0;
		int counter = 0; //used for the functions to know what room they're in
			
		//decimal format
   	DecimalFormat formatter = new DecimalFormat("##,##0.00");
		DecimalFormat formatter2 = new DecimalFormat("###");
		DecimalFormat formatter3 = new DecimalFormat("###.#");

 		//call function for amount of rooms
		roomsReturn = getRooms();	
		//call function for price of paint per gallon
		perGallonReturn = getPaint();
			
		for(double sentinal = 1; sentinal <= roomsReturn; sentinal++)
		{ 
			counter += 1;
			
			//call function for square feet per room
			sqrftReturn += getSquareFeet(counter);

		}
		//call function for deciding how many gallons of paint are needed
		galReq = getGals(SQRFTPERRUN, sqrftReturn);
		
		//call function for deciding how many hours of labor are required
		laborReq = getLaborHours(SQRFTPERRUN, HOURSPERRUN, sqrftReturn);
			
		//call function for determining how much the paint costs
		paintCost =getPaintCost(perGallonReturn, galReq);
			
		//call function for determining the labor charges
		laborPrice = getLaborPrice(laborReq, COSTPERHOUR);
	
	//call function to calculate the total
	totalPrice = getTotal(paintCost, laborPrice);
	
	//display the data
	JOptionPane.showMessageDialog(null, "Number of gallons required to paint are: " + formatter2.format(galReq) + " gallons,\n "+
	"hours of labor required are: " + formatter3.format(laborReq) + " hours,\n cost of the paint is: $" + formatter.format(paintCost) + 
	",\n the labor charges are: $"+ formatter.format(laborPrice) + ",\n and the total cost is: $" + formatter.format(totalPrice));
	
}	

	/**
		getRooms gets and returns the amount
		of rooms in an area.
		@return the amount of rooms
	*/
	
	public static double getRooms()
	{
		String input;	/*I'm going to need a new "String input" each time
							each time i use JOptionPane, so i'm just going to
							number them in order to make it easier, then i'll
							parse it to a more sensible variable */							
		double rooms;
		
		input = JOptionPane.showInputDialog("Enter the number of rooms");	
		rooms = Double.parseDouble(input);
		
		return rooms;
	}
	
	/**
		getPaint gets and returns the paint price
		per gallon
		@return the amount of paint per gallon
	*/
	
	public static double getPaint()
	{
		String input2;
		double paint = 0.0;
		
		input2 = JOptionPane.showInputDialog("Enter the price of paint per Gallon");	
		paint = Double.parseDouble(input2);
		
		return paint;
	}
	
	/**
		getSquareFeet gets and returns the amount
		of rooms in an area.
		@param count is what room it's on
		@return the amount of rooms
	*/
	
	public static double getSquareFeet(int count)
	{
		String input3;
		double squareFeet;
		
		input3 = JOptionPane.showInputDialog("Enter the Square Feet of" +
		" the wall space in room " + count);	
		squareFeet = Double.parseDouble(input3);
		
		return squareFeet;
	}
	
	/**
		getGals decides how many gallons of paint 
		need to be used
		
		@param SQRFTPERGAL is the constant that holds
				 the amount of wallspace taken by a gallon
				 of paint
		@param sqrftReturn is the amount of square feet
				 in the rooms
		@return the number of gallons
	*/
	public static double getGals(final double FTPERGAL, double squareFeet)
	{
		double gallons;
		int intGallon;
		
		if(squareFeet <= FTPERGAL)
			gallons = 1;
		else
			gallons = squareFeet / FTPERGAL;
		
		intGallon = (int)gallons;
		
		if(intGallon < gallons)
			intGallon += 1;
		
		return intGallon;
	}
	
	/**
		getLaborHours decides how much time is needed to
		paint
		
		@param SQRFT is the amount of square feet
				 that can be painted per 8 hours
		@param HRS is the constant that holds 8
		@param sqrFeet holds the square feet of the 
				 area
	
		@return the number of hours
	*/

	public static double getLaborHours(final double SQRFT, final double HRS, double sqrFeet)
	{
		double hoursUsed;
		double remainder;
		
		hoursUsed = (sqrFeet / SQRFT) * HRS;
					
		return hoursUsed;
	}
	/**
		getPaintCost decides how the paint costs
		
		@param price is the price per gal		
		@param amountOfPaint is the number of gallons
				 used

		@return the paint cost
	*/

	public static double getPaintCost(double price, double amountOfPaint)
	{
		double paintTotal = price * amountOfPaint;
		
		return paintTotal;
	}
	
	/**
		getLaborPrice calculates how much the labor
		will cost
		
		@param lHours is the amount of labor hours
		@param COST is the amount they get paid
		
		@return labor cost
	*/
	public static double getLaborPrice(double lHours,final double COST)
	{
		double totalCost = lHours * COST;
		
		return totalCost;
	
	}
	
	/**
		getTotal will calculate the total
		
		@param paint is the paint cost
		@param labor is the labor cost
		
		@return the total
	 */
	
	public static double getTotal(double paint,double labor)
	{	
		double endTotal = paint + labor;
		return endTotal;
	}
}