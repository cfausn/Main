//RetailItem Class

public class RetailItem
{
	private String description;
	private int unitsOnHand;
	private double price;
	
	/**
		Default Constructor
	*/
	public RetailItem()
	{
		description = "";
		unitsOnHand = 0;
		price = 0.0;
	}
	/**
		Constructor
		@param des is description
		@param units is units on hand
		@param pri is price
	*/
	public RetailItem(String des, int units, double pri)
	{
		description = des;
		unitsOnHand = units;
		price = pri;
	}
	/**
		setDescription sets the description
		@param des is description
	*/
	
	public void setDescription(String des)
	{
		description = des;
	}
	
	/**
		setUnitsOnHand units on hand
		@param units is the units on hand
	*/
	
	public void setUnitsOnHand(int units)
	{
		unitsOnHand = units;
	}
	
	/**
		setPrice sets the price
		@param pri The price
	*/
	
	public void setPrice(double pri)
	{
		price = pri;
	}
	
	/**
		getDescription returns description
		@return the description
	*/
	
	public String getDescription()
	{
		return description;
	}
	
	/**
		getPrice returns the price
		@return the price
	*/
	
	public double getPrice()
	{
		return price;
	}
	
	/** 
		getUnitsOnHand returns the units on hand
		@return the units on hand
	*/
	
	public int getUnitsOnHand()
	{
		return unitsOnHand;
	}
}