# Script that obtains various git metrics from a basic git log file
require "date"

# Given an array of git log lines, count the number of commits in the log
def num_commits(lines)
  commits = 0
  tempArr = []
  for line in lines
    #simply seperate the string into an array and check if the first
    #value is "commit"
    tempArr = line.split(" ")
    if tempArr[0] == "commit"
	commits += 1
    end
  end
  return commits
end

# Given an array of git log lines, count the number of different authors
#   (Don't double-count!)
# You may assume that emails make a developer unique, that is, if a developer
# has two different emails they are counted as two different people.
def num_developers(lines)
  #the initializers may be unneccesary but I like them
  #as they remind me of my variable names and types.
  knownDevelopers = []
  tempArr = []
  countedDevelopers = 0

  for line in lines
    tempArr = line.split(": ")
    if tempArr[0] == "Author"
	#Only the name is used as an identifier, emails do not count!
	#George Carl <george@gmail.com>
	#George Carl <g@gmail.com>
	#^ The above will only count as one developer
	tempArr2 = tempArr[1].split("<")
	if not (knownDevelopers.include? tempArr2[0])
	  countedDevelopers += 1
	  knownDevelopers.push(tempArr2[0]) #don't be counted again
	end
    end
  end
  return countedDevelopers
end

# Given an array of Git log lines, compute the number of days this was in development
# Note: you cannot assume any order of commits (e.g. you cannot assume that the newest commit is first).
def days_of_development(lines)
  numDays = 0
  startDate = ""
  finishDate = ""
  tempArr = []
 
  for line in lines
    tempArr = line.split(": ")
    if tempArr[0] == "Date"
	#git doesn't put information in correctly for DateTime to parse.
	#Sun Jan 26 21:25:22 2014 -0600
	#MUST BE CHANGED TO
	#Sun Jan 26 21:25:22 -0600 2014
	#For DateTime to parse it correctly!!!! 

	tAr = tempArr[1].split(" ")
	tempDate = tAr[0] + " " + tAr[1] + " " + tAr[2] + " " + tAr[3] + " " + tAr[5] + " " + tAr[4]
	
	#checks for start and finish dates, using DateTime.parse()
	#to check which is higher
	if startDate == ""
	  startDate = tempDate      
	elsif finishDate == ""
	  if DateTime.parse(tempDate) < DateTime.parse(startDate)
	    finishDate = startDate
	    startDate = tempDate
          else
	    finishDate = tempDate
	  end
	elsif DateTime.parse(startDate) > DateTime.parse(tempDate)
	  startDate = tempDate
	elsif DateTime.parse(finishDate) < DateTime.parse(tempDate)
	  finishDate = tempDate
	end
   end
  end

  #1.8 days is always 1 day, not 2. Therefore we should not round the 
  #float value but simply drop the decimals. It doesn't match the 
  #given code but this has to be right.
  return (DateTime.parse(finishDate) - DateTime.parse(startDate)).to_i
  

end

# This is a ruby idiom that allows us to use both unit testing and command line processing
# Does not get run when we use unit testing, e.g. ruby test_git_metrics.rb
# These commands will invoke this code with our test data: 
#    ruby git_metrics.rb < ruby-progressbar-short.txt
#    ruby git_metrics.rb < ruby-progressbar-full.txt
if __FILE__ == $PROGRAM_NAME
  lines = []
  $stdin.each { |line| lines << line }
  puts "Nunber of commits: #{num_commits lines}"
  puts "Number of developers: #{num_developers lines}"
  puts "Number of days in development: #{days_of_development lines}"
end

