# grades_util.rb Ruby Script
#
# Support methods used by grades.rb for reading CSV gradebook files
# and producing reports
#

##### TRANSLATION HASH FOR LETTER GRADES TO NUMERIC #####

LETTER_TO_NUMERIC = {
  "A+" => 98, "A" => 95, "A-" => 92,
  "B+" => 88, "B" => 85, "B-" => 82,
  "C+" => 78, "C" => 75, "C-" => 72,
  "D+" => 68, "D" => 65, "D-" => 62,
  "F+" => 55, "F" => 40, "F-" => 25,
}

##### TRANSLATION OF LETTER GRADES TO QUALITY POINTS #####

QUALITY_POINTS = { 'A' => 4, 'B' => 3, 'C' => 2, 'D' => 1, 'F' => 0 }


# sum_weights(weights)
#	weights = array of weights strings (2nd line of input)
# returns integer value equal to the sum of all weights
#
# Method to sum up the weights in the weight line. 
# Skips over empty fields.

def sum_weights(weights)
  
  #simply sums all integer values passed to it, if an empty string is 
  #in the array then it skips it. 
  sum = 0
  weights.each do |num|
    if not (sum == "")
	sum += num.to_i
    end
  end

  return sum
end

# numeric_to_letter(numeric)
#	numeric =  integer value to convert to a whole letter grade
# return letter grade as a string
#
# Method to convert a raw numeric grade to a whole letter A - F.
# A (90-100), B (80-89), C (70-79), D (60-69), F (<60)


def numeric_to_letter(numeric)
  #Basic if/elsif statements to raise errors and return values

  #NOTE: This supports negative integers! -2 is an "F" to this program
  if not (numeric.is_a?(Integer))
	raise TypeError, "Value must be an Integer!"  
  elsif numeric <= 100 and numeric >= 90
	return "A"
  elsif numeric < 90 and numeric >= 80
	return "B"
  elsif numeric < 80 and numeric >= 70
	return "C"
  elsif numeric < 70 and numeric >= 60
	return "D"
  elsif numeric < 60
	return "F"
  else
	#just in case the value is over 100
	raise ArgumentError, "Value not below 100!"
  end

end
  
  
# get_CSV_line( line)
#	line = string of one line of input
# returns array of strings representing fields in that line
#
# Get a CSV line for the header line, weight lines or field line
# Each line should be "chomped" to eliminate the end of line character(s).
# Create arrays for the headers, weights and fields by splitting on commas.

def get_CSV_line( line )  

   if not (line.is_a?(String))
	raise TypeError, "Line must be a string!"
   elsif not (line.include? ",")
	raise ArgumentError, "Must include commas for valid input!"
   end

   line = line.chomp()
   line = line.split(",")
   
   return line
  
end

# compute_grade( weight, field )
# 	weight = string value representing weight of the graded item
#   field = string value representing value of graded item in numeric or letter grade format
# returns floating point grade value
#
# Compute a numeric grade given the weight of the grade and either a numeric 
# score or letter score in the field. 

def compute_grade( weight, field)
   
  #field / 100  * weight gets the grade, then add them all together

  counter = 0
  sum = 0.0
  
  weight.each do |currentWeight|
	
        if LETTER_TO_NUMERIC.has_key?(field[counter].upcase) 
	    sum += ((LETTER_TO_NUMERIC[field[counter].upcase].to_f / 100 ) * currentWeight.to_f)
	else
	    #a name to_f will be 0.0, so no need to error check! :)
	    sum += ((field[counter].to_f / 100) * currentWeight.to_f)
	    
	end
	counter += 1
  end
  return sum
 
    
end

# print_summary(lettercount)  - !!! DO NOT MODIFY !!!
#	lettercount = hash of letter grades => count of number of students
#
# Prints summary information. First the count of the number of students for each
# letter grade and then the class GPA.

def print_summary(lettercount)
  qualty_points = 0
  grade_count = 0

  ['A', 'B', 'C', 'D', 'F'].each do | letter |
    puts "#{letter} = #{lettercount[letter]}"
    qualty_points += QUALITY_POINTS[letter] * lettercount[letter]
    grade_count += lettercount[letter]
  end

  printf "Class GPA = %1.2f", qualty_points.to_f / grade_count.to_f
  puts
end

