//RetailItemCall

public class RetailItemCall
{
	public static void main(String[] args)
	{
		String des = "";
		int uni = 0;
		double pr = 0.0;

		
		RetailItem retail1 = new RetailItem();
		//write info for retail1
		retail1.setDescription("Jacket");
		retail1.setUnitsOnHand(12);
		retail1.setPrice(59.95);
		
		System.out.println(retail1.getDescription()+ ", " + retail1.getUnitsOnHand() + 
		" $" + retail1.getPrice());
		
		//write info for retail 2
		RetailItem retail2 = new RetailItem("Designer Jeans", 40, 34.95);		
		System.out.println(retail2.getDescription()+ ", " + retail2.getUnitsOnHand() + 
		" $" + retail2.getPrice());

		
		RetailItem retail3 = new RetailItem();
		//write info for retail 3
		retail3.setDescription("Shirt");
		retail3.setUnitsOnHand(20);
		retail3.setPrice(24.95);
		
		System.out.println(retail3.getDescription()+ ", " + retail3.getUnitsOnHand() + 
		" $" + retail3.getPrice());

	}
}