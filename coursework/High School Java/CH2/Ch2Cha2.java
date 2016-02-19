//Ch2Cha2.java

public class Ch2Cha2
{
	public static void main(String[] args)
	{
		//variables
		String firstName, middleName, lastName;
		char firstInitial, middleInitial, lastInitial;
		
		//storing
		firstName = "Colin";
		middleName = "Joseph";
		lastName = "Fausnaught";
		firstInitial = firstName.charAt(0);
		middleInitial = middleName.charAt(0);
		lastInitial = lastName.charAt(0);
		
		//printing
		System.out.println("First name: " + firstName + "\nMiddle name: "
		+ middleName + "\nLast name: " + lastName + "\nFirst initial: "
		+ firstInitial + "\nMiddle initial: " + middleInitial + "\nLast initial: "
		+ lastInitial );
		
		}
	}