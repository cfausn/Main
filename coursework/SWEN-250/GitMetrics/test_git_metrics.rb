require_relative 'git_metrics'
require 'test/unit'

class TestGitMetrics < Test::Unit::TestCase

  def test_commit_example
  	assert_equal 2, num_commits(["commit abc", "commit 123"]), "Should have counted two commits"
  end

  def test_dates_with_three_days
  	exp = [ "Date:  Sun Jan 26 21:25:22 2014 -0600", \
  			"Date:  Sun Jan 23 21:25:22 2014 -0600", \
  			"Date:  Sun Jan 25 21:25:22 2014 -0600"]
    assert_equal 3, days_of_development(exp), "Should have been a 3 days difference"
  end

  #Add more tests here
  def test_num_developers_working
	assert_equal 2, num_developers(["Author: Jeff Felchner <accounts+git@thekompanee.com>",\
                                        "Author: Eugene Korbut <me@mvl.ru>"]), "Should be 2 developers"
  end

  def test_dates_with_two_days
	exp = ["Date:  Sat Jan 1 12:20:00 2015 -0000", \
	       "Date:  Sun Jan 2 18:12:12 2015 -0000"]
	assert_equal 1, days_of_development(exp), "Should have a 1 day difference."
  end

  def test_num_commits_five
	exp = ["commit 1", "commit 2", "commit 3", "commit 4", "commit 5"]
	assert_equal 5, num_commits(exp), "Should have 5 commits"
  end

  def test_dates_with_five_days
	exp = ["Date:  Sat Jan 1 12:00:00 2015 +0700",\
	       "Date:  Sat Jan 8 08:12:51 2015 +0700",\
	       "Date:  Mon Jan 3 12:00:00 2015 -0200",\
	       "Date:  Tue Jan 4 10:12:41 2015 -0200",\
	       "Date:  Sat Jan 1 11:00:00 2015 +0700"]
	assert_equal 6, days_of_development(exp), "Should have 6 days of development"
  end

  def test_num_developers_one
	assert_equal 1, num_developers(["Author: George Carl <gcarl@gmail.com"]), "Should be one developer"
  end

  def test_num_commits_one
	assert_equal 1, num_commits(["commit 1"]), "Should have 1 commit"
  end

  def test_num_developers_diff_email
	exp = ["Author: Jeff George <jG@gmail.com>",\
	       "Author: Jeff George <jGeorge@yahoo.com>"]
	assert_equal 1, num_developers(exp), "Should be one developer"
  end
end
