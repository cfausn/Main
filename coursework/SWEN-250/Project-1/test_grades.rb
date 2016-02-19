require_relative 'grades_util'
require 'test/unit'

# TetsGrades
#
# Unit test suite for testing grades_util.rb support methods:
#	compute_grade()
#	get_CSV_line()
#	numeric_to_letter()
#	sum_weights()

class TestGrades < Test::Unit::TestCase
   
  # Tests get_CSV_line to insure the entered input line
  # is correctly be parsed to an array of string words
  #
  def test_header_line
	headers = get_CSV_line("Name,ID,Grade")		  # pass in an input string 
	assert_equal ["Name","ID","Grade"], headers   # return an array of header words
  end
  
  ####  YOUR ADDITIONAL UNIT TESTS START HERE  ####
  
# Test with an empty array
  def test_CSV_line_empty
	assert_equal [],  get_CSV_line(",,,")
	
  end

# Test with an example value
  def test_CSV_line_valueG
	headerG = get_CSV_line("George,4,95")
	assert_equal ["George", "4", "95"], headerG, "headerG isn't equal to the return!"

  end

# Test with spaces
  def test_CSV_line_value0
	headerEmpty = get_CSV_line(" , , ,")
	assert_equal [" ", " ", " "], headerEmpty, "headerEmpty should be an array of empty strings"
  end

# Test for invalid input (no commas)
  def test_CSV_line_invalidInput
	assert_raise ArgumentError do
	    get_CSV_line(" ")
	end
  end

# Test for invalid input (wrong type)

  def test_CSV_line_wrongType
	assert_raise TypeError do
	    get_CSV_line(1.2)
	end
  end


########## numeric_to_letter testing ##########

# Test working value (for A)
  def test_numeric_to_letter_A
	assert_equal "A", numeric_to_letter(95), "95 should be an A"
  end

# Test working value (for B)
  def test_numeric_to_letter_B
	assert_equal "B", numeric_to_letter(89), "89 should be a B"
  end

# Test for an F 
  def test_numeric_to_letter_F
	assert_equal "F", numeric_to_letter(32), "32 should be a F"
  end

# Test negative integers (will work)
  def test_numeric_to_letter_negative
	assert_equal "F", numeric_to_letter(-6), "-6 should be a F"
  end

# Test for invalid input (Over 100)
  def test_numeric_to_letter_over
	assert_raise ArgumentError do
	    numeric_to_letter(115)
	end
  end

# Test for invalid input (not an Integer)
  def test_numeric_to_letter_wrongType
	assert_raise TypeError do
	    numeric_to_letter("Letter")
	end
  end

########## sum_weights testing ###########

# Test working values
  def test_sum_weights_valid
	assert_equal 27,sum_weights(["5","8","7","4","3"]), "given values should equal 27!"
  end

# Test working values with empty element
  def test_sum_weights_someEmpty
	assert_equal 50, sum_weights(["10","20","20","",""]), "given values should equal 50!"
  end

# Test with an array of empty strings
  def test_sum_weights_allEmpty
	assert_equal 0, sum_weights(["","","","",""]), "given values should equal 0!"
  end


########## compute_grade testing ##########

# Test working values
  def test_compute_valid
	validTest = compute_grade(["","","50","30","20"],["Drew","Wold",100,100,100])
	assert_equal 100.0, validTest, "Given values should equal 100.0"
  end

# Test values with character grades "like A+"
  def test_compute_validChar
	validTestChar = compute_grade(["","","25","35","40"], ["Derrick","Amie","A+","C-","B+"])
	assert_equal 84.9, validTestChar, "Given values should equal 84.9"
  end

# Test empty values (for all)
  def test_compute_empty
	zeroTest = compute_grade(["","","","",""], ["","","","",""])
	assert_equal 0.0, zeroTest, "Empty passed, should return 0.0"
  end
end
