//Ch4Cha5

import javax.swing.JOptionPane; //needed for JOptionPane

public class Ch4Cha5
{
	public static void main(String args[])
	{
		//variables
		String tempString, sentence;
		char letter, tempLetter;
		int num = 0;


		//Prompt
		sentence = JOptionPane.showInputDialog("Enter a sentence: ");
		tempString = JOptionPane.showInputDialog("Enter a letter: ");
		
		sentence = sentence.toUpperCase();
		tempString = tempString.toUpperCase();

		letter = tempString.charAt(0);
	
		//loop
		
		for(int character = 0; character < sentence.length(); character++)
		{
			if(letter == sentence.charAt(character))
			{
				num ++;
			}

		}
		
		//output
		JOptionPane.showMessageDialog(null, letter +" shows up " + num + " times.");
		
		System.exit(0);
	}
}
		