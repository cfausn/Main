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
