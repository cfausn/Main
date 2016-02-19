# Convert to/from phonetic alphabet
# Colin Fausnaught

class Phonetic

  Letters = [
             ['A', 'ALPHA'],
             ['B', 'BRAVO'],
             ['C', 'CHARLIE'],
             ['D', 'DELTA'],
             ['E', 'ECHO'],
             ['F', 'FOXTROT'],
             ['G', 'GOLF'],
             ['H', 'HOTEL'],
             ['I', 'INDIA'],
             ['J', 'JULIET'],
             ['K', 'KILO'],
             ['L', 'LIMA'],
             ['M', 'MIKE'],
             ['N', 'NOVEMBER'],
             ['O', 'OSCAR'],
             ['P', 'PAPA'],
             ['Q', 'QUEBEC'],
             ['R', 'ROMEO'],
             ['S', 'SIERRA'],
             ['T', 'TANGO'],
             ['U', 'UNIFORM'],
             ['V', 'VICTOR'],
             ['W', 'WHISKEY'],
             ['X', 'XRAY'],
             ['Y', 'YANKEE'],
             ['Z', 'ZULU'],
             ]

  # Translate a word to its phonetic alphabet equivalent
  def self.to_phonetic(word)
	phoneticArray = []
	phoneticString = ""
	
	wordString = word.split(//)	
	for char in wordString
	  char = char.upcase 
	  Letters.each do |elm| 
	    
	    if elm[0] == char
	       phoneticArray.push(elm[1])
	    end
	  end
	end
	
		
	for word in phoneticArray
	   if not (phoneticString == "")
	     phoneticString << " " 
	end
	phoneticString << word
	end
	
	return phoneticString
	   
  end

  # Translate a sequence of phonetic alphabet code words 
  # to their alphabetic equivalent
  def self.from_phonetic(str)
	newString = ""
	str.each do |elm|
	  elm = elm.upcase
	  Letters.each do |word|
	    if word[1] == elm
		newString << word[0]
	    end
	  end
	end
	
	return newString
  end

  # If the line starts with A2P, call to_phonetic on the rest of the substring
  # If the line starts with P2A, call from_phonetic on the rest of the substring
  # Otherwise, return nothing.
  def self.translate(line)
	line = line.split(" ")
	if line[0].upcase == "A2P"
	  return to_phonetic(line[1])
	elsif line[0].upcase == "P2A"
	  line.delete_at(0)
	  return from_phonetic(line)
	end
  end

end


# This is ruby idiom that allows us to use both unit testing and command line processing
# This gets run with ruby phonetic.rb
# Does not get run when we use unit testing, e.g. ruby phonetic_test.rb
if __FILE__ == $PROGRAM_NAME
  $stdin.each do |line|
    puts Phonetic.translate(line)
  end
end
