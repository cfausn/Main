//Ch3Cha9.java

import java.text.DecimalFormat; //needed for DecimalFormat
import javax.swing.JOptionPane; //needed for JOptionPane

public class Ch3Cha9
{
	public static void main(String args[])
	{
		//variables
		double lbs, miles, rate, mod, end;
		int getNum;
		final int SMILES = 500;
		String input;
		
		//prompt
		input = JOptionPane.showInputDialog("Enter weight: ");
		lbs = Double.parseDouble(input);
		
		input = JOptionPane.showInputDialog("Enter miles: ");
		miles = Double.parseDouble(input);
		
		//decimal format
   	DecimalFormat formatter = new DecimalFormat("##0.00");

		//decide rate
		if(lbs <= 2)
			rate = 1.1;
		else if(lbs > 2 && lbs <= 6)
			rate = 2.2;
		else if(lbs > 6 && lbs <= 10)
			rate = 3.7;
		else if(lbs > 10)
			rate = 3.8;
		else
			rate = 0;
	
		//decide the price
		getNum = (int)miles / SMILES;
		mod = miles % SMILES;
		if(mod > 1)
			getNum += 1;
		
		//calculate
		end = getNum * rate;
		
		//display
		JOptionPane.showMessageDialog(null, "The end price is: $" + formatter.format(end) + ".");
		
	}
	
}