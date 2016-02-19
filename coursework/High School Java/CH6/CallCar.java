//call car Class

public class CallCar
{
	public static void main(String[] args)
	{
		int x = 1;
		int y = 1;
		int year = 2003;
		int speed = 0;
		String make = "Honda";
		
		Car car = new Car(year, make);
		
		while(x <= 5)
		{
			speed = car.accelerate(speed);
			System.out.println("Car is: " +make + " " +year +" Speed is: " +speed);
			x++;
		}
		
		while(y <= 5)
		{
			speed = car.brake(speed);
			System.out.println("Car is: " +make + " " +year +" Speed is: " +speed);
			y++;
		}
	}
}