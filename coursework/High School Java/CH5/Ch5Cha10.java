//Ch5Cha10

import javax.swing.JOptionPane; //needed for JOptionPane

public class Ch5Cha10
{
	public static void main(String args[])
	{
		//call variables
		
		/*
			ns is first number of shares
			sp is sale price per share
			sc is sale commission
			pp is purchase price per share
			pc is purchase commision paid
			nns is secound number of shares
		*/
		double ns, sp, sc, pp, pc, nns, profit;
		
		ns = getNS();
		sp = getSP();
		sc = getSC();
		nns = getNNS();
		pp = getPP();
		pc = getPC();
		
		profit = getProfit(ns,sp,sc,nns,pp,pc);
		
		if(profit > 0)
			JOptionPane.showMessageDialog(null, "Net profit of $" + profit);
		else
		{
			profit = profit * -1;
			JOptionPane.showMessageDialog(null, "Net loss of $" + profit);
		}
	}

	/**
		getNS gets the first ns value
		to be plugged in at the end
		
		@return the first ns value
	*/
	public static double getNS()
	{
		double valid;
		String input;
		
		input = JOptionPane.showInputDialog("Enter first number of shares: ");	
		valid = Double.parseDouble(input);
		
		return valid;
	}
	/**
		getSP gets the sp value
		to be plugged in at the end
		@return the sp value
	*/
	public static double getSP()
	{
		double valid2;
		String input2;
		
		input2 = JOptionPane.showInputDialog("Enter sale price per share: ");	
		valid2 = Double.parseDouble(input2);
		
		return valid2;
	}
	
	/**
		getSC gets the sc value
		to be plugged in at the end
		
		@return the sc value
	*/
	public static double getSC()
	{
		double valid3;
		String input3;
		
		input3 = JOptionPane.showInputDialog("Enter sale commission paid: ");	
		valid3 = Double.parseDouble(input3);
		
		return valid3;
	}
	
	/**
		getPP gets the pp value
		to be plugged in at the end
		
		@return the pp value
	*/
	public static double getPP()
	{
		double valid4;
		String input4;
		
		input4 = JOptionPane.showInputDialog("Enter purchase price per share: ");	
		valid4 = Double.parseDouble(input4);
		
		return valid4;
	}
	
	/**
		getPC gets the pc value
		to be plugged in at the end
		
		@return the pc value
	*/
	public static double getPC()
	{
		double valid5;
		String input5;
		
		input5 = JOptionPane.showInputDialog("Enter purchase commission paid: ");	
		valid5 = Double.parseDouble(input5);
		
		return valid5;
	}	
	
	/**
		getNNS gets the secound ns value
		to be used at the end
		
		@return the secound ns value
	*/
	public static double getNNS()
	{
		double valid6;
		String input6;
		
		input6 = JOptionPane.showInputDialog("Enter secound number of sales: ");	
		valid6 = Double.parseDouble(input6);
		
		return valid6;
	}

	/**
		getProfit uses the algorithm given in the book
		to decide what the profit or loss is based
		on the input
		
		@param pns is the first ns value
		@param psp is the sp value
		@param psc is the sc value
		@param pnns is the secound ns value
		@param ppp is the pp value
		@param ppc is the pc value
		
		@return the profit or loss
	*/
	public static double getProfit(double pns,double psp,double psc,double pnns,double ppp,double ppc)
	{
		double profit = ((pns * psp) - psc) - ((pnns * ppp) + ppc);
		
		return profit;
	}
}