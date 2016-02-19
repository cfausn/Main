require_relative 'stocks_util'

# Stocks Calculator Main Driver

# Using the methods from stocks_util, for each line of CSV input:
#	- parse the input line into appropriate fields
# - based on elements provided perform the corresponding computation 
# - output the result in the specified format
# ASSUME: No empty lines will be entered.
#
# You may want to consider using the following variable names:
$stdin.each do |line|
	elements = parse_line( line ) 

	next if elements == []  # skip processing if receiving empty line

    # Consider having variables to receive the following:
    # has_enough_funds  #boolean to receive results of verify_exchange()
    # market_value_1 	#float to store first pair market value
    # market_value_2 	#float to store second pair market value
    #
    # Remember to check the array before deciding what action to take.

	#ADD YOUR CODE BELOW (Did you already run tests to make sure util is working?)
	#BEGIN_STUDENT
	if elements.length == 2
		puts elements[0] + " x " + elements[1] + " = " + market_value(elements[0], elements[1].to_f).to_s + " USD"
	elsif elements.length == 3
		puts elements[0] + " x " + elements[1] + " => " + elements[2] + " x "+ compute_exchange(elements[0], elements[1].to_f, elements[2]).to_s
	elsif elements.length == 4
		has_enough_funds = verify_exchange(elements[0], elements[1].to_f, elements[2], elements[3].to_f)
		market_value_1 = market_value(elements[0], elements[1].to_f)
		market_value_2 = market_value(elements[2], elements[3].to_f)
		if has_enough_funds
			puts elements[2] + " x " + elements[3] + " => SUCCESSFUL TRADE. REMAINING FUNDS = " + (market_value_1 + market_value_2).to_s
		else
			puts elements[0] + " x " + elements[1] + " => UNSUCCESSFUL TRADE. NEEDED FUNDS = " + (-1 * (market_value_1 - market_value_2)).to_s

		end
	end

	#END_STUDENT
end

