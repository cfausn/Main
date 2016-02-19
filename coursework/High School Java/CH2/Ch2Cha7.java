//Ch2Cha7.java

public class Ch2Cha7
{
	public static void main(String args[])
	{
		//variables
		final double TRACT = 389767;
		final double ACRE = 43560;
		double acres = 0.0;
		
		//assign
		acres = TRACT / ACRE;
		
		//print
		System.out.println("There are " + acres + " acres.");
	}
}