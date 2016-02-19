# Stock Exchange Calculator Utility Methods

# Hash of stock values in USD (US Dollars) to be used in calculations
STOCKS = {
	"AAPL" => 129.49,
	"DIS" => 100.00,
	"FB" => 79.89,
	"GOOG" => 538.95,
	"SBUX" => 93.51,
	"TWTR" => 50.00
}

# Given a stock ticker symbol and quantity of shares,
# return the equivalent USD as a floating point value using the STOCKS Hash.
# returns 0.0 if stock ticker symbol does not exist

def market_value( stock_ticker_symbol, shares )
	result = 0.0

	#BEGIN_STUDENT
	if STOCKS.include? stock_ticker_symbol
	  result = STOCKS[stock_ticker_symbol] * shares
	  result.round(2)
	end

	#END_STUDENT

	return result
end

# Based on the market value of the given first stock ticker symbol and shares,
# return the boolean value indicating whether exchange is possible
# Note: You are trying to verify that you can buy the second pair of shares
# 
# If stock ticker unknown or number of shares <= 0 result is false
#
def verify_exchange( stock_ticker_symbol_1, shares_1, stock_ticker_symbol_2, shares_2 )
	result = false

	#BEGIN_STUDENT
	if (STOCKS.include? stock_ticker_symbol_1 and STOCKS.include? stock_ticker_symbol_2)
	  if not (shares_1 <= 0 or shares_2 <= 0)
	    result = (market_value(stock_ticker_symbol_1, shares_1) >= market_value(stock_ticker_symbol_2, shares_2))
	      
	end
	end

	#END_STUDENT

	return result
end

# Based on the given first stock ticker symbol and its number of shares,
# computes the market value and then the calculates the equivalent number of 
# shares for the second stock symbol returned as floating point result.
#
# If stock ticker unknown or provided number of shares <= 0 result is 0.0 
#
def compute_exchange( stock_ticker_symbol_1, shares, stock_ticker_symbol_2 )
	result = 0.0

	#BEGIN_STUDENT
	if (STOCKS.include? stock_ticker_symbol_1 and STOCKS.include? stock_ticker_symbol_2)
	  if not shares <= 0
	    result = market_value(stock_ticker_symbol_1, shares) / STOCKS[stock_ticker_symbol_2]
	    result.round(2)
	  end
	end

	#END_STUDENT

	return result
end

# Given an input string in CSV format, return an array
# of values.
def parse_line( line )
	line.chomp!
	values = []
	#BEGIN_STUDENT
	values = line.split(',')
	return values


	#END_STUDENT
end

