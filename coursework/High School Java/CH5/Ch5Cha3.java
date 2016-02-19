//Ch5Cha3

/** You must complete this program so it calculates
	 and displays the area of a rectangle.
*/

import javax.swing.JOptionPane; //needed for JOptionPane

public class Ch5Cha3
{
	public static void main(String[] args)
	{
	
		double length,		// The rectangle's length
				 width, 		// The rectangle's width
				 area;		// The rectangle's area
				 
		//get the rectangle's length from the user.
		length = getLength();
		
		//get the rectangle's width from the user
		width = getWidth();
		
		//get the recangle's area.
		area = getArea(length, width);
		
		//Display the rectangle data.
		displayData(length, width, area);
	}
	
	/**
		getLength gets the length from the user
		@return the length 
		
	*/
	public static double getLength()
	{	
		double len;
		len = Double.parseDouble(JOptionPane.showInputDialog(null, "Enter length: "));
		
		return len;
	}
	/**
		getWidth gets the width from the user
		@return the width
	*/
	public static double getWidth()
	{
		double wid;
		wid = Double.parseDouble(JOptionPane.showInputDialog(null, "Enter width: "));
		return wid;
	}
	/**
		getArea calculates area from width and length
		@param length
		@param width
		@return the area
		
	*/
	public static double getArea(double len,double wid)
	{
		double are = len * wid;
		return are;
	}
	
	/**
		displayData displays everything collected up to this point
		@param length
		@param width
		@param area
	*/
	public static void displayData(double len, double wid, double are)
	{
		JOptionPane.showMessageDialog(null, "Length is " + len + ", width is " + wid
		+ ", and area is " + are + ".");

	}
}