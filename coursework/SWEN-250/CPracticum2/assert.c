#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include "assert.h"

/*
 * Counts of assertion failures and passes
 * along with the number of tests.
 */
static int nfail = 0 ;
static int npass = 0 ;
static int ntests = 0 ;

/*
 * Test mode - determines when failures cause program exit.
 */
static t_mode mode = RUN_ALL ;

/*
 * Start a new test.
 *
 * If the *last* test resulted in assertion failures,
 * and if we're running to test failure, print a
 * summary and exit.
 * Otherwise print a new test message, remember the number of
 */
void newtest(char *testname) {
	if( mode == RUN_TO_TEST_FAILURE && nfail > 0) {
		summary() ;
		fprintf(stderr, "*** Exit on test failure ***\n") ;
		exit(1) ;
	}
	fprintf(stderr, "\n*** Test %s ***\n\n", testname) ;

	ntests++ ;
	return ;
}

void set_test_mode(t_mode m) {
	mode = m ;
}

void summary() {
	fprintf(stderr,"\nTesting summary\n") ;
	if(ntests > 0) {
		fprintf(stderr, "Tests: %d\n", ntests) ;
	}
	fprintf(stderr, "Assertions passed: %d\n", npass) ;
	fprintf(stderr, "Assertions failed: %d\n", nfail) ;
}

bool assert_impl(int cond, char *mesg, char *file, int line) {
	if( cond ) {
		npass++ ;
	} else {
		nfail++ ;
		fprintf(stderr, "Assertion failure (%s@%d): %s\n",
				file, line, mesg) ;

		if( mode == RUN_TO_ASSERT_FAILURE ) {
			summary() ;
			fprintf(stderr, "*** Exit on assert failure ***\n") ;
			exit(1) ;
		}
	}
	return cond ;
}

bool assert_strs_eq_impl(
		char *want, char *have, char *file, int line) {

	int cond = strcmp(want, have) == 0 ;

	if( cond ) {
		npass++ ;
	} else {
		nfail++ ;
		fprintf(stderr, "Assertion failure (%s@%d): string equality\n",
			file, line) ;
		fprintf(stderr, "   want \"%s\"\n", want) ;
		fprintf(stderr, "   have \"%s\"\n", have) ;

		if( mode == RUN_TO_ASSERT_FAILURE ) {
			summary() ;
			fprintf(stderr, "*** Exit on assert failure ***\n") ;
			exit(1) ;
		}
	}

	return cond ;
}
