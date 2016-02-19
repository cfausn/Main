require 'pp'
bag = Hash.new(0)
$stdin.each do |line|
   line = line.downcase.chomp().gsub(/[^a-zA-Z\s]/, '').sub(/^\s+/, '')
   theArray = line.split(/ +/)
   theArray.each do |word|
       bag[word] = bag[word] +  1
   end
end

bag.each do |key, value|
    puts "Key #{key}"
    puts "value #{value}"
end
   
newArray = bag.select{|k,v| v > 1}

newArray.each do |value|
    puts "Word #{value[0]} count #{value[1]}"
end

sortedArray = newArray.sort{|k,v| v[1] <=> k[1]} 

tempArray = Array.new
prevNum = 0
finalSorted = Array.new
acc = 0

sortedArray.each do |sortThis|    
    acc += 1
    if prevNum == 0
	tempArray.push(sortThis)
	prevNum = sortThis[1]
    elsif sortThis[1] == prevNum && acc != sortedArray.count
	tempArray.push(sortThis)
	prevNum = sortThis[1]

    else
        if tempArray.count != 1
  	    tempArray.sort_by!{|m| m[0].downcase}
	end
	tempArray.each do |addThis|
	    finalSorted.push(addThis)
	end
	tempArray = Array.new
	tempArray.push(sortThis)
	prevNum = sortThis[1]
    end
end

tempArray = Array.new

finalSorted.each do |name|
    tempArray.push(name[0])
end

longest = tempArray.inject do |memo,word|
    memo.length > word.length ? memo : word
end

longestI = longest.length

finalSorted.each do | apair |
  printf "%-*.*s ", longestI, longestI, apair[0]
  puts "*" * apair[1]
end
