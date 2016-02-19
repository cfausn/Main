import java.io.*;
public class Test
{
	public static void main(String[] args) throws IOException
	{
		
		WineBotWindow wine = new WineBotWindow();
		
		PrintWriter outputFile = new PrintWriter("waitTime.txt");
		outputFile.println(wine.returnTheWaitTime());
		outputFile.close();
	}
}