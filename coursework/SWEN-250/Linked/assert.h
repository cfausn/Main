/*
 * Interface to assertion package for use in unit testing.
 */

#ifndef ASSERTION_H
#define ASSERTION_H

#include <stdbool.h>

/*
 * Most tests should use the assertion macros below.
 *
 * assert(expr)
 * 	Assert <expr> is true; if not, print the <expr> as a string,
 * 	along with file and line number of the failure.
 * assert_mesg(expr, mest)
 * 	Like assert except rather than printing <expr> as a string
 * 	on failure, string <mesg> is used.
 * assert_strs_eq(want, have)
 * 	Assert that the two strings, <want> and <have>, are equal in
 * 	length and in the sequence of characters.
 */

#define assert(expr) assert_impl((expr), #expr, __FILE__, __LINE__)
#define assert_mesg(expr, mesg) assert_impl((expr), (mesg), __FILE__, __LINE__)

#define assert_strs_eq(want, have) \
	assert_strs_eq_impl((want), (have), __FILE__, __LINE__)

/*
 * Signals the start of a new test
 */
extern void newtest(char *testname) ;

/*
 * Type to specify the mode of execution
 */
typedef enum {
    RUN_ALL,                // run all tests to completion.
    RUN_TO_TEST_FAILURE,    // run until a test fails (>= 1 assertions fail)
    RUN_TO_ASSERT_FAILURE   // run until an assertion fails.
} t_mode ;

/*
 * Set the test mode (default is RUN_ALL)
 */
extern void set_test_mode(t_mode mode) ;

/*
 * Print a summary of the tests and assertions executed.
 */
extern void summary() ;

/************
 * The functions implementing the assertion macros.
 * Rarely if ever used by clients.
 ***********/

/*
 * Simple assertion - is the condition true?
 */
extern bool assert_impl(int cond, char *mesg, char *file, int line) ;

/*
 * Assert to strings are equal (same length and char. sequence).
 */
extern bool assert_strs_eq_impl(
		char *want, char *have, char *file, int line) ;

#endif
