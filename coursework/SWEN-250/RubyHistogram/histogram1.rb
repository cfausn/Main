$stdin.each do |line|
   puts line.downcase.chomp().gsub(/[^a-zA-Z\s]/, '').sub(/^\s+/, '')
#< is used for input, > is used for output (in bash)
end
