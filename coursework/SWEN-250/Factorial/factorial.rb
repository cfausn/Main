# factorial(n) is defined as n*n-1*n-2..1 for n > 0
# factorial(n) is 1 for n=0
# Let's raise an exception if factorial is negative
# Let's raise an exception if factorial is anything but an integer

def factorial(n)
  # Write the factorial code here per the activity
  if not (n.is_a? Integer)
    # If the input isn't a integer, raise TypeError
    raise TypeError, "Must enter an Integer"
  elsif n < 0
    # If the input is less than 0, raise ArgumentError
    raise ArgumentError,  "Number cannot be negative"
  end
   
  # Program made it through the error-checking, now calculate factorial
  sum = 1
  if n == 0
    return sum
  else
    while n != 0 do
      sum *= n
      n -= 1 
    end
  end

  # return calculated factorial
  return sum
end

