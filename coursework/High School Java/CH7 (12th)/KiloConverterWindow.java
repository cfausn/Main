import javax.swing.*;
import java.awt.event.*; 

/** 
	KiloConverterWindow
	
*/

public class KiloConverterWindow extends JFrame
{
	private JPanel panel;
	private JLabel messageLabel;
	private JTextField kiloTextField;
	private JButton calcButton;
	private final int WINDOW_WIDTH = 310;
	private final int WINDOW_HEIGHT = 100;
	
	//Constructor
	
	public KiloConverterWindow()
	{
		//set window title
		setTitle("Kilometer Converter");
		
		//set size of window
		setSize(WINDOW_WIDTH, WINDOW_HEIGHT);
		
		//specifiy what happens when close button is clicked.
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		//build panel
		buildPanel();
		
		//add panel to frame
		add(panel);
		
		//display
		setVisible(true);
	}
	
	//buildpanel adds a label text field and button
	
	private void buildPanel()
	{
		//create label to display instructions
		messageLabel = new JLabel("Enter a distance " + "in kilometers");
		
		//create text field 10 chars wide
		kiloTextField = new JTextField(10);
		
		//create button with caption "calculate"
		calcButton = new JButton("Calculate");
		
		//add an action listener
		calcButton.addActionListener(new CalcButtonListener());
		
		//create JPanel object and let field reference it
		panel = new JPanel();
		
		//add the label text field and button componets to panel
		panel.add(messageLabel);
		panel.add(kiloTextField);
		panel.add(calcButton);
	}
	
	//action listener
	private class CalcButtonListener implements ActionListener
	{
		//actionPerformed method executes when the user clicks on the calculate button
		//@param e The Event object
		
		public void actionPerformed(ActionEvent e)
		{
			String input;
			double miles;
			
			//get the text entered
			input = kiloTextField.getText();
			
			//convert to miles
			miles = Double.parseDouble(input) * 0.6214;
			
			//display result
			JOptionPane.showMessageDialog(null, input +
				" kilometers is " +miles + " miles.");
		}
	}
		
	
}