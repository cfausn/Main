//GrPrg1.java

public class StockTransaction
{
	public static void main(String[] args)
	{
		//variables
		final double PPRICE = 32.87, SPRICE = 33.92,
		COMMISSION = 0.02, SHARES = 1000;
		
			/***Reminder***
			the s in sPPrice and sSprice stands for Shares.
			All other s's stand for sell, as in how much he sells for.
			*/
			
		double sPPrice, sSPrice, pCom, sCom, gain, comGain, total;
		
		//compute
		sPPrice = PPRICE * SHARES;
		sSPrice = SPRICE * SHARES;
		pCom = COMMISSION * sPPrice;
		sCom = COMMISSION * sSPrice;
		gain = sSPrice - sPPrice;
		comGain = pCom + sCom;
		total =(gain - comGain) * -1;
		
		
		//display
		System.out.println("Payed: $" + sPPrice);
		System.out.println("Bought commission: $" + pCom);
		System.out.println("Sold for: $" + sSPrice);
		System.out.println("Sold commission: $" + sCom);
		System.out.println("Gained $" + gain + " from stocks.");
		System.out.println("Payed $" + comGain + " in commissions.");
		System.out.println("Joe lost $" + total + " in total.");
	
	
	
	}

}