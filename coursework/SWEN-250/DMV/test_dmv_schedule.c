#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

#include "assert.h"
#include "memory.h"
#include "dmv_schedule.h"

/*
 * Other includes here
 */

static void test_init_service_lines() ;
static void test_all_lines_empty() ;
static void test_all_counts_zero() ;
static void test_next_ticket() ;
static void test_add_a_customer_to_each_line() ;
static void test_add_second_customer_to_each_line() ;
static void test_add_third_customer_to_each_line() ;
static void intermission1() ;
static void test_serve_2_Bs() ;
static void test_serve_an_A_and_a_C() ;
static void intermission2() ;
static void test_serve_highest_priority() ;

//int main() {
int main(int argc, char *argv[]) {

	if (argc == 2){
		set_test_mode(RUN_ALL) ;
	}
	else {
		set_test_mode(RUN_TO_ASSERT_FAILURE) ;
	}

	test_init_service_lines() ;
	test_all_lines_empty() ;
	test_all_counts_zero() ;
	test_next_ticket() ;
	test_add_a_customer_to_each_line() ;
	test_add_second_customer_to_each_line() ;
	test_add_third_customer_to_each_line() ;

	intermission1() ;

	test_serve_2_Bs() ;
	test_serve_an_A_and_a_C() ;

	intermission2() ;

	test_serve_highest_priority() ;

	test_all_lines_empty() ;
	test_all_counts_zero() ;
	summary() ;
}

static void test_init_service_lines() {
	newtest("initialization of service_line line array") ;

	init_service_lines() ;

	assert( line[0].priority == 'A' ) ;
	assert( line[0].head_of_line == NULL ) ;
	assert( line[1].priority == 'B' ) ;
	assert( line[1].head_of_line == NULL ) ;
	assert( line[2].priority == 'C' ) ;
	assert( line[2].head_of_line == NULL ) ;
}

static void test_all_lines_empty() {
	newtest("service lines are empty") ;

	assert( serve_customer('A') == NO_CUSTOMER ) ;
	assert( serve_customer('B') == NO_CUSTOMER ) ;
	assert( serve_customer('C') == NO_CUSTOMER ) ;
	assert( serve_highest_priority_customer() == NO_CUSTOMER ) ;
}

static void test_all_counts_zero() {
	newtest("line counts are zero") ;

	assert( customer_count('A') == 0 ) ;
	assert( customer_count('B') == 0 ) ;
	assert( customer_count('C') == 0 ) ;
	assert( customer_count_all() == 0 ) ;
}

static void test_next_ticket() {
	int ticket ;
	newtest("generate correct next ticket") ;

	ticket = next_ticket() ;
	assert( ticket == 1 ) ;

	ticket = next_ticket() ;
	assert( ticket == 2 ) ;

	next_ticket() ;		// skip one
	ticket = next_ticket() ;
	assert( ticket == 4 ) ;
}

static void test_add_a_customer_to_each_line() {
	newtest("add a single customer to each line") ;

	new_customer('C', next_ticket()) ;	// ticket 5
	new_customer('A', next_ticket()) ;	// ticket 6
	new_customer('B', next_ticket()) ;	// ticket 7

	printf("Check for correct tickets at head of each line\n") ;
	assert(line[0].head_of_line != NULL &&
			line[0].head_of_line->ticket_number == 6) ;
	assert(line[1].head_of_line != NULL &&
			line[1].head_of_line->ticket_number == 7) ;
	assert(line[2].head_of_line != NULL &&
			line[2].head_of_line->ticket_number == 5) ;

	printf("Checks for correct customer counts\n") ;
	assert( customer_count('A') == 1 ) ;
	assert( customer_count('B') == 1 ) ;
	assert( customer_count('C') == 1 ) ;
	assert( customer_count_all() == 3 ) ;
}

static void test_add_second_customer_to_each_line() {
	newtest("add a second customer to each line") ;

	new_customer('A', next_ticket()) ;	// ticket 8
	new_customer('C', next_ticket()) ;	// ticket 9
	new_customer('B', next_ticket()) ;	// ticket 10

	printf("Check for correct tickets at head of each line\n") ;
	assert(line[0].head_of_line != NULL &&
			line[0].head_of_line->ticket_number == 6) ;
	assert(line[1].head_of_line != NULL &&
			line[1].head_of_line->ticket_number == 7) ;
	assert(line[2].head_of_line != NULL &&
			line[2].head_of_line->ticket_number == 5) ;

	printf("Checks for correct customer counts\n") ;
	assert( customer_count('A') == 2 ) ;
	assert( customer_count('B') == 2 ) ;
	assert( customer_count('C') == 2 ) ;
	assert( customer_count_all() == 6 ) ;
}

static void test_add_third_customer_to_each_line() {
	newtest("add a third customer to each line") ;

	new_customer('B', next_ticket()) ;	// ticket 11
	new_customer('A', next_ticket()) ;	// ticket 12
	new_customer('C', next_ticket()) ;	// ticket 13

	printf("Checks for correct customer counts\n") ;
	assert( customer_count('A') == 3 ) ;
	assert( customer_count('B') == 3 ) ;
	assert( customer_count('C') == 3 ) ;
	assert( customer_count_all() == 9 ) ;
}

static void intermission1() {
	printf("\n** INTERMISSION #1 **\n") ;
	printf("At this point each line should have three customers with\n") ;
	printf("the following tickets in the order shown.\n") ;

	printf("Priority A line = 6  8 12\n") ;
	printf("Priority B line = 7 10 11\n") ;
	printf("Priority C line = 5  9 13\n") ;
}

static void test_serve_2_Bs() {
	newtest("serve two B customers") ;

	assert( serve_customer('B') == 7 ) ;
	assert( serve_customer('B') == 10 ) ;

	printf("Checks for correct customer counts\n") ;
	assert( customer_count('A') == 3 ) ;
	assert( customer_count('B') == 1 ) ;
	assert( customer_count('C') == 3 ) ;
	assert( customer_count_all() == 7 ) ;
}

static void test_serve_an_A_and_a_C() {
	newtest("serve an A and a C customer") ;

	assert( serve_customer('A') == 6 ) ;
	assert( serve_customer('C') == 5 ) ;

	printf("Checks for correct customer counts\n") ;
	assert( customer_count('A') == 2 ) ;
	assert( customer_count('B') == 1 ) ;
	assert( customer_count('C') == 2 ) ;
	assert( customer_count_all() == 5 ) ;
}

static void intermission2() {
	printf("\n** INTERMISSION #2 **\n") ;
	printf("At this point each line should have\n") ;
	printf("the following tickets in the order shown.\n") ;

	printf("Priority A line =  8 12\n") ;
	printf("Priority B line = 11\n") ;
	printf("Priority C line =  9 13\n") ;
}

static void test_serve_highest_priority() {
	newtest("serve highest priority customers") ;

	assert( serve_highest_priority_customer() == 8 ) ;
	assert( serve_highest_priority_customer() == 12 ) ;
	assert( serve_highest_priority_customer() == 11 ) ;
	assert( serve_highest_priority_customer() == 9 ) ;
	assert( serve_highest_priority_customer() == 13 ) ;
}
