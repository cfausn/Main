import java.awt.*;
import java.io.*;
import java.util.Scanner;

public class MouseInfoDemo
{
    public static void main(String[] args) throws IOException
	 {
      
		int dec = 0;
		int xInt = 0;
		int yInt = 0;
		double x = 0.0;
		double y = 0.0;
		
		//create scanner
		Scanner keyboard = new Scanner(System.in);
	
		System.out.println("******* GET MOUSE POSITION *******");
		System.out.println("Press 1 for Telegrab location");
		System.out.println("Press 2 for Wine of Zamorak location");
		System.out.println("Press 3 for bag location");
		System.out.println("Press 4 for magic book location");
		System.out.println("Press 5 for Falador Tele location");
		System.out.println("Press 6 to exit");
		dec = keyboard.nextInt();

		
		while(dec != 6)
		{
			//create mouseGet
			Point location = MouseInfo.getPointerInfo().getLocation();

			if(dec == 1)
			{
				x = location.getX();
				y = location.getY();
				xInt = (int)x;
				yInt = (int)y;
				PrintWriter outputFile = new PrintWriter("1Telegrab.txt");
				outputFile.println(xInt);
				outputFile.println(yInt);
				outputFile.close();
			}
			else if(dec == 2)
			{
				x = location.getX();
				y = location.getY();
				xInt = (int)x;
				yInt = (int)y;
				PrintWriter outputFile = new PrintWriter("2Wine.txt");
				outputFile.println(xInt);
				outputFile.println(yInt);
				outputFile.close();
			}
			else if(dec == 3)
			{
				x = location.getX();
				y = location.getY();
				xInt = (int)x;
				yInt = (int)y;
				PrintWriter outputFile = new PrintWriter("3Bag.txt");
				outputFile.println(xInt);
				outputFile.println(yInt);
				outputFile.close();
			}
			else if(dec == 4)
			{
				x = location.getX();
				y = location.getY();
				xInt = (int)x;
				yInt = (int)y;				
				PrintWriter outputFile = new PrintWriter("4Magic.txt");
				outputFile.println(xInt);
				outputFile.println(yInt);
				outputFile.close();
			}
			else if(dec == 5)
			{
				x = location.getX();
				y = location.getY();
				xInt = (int)x;
				yInt = (int)y;
				PrintWriter outputFile = new PrintWriter("5Falador.txt");
				outputFile.println(xInt);
				outputFile.println(yInt);
				outputFile.close();
			}
							
			System.out.println("Enter another value");
			dec = keyboard.nextInt();	

		}
    }
}