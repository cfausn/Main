"""
    olympics_simpl.py
    Colin Fausnaught
    9/15/14, revised 9/16/14

    Opens a file and reads the contents of the file, then prints out requested information.
    Uses iteration in both instances in order to accomplish these tasks, along with the
    readline() function and other file functions.
"""

def countWinners(year):
    """
         countWinners will take a year input and count the number of gold medals in that specific year.
         It uses a while loop and the readline() function to accomplish this, along with the open() command
         in order to open the file.

         Pre-Conditions: User has entered the year to count
                         The file has not been opened

         Post-Conditions: The number of gold medals has been counted and returned
                          The file has been completely read through
                          The file has been closed

    """
    f = open("athletes.txt", encoding='utf-8')
    medalACC = 0
    
    while True:
        
        st1 = f.readline()
        
        if st1.strip() == year:
            
            medal = f.readline()
            
            if medal.strip() == '1':
                medalACC += 1
            

        if not st1:
            break
    f.close()           
    return medalACC


def countByName(last, first):
    """
         countByName will take two parameters, last, and first, and use them to search the file
         for that person's number of gold, silver, and bronze medals. It will open the file to
         do this and use the readline() function to accomplish the goal.

         Pre-Conditions: User has entered the last and first values
                         User has recieved the output from countWinners
                         The file is closed

         Post-Conditions: The number of medals has been counted
                          The file has been read through
                          The number of each medal has been printed
                          The file has been closed
                          
    """
    f = open("athletes.txt", encoding='utf-8')
    goldACC = 0
    silverACC = 0
    bronzeACC = 0

    while True:
        st1 = f.readline()
        st1 = st1.upper()

        
        if st1.strip() == last.upper():
            st2 = f.readline()
            st2 = st2.strip()
            st2 = st2.upper()

            if st2 == first.upper():
                f.readline()
                medal = f.readline()

                if medal.strip() == '1':
                    goldACC += 1
                if medal.strip() == '2':
                    silverACC += 1
                if medal.strip() == '3':
                    bronzeACC += 1
        
        if not st1:
            print( first[0].upper() + first[1:].lower() + " " + last[0].upper() + last[1:].lower() +
                   " had " + str(goldACC) + " gold medals, " + str(silverACC)+" silver medals, and " + str(bronzeACC) +
                   " bronze medals.")
            f.close()
            break


def main():
    """
         This main function will recieve the user's input and pass that information to the
         functions countWinners() and countByName(). It also prints out the information after
         countWinners() has been called.
    """
    year = str(input("Enter year to count its winners: "))
    gold = countWinners(year)
    print("In the year " + year + " there were " + str(gold) +
          " gold medalists in total.")
    print("Let’s look up the total medals won by an athlete (1896-2008)!")

    last = str(input("Last Name: "))
    first = str(input("First Name: "))

    countByName(last,first)

#call main()
main()
