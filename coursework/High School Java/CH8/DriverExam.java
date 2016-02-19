//DriverExam class

public class DriverExam
{
	//fields
	private char[] answers = {'B', 'D', 'A', 'A', 'C', 
									  'A', 'B', 'A', 'C', 'D', 
									  'B', 'C', 'D', 'A', 'D', 
									  'C', 'C', 'B', 'D', 'A'};
	private char[] stored = new char[20];
	private int correct = 0;
	private int incorrect = 0;
	private int sCounter = 0;
	
	/** Used Default Constructor **/
	
	/**
		store stores whatever answers the user enters into the 
		class for further comparison. Input validation is in the
		calling program.
	*/
	public void store(char ans)
	{
		stored[sCounter] = ans;
		sCounter++;
	}
	
	/**
		grade compares the user's input stored in the class
		with the correct answer stored in the class and then adds
		the incorrect and correct fields based on what the answer is.
	*/
	public void grade()
	{
		for(int index = 0; index < 20; index++)
		{
			if(stored[index] == answers[index])
				correct += 1;
			else if(stored[index] != answers[index])
				incorrect += 1;
			
		}

	}
	
	/**
		totalCorrect returns how many correct answers there were
		as decided in the grade function.
		
		@return the number of correct answers
	*/
	public int totalCorrect()
	{
		return correct;
	}
	
	/**
		totalIncorrect returns how many incorrect answers there were
		as decided in the grade function.
		
		@return the number of incorrect answers
	*/
	public int totalIncorrect()
	{
		return incorrect;
	}
	
	/**
		passed decides whether the user had a passing grade or not.
		
		@return pass is the decision 
	*/
	public boolean passed()
	{
		boolean pass;
		
		if(correct >= 15)
			pass = true;
		else
			pass = false;
		
		return pass;
	}
	
	/**
		questionsMissed uses an array and a sentinal value
		to decide what the number of each question missed was.
	*/
	public void questionsMissed()
	{
		int[] missed = new int[20];
		
		for(int index = 0; index < 20; index++)
		{
			if(stored[index] != answers[index])
			{
				missed[index] = index + 1;
				System.out.println("Question " +missed[index]+ " was wrong.");
			}
		}
	}
	
	
	
}