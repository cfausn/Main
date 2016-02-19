import java.awt.Robot;
import java.util.Scanner;
import java.awt.event.InputEvent;
import java.io.*;
import java.awt.*;

public class MouseMovement
{
	public static void main(String[] args) throws Exception 
 	{
		//variables
		int waitTime = 0;
		
		//create scanner
		Scanner keyboard = new Scanner(System.in);		
		Robot robot = new Robot();		
		
		System.out.println("Enter wait time in milliseconds");
		waitTime = keyboard.nextInt();
		System.out.println("Open runescape within 5 secounds");
		robot.delay(5000);
				
		for(int sent = 0; sent !=26; sent++)
		{
			getTelegrab();
			getWine();
			robot.delay(waitTime);
			robot.mousePress(InputEvent.BUTTON1_MASK);
     		robot.mouseRelease(InputEvent.BUTTON1_MASK);
			writeLocation();
			robot.delay(0500);
		}
 
	}
	
	public static void getTelegrab() throws Exception
	{
		Robot robotTele = new Robot();	
			
		//variables
		int teleX = 0;
		int teleY = 0;
		
		
		File file = new File("1Telegrab.txt");
		Scanner inputFile = new Scanner(file);
		
		teleX = inputFile.nextInt();
		teleY = inputFile.nextInt();
		inputFile.close();

		robotTele.mouseMove(teleX, teleY);
		
		robotTele.delay(800);
		// LEFT CLICK
		robotTele.mousePress(InputEvent.BUTTON1_MASK);
      robotTele.mouseRelease(InputEvent.BUTTON1_MASK);
		
			
	}
	public static void writeLocation() throws IOException
	{
		Point location = MouseInfo.getPointerInfo().getLocation();
		
		double xx = 0.0;
		double yy = 0.0;
		int x = 0;
		int y = 0;
		
		xx = location.getX();
		yy = location.getY();
		x = (int)xx;
		y = (int)yy;
		PrintWriter outputFile = new PrintWriter("2Wine.txt");
		outputFile.println(x);
		outputFile.println(y);
		outputFile.close();

	}
	public static void getWine() throws Exception
	{
		Robot robotWine = new Robot();	
			
		//variables
		int wineX = 0;
		int wineY = 0;
				
		File file = new File("2Wine.txt");
		Scanner inputFile = new Scanner(file);
		
		wineX = inputFile.nextInt();
		wineY = inputFile.nextInt();
		inputFile.close();

		robotWine.mouseMove(wineX, wineY);
	}
	
}