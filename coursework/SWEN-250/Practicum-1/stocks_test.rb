require_relative 'stocks_util' 
require 'test/unit'          

class StocksTest < Test::Unit::TestCase 

	def test_parse_line
		assert_equal %w{GOOG 10}, parse_line("GOOG,10")
		assert_equal %w{GOOG 10 FB}, parse_line("GOOG,10,FB")
	end

	# assert_in_delta() is used to compare two floating point
	# values within a tolerance, or delta to account for potential
	# rounding errors when performing floating point computations.

	def test_market_value
		assert_in_delta 5389.5, market_value( 'GOOG', 10  ), 0.01
	end

	def test_compute_exchange
		assert_in_delta 67.46, compute_exchange( 'GOOG', 10, 'FB' ), 0.01
	end

	#ADD YOUR TESTS BELOW
	#BEGIN_STUDENT

	def test_parse_line_commas_only
		assert_equal [], parse_line(",,,"), "Should equal []"
	end

	def test_verify_exchange_false
		assert_equal false, verify_exchange('GOOG',10,'FB', 1000)
	end

	def test_verify_exchange_true
		assert_equal true, verify_exchange('FB', 1000, 'GOOG', 10)
	end

	def test_compute_exchange_invalid
		assert_in_delta 0.0, compute_exchange('GOOG', -1, 'FB'), 0.0
	end

	def test_compute_exchange_invalid_word
		assert_in_delta 0.0, compute_exchange('WRONG', 10, 'FB'), 0.0
	end

	def test_market_value_invalid
		assert_in_delta 0.0, market_value('WRONG', 10), 0.0
	end




	#END_STUDENT
end
