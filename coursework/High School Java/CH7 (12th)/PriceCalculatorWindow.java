//Retail Price Calculator Class

import javax.swing.*;
import java.awt.event.*; 
import java.text.DecimalFormat; //needed for DecimalFormat
import java.awt.*;

public class PriceCalculatorWindow extends JFrame
{
	private JPanel panel;
	private JLabel itemPrice;
	private JLabel markup;
	private JTextField costOfItem;
	private JTextField markupPercent;
	private JButton calcButton;
	
	DecimalFormat formatter = new DecimalFormat("##.##");
		
	//constructor
	public PriceCalculatorWindow()
	{
		//set title
		setTitle("Price Calculator");
		
		setSize(305,125);
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		setLayout(new FlowLayout(FlowLayout.CENTER));
		
		//build panel
		buildPanel();
		
		//add panel to frame
		add(itemPrice);
		add(costOfItem);
		add(markup);
		add(markupPercent);
		add(calcButton);
		
		setVisible(true);
		
	}
	
	private void buildPanel()
	{
				
		//setup lab
		itemPrice = new JLabel("Enter Item Price: ");
		markup = new JLabel("Enter Markup Percent: ");
		
		costOfItem = new JTextField(10);
		markupPercent = new JTextField(10);
		
		//create button
		calcButton = new JButton("Calculate");
		
		calcButton.addActionListener(new CalcButtonListener());
		
		panel = new JPanel();
		
		panel.add(itemPrice);
		panel.add(markup);
		panel.add(costOfItem);
		panel.add(markupPercent);
		panel.add(calcButton);
	}
	
	//action listener
	private class CalcButtonListener implements ActionListener
	{
		//actionperformed executes when user clicks calc
		public void actionPerformed(ActionEvent e)
		{
			String input;
			String input2;
			double result;
			
			input = costOfItem.getText();
			input2 = markupPercent.getText();
			
			double price = Double.parseDouble(input);
			double percent = Double.parseDouble(input2);
			
			percent *= .01;
			
			result = (percent * price) + price;
			
			JOptionPane.showMessageDialog(null, "Retail price is $" +formatter.format(result)); 
		}
	}
}