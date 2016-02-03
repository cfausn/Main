"""
    perk.py
    Colin Fausnaught
    9/29/14

    perk.py will take a filename, open the file, read the integer list in the file and then sort that
    list from least to greatest.
"""
def Perksort(nums):
    """
         Perksort() sorts the list's values from least to greatest. It uses nested while loops to accomplish this.

         Pre-Conditions: a list has been passed to Perksort()

         Post-Conditions: The list has been sorted
                          The sorted list has been returned
                          
    """
    x = 1
    while x < len(nums):
        y = 1
        while y < len(nums):
            if nums[y-1] > nums[y]:
                tempNum = nums[y-1]
                nums[y-1] = nums[y]
                nums[y] = tempNum
            y+=1
        x+=1
    return nums

def fileManagement():
    """
         fileManagement() will prompt the user to enter the file name of their stored integer data file. It will
         take each line of the file and store it in a list to be sorted later.

         Pre-Conditions: None

         Post-Conditions: File has been opened
                          Data from file has been stored in numList
                          numList has been returned
    """
    filename = input("Enter File Name: ")
    numList = []
    for line in open(filename):
        numList.append(int(line))
    
    print("Unsorted List: ")
    print(numList)
    input("Press ENTER to continue ")
    return numList

def test_Perksort():
    """
         test_Perksort() is a simple test function used to test Perksort. 
    """
    print("Testing Perksort() with [1,5,2,6,7,10]:", Perksort([1,5,2,6,7,10])," (expect [1,2,5,6,7,10])")
    print("Testing Perksort() with [22,1,6,14,26,19]:", Perksort([22,1,6,14,26,19])," (expect [1,6,14,19,22,26])")
    print("Testing Perksort() with [1,2,3,4,5,6,7,8]:", Perksort([1,2,3,4,5,6,7,8])," (expect [1,2,3,4,5,6,7,8])")
    print("Testing Perksort() with [1]:", Perksort([1])," (expect [1])")
    print("Testing Perksort() with []:", Perksort([])," (expect [])")

    
def main():
    """
         main() will call Perksort() and fileManagement() to get their respective values,
         then print the sorted list.
    """
    nums = Perksort(fileManagement())
    print("Sorted List: ")
    print(nums)
    

#call main()
main()
#test_Perksort()
