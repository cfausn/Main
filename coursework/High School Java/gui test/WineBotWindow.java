import javax.swing.*;
import java.io.*;
import java.awt.event.*; //action listener

/**
	Base class for Wine bot
*/

public class WineBotWindow extends JFrame
{
	private JPanel panel; 				//reference jPanel
	private JLabel messageLabel; 	   //to reference a label
	private JTextField enterWaitTime;//to reference a text field
	private JButton startBot;			//to refernce a button
	private final int WINDOW_WIDTH = 350;
	private final int WINDOW_HEIGHT = 100;
	private int returnWaitTime = 0;
	
	/**
		Constructor
	*/
	
	public WineBotWindow()
	{
		//set the window title
		setTitle("Wine of Zamorak Bot");
		
		//set the size of the window
		setSize(WINDOW_WIDTH, WINDOW_HEIGHT);
		
		//close button
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		//build panel and add it to the frame
		buildPanel();
		
		//add the panel to the frame's content page
		add(panel);
		
		setVisible(true);

	}
	
	//buildPanel adds a label text field and button
	private void buildPanel()
	{
		//create a label to display instructions
		messageLabel = new JLabel("Enter the wait time "+ "in milliseconds");
		
		//create a text field 10 chars wide
		enterWaitTime = new JTextField(10);
		
		//create a button with caption
		startBot = new JButton("Start");
		
		//add an action listener to the button
		startBot.addActionListener(new StartBotListener());
		
		panel = new JPanel();
		
		//add the label, text field and button components to the panel
		panel.add(messageLabel);
		panel.add(enterWaitTime);
		panel.add(startBot);
	}
	
	public class StartBotListener implements ActionListener
	{
		//makes button work
		
		public void actionPerformed(ActionEvent e)
		{
			String input;
			
			input = enterWaitTime.getText();
			
			//parse
			returnWaitTime = Integer.parseInt(input);
			
			JOptionPane.showMessageDialog(null, "Done");
		}	
	}
	
	public int returnTheWaitTime()
	{
		return returnWaitTime;
	}
}

	
	
	