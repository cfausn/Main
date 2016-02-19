//TestScores

public class TestScores
{
	//fields
	private double testScore1;
	private double testScore2;
	private double testScore3;
	private double average;
	
	/**
		Constructor
		@param year The yearmodel
		@param ma The make	
	*/
	
	public TestScores(double test1, double test2, double test3)
	{
		testScore1 = test1;
		testScore2 = test2;
		testScore3 = test3;
	}
	
	/**
		setTest1 first Test score
		@param test1 The first test score
	*/
	
	public void setTest1(double test1)
	{
		testScore1 = test1;
	}
	
	/**
		setTest2 second test score
		@param test2 the second test score
	*/
	
	public void setTest2(double test2)
	{
		testScore2 = test2;
	}
	
	/**
		setTest3 third test score
		@param test3 the third test score
	*/
	
	public void setTest3(double test3)
	{
		testScore3 = test3;
	}
	
	/**
		getTest1 returns testScore1
		@return first test score
	*/
	
	public double getTest1()
	{
		return testScore1;
	}
	
	/**
		getTest2 returns testScore2
		@return second test score
	*/
	
	public double getTest2()
	{
		return testScore2;
	}
	
	/** 
		getTest3 returns testScore3
		@return third test score
	*/
	
	public double getTest3()
	{
		return testScore3;
	}
	
	/**
		average calculates the 
		average
	*/
	
	public double average()
	{
		return average = (testScore1 + testScore2 + testScore3)/3.0;
	}
	
}
	