require_relative 'grades_util'

# grades.rb Ruby Script
#
# Read the first row (column names) and second row (grade weights).
# If the weights don't sum up to 100, print an error message and exit.
# Otherwise print the column headers with their weights (empty weights simply don't print)
#
# For each student line, print the header and column for each field in the line.
# The field could be identifying information (if the weight is blank) or numeric (if the
# weight is non-negative). Grades can be numeric or letter (with optional +/-)
# Also prints final weighted numeric grade and letter grade.
#
# At end, prints a summary showing the number students for each letter grade and
# the class GPA.


# Create the hash for counting the number of occurrences of each letter grade.

lettercount = Hash.new(0)   # default count is 0.

# Use get_CSV_line() to get the header and weight lines.
# Each line should be "chomped" to eliminate the end of line character(s).
# Create arrays for the headers and weights by splitting on commas.

### YOUR CODE HERE ###
lines = []
count = 0
header = []
weights = []

$stdin.each do |line|
  if count == 0
    header = get_CSV_line(line)
  elsif count == 1
    weights = get_CSV_line(line)
  else
    lines.push(line)
  end
  count += 1
end

count = 0
# For each header, print the header and, if present, its weight.

### YOUR CODE HERE ###
puts "Summary information for grades file"
puts ""
#print header
for line in header
  if not weights[count] == ""
    puts line + " " + weights[count] + "%"
  else
    puts line
  end
  count += 1
end


#Use sum_weights() to check if the weights do not sum to 100, output the error message:
# "Weights add up to #{sum}, not 100" - where sum is the sum of input weights

### YOUR CODE HERE ###
sum = sum_weights(weights)

if sum != 100
  puts "Weights add up to #{sum}, not 100"
end

# Get each of the remaining lines, representing grade information for an individual student.
# Print the header for each column and whatever is in that column on the student grade line.
# Compute contribution of each weighted field to the overall grade using compute_grade(),
# remember to skip fields that do not have weights associated with them.
# Convert the numeric grade to a letter grade using numeric_to_letter().
# Output the final numeric and letter grade for that student and update the 
# lettercount hash that is keeping track of the number of occurrences of each letter grade
# for the class.

for line in lines
  puts ""
  line = line.split(",")
  puts header[0] + ": " + line[0]
  puts header[1] + ": " + line[1]
  puts header[2] + ": " + line[2]
  puts header[3] + ": " + line[3]
  puts header[4] + ": " + line[4]
  finalGrade = compute_grade(weights,line).to_i
  lettercount[numeric_to_letter(finalGrade)] += 1
  puts "Final Numeric Grade = " + finalGrade.to_s + " Letter = " + numeric_to_letter(finalGrade).to_s
  
     
  ### YOUR CODE HERE ###
 

end

# Now print the summary information - the number of students at each letter grade level
# and the class GPA using print_summary(). 
  puts ""
  print_summary(lettercount)
  ### YOUR CODE HERE ###
