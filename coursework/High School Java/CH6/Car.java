//Ch6Cha2 class

public class Car
{
	//fields
	private int yearModel;
	private String make;
	private int speed;
	
	/**
		Constructor
		@param year The yearmodel
		@param ma The make	
	*/
	
	public Car(int year, String ma)
	{
		yearModel = year;
		make = ma;
		speed = 0;
	}
	
	/**
		setYearModel sets the year Model
		of the car
		@param year The year model
	*/
	
	public void setYearModel(int year)
	{
		yearModel = year;
	}
	
	/**
		setMake sets the car's make
		@param ma The make
	*/
	
	public void setMake(String ma)
	{
		make = ma;
	}
	
	/**
		setSpeed sets the speed
		@param spe The speed
	*/
	
	public void setSpeed(int spe)
	{
		speed = spe;
	}
	
	/**
		getYearModel returns yearModel
		@return the year model
	*/
	
	public int getYearModel()
	{
		return yearModel;
	}
	
	/**
		getMake returns the make
		@return the make
	*/
	
	public String getMake()
	{
		return make;
	}
	
	/** 
		getSpeed returns the speed
		@return the speed
	*/
	
	public int getSpeed()
	{
		return speed;
	}
	
	/**
		accelerate calculates the 
		acceleration
	*/
	
	public int accelerate(int spe)
	{
		return speed += 5;
	}
	
	/**
		brake calcualtes after
		the braking
	*/
	
	public int brake(int spe)
	{
		return speed -= 5;
	}
}
	