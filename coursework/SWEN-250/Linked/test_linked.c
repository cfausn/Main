#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

#include "assert.h"
#include "memory.h"
#include "linked.h"

/*
 * Other includes here
 */

static void test1() ;
static void test2() ;
static void test3() ;
static void test4() ;

int main() {
	set_test_mode(RUN_TO_TEST_FAILURE) ;

	test1() ;
	test2() ;
	test3() ;
	test4() ;

	summary() ;
}

static void test1() {
	newtest("making & freeing nodes np1 & np2") ;
	node *np1 ;
	node *np2 ;

	printf("\nAllocate two nodes\n") ;
	printf("    Make a node for np1\n") ;
	np1 = make_node(0) ;
	assert(np1 != NULL) ;

	printf("    Make a node for np2\n") ;
	np2 = make_node(100) ;
	assert(np2 != NULL) ;

	printf("    Should have two areas allocated\n") ;
	assert(allocated_area_count() == 2) ;

	printf("\nCheck the nodes for correct contents and next links\n") ;
	printf("   np1: contents == 0 and next == NULL\n") ;
	assert(np1->contents == 0) ;
	assert(np1->next == NULL) ;
	printf("   np2: contents == 100 and next == NULL\n") ;
	assert(np2->contents == 100) ;
	assert(np2->next == NULL) ;

	printf("\nFree both nodes - 0 allocated areas at end\n") ;
	free_node(np1) ;
	free_node(np2) ;
	assert(allocated_area_count() == 0) ;
}

static void test2() {
	node *head = NULL ;
	node *np = NULL ;

	newtest("list Length") ;

	printf("\nTest the empty list for length 0\n") ;
	assert(list_length(NULL) == 0) ;

	printf("\nTest lists of length 1, 2, 3\n") ;
	printf("   first node - length == 1\n") ;
	head = make_node(123) ;
	assert(list_length(head) == 1) ;

	printf("   add node - length == 2\n") ;
	np = make_node(456) ;
	np->next = head ; head = np ;
	assert(list_length(head) == 2) ;

	printf("   add node - length == 3\n") ;
	np = make_node(789) ;
	np->next = head ; head = np ;
	assert(list_length(head) == 3) ;

	printf("\nReturn all the node storage\n") ;

	np = head ; head = head->next ; free_node(np) ;
	np = head ; head = head->next ; free_node(np) ;
	np = head ; head = head->next ; free_node(np) ;

	printf("    length == 0 at end\n") ;
	assert(list_length(head) == 0) ;
	printf("    no space allocated at end\n") ;
	assert(allocated_area_count() == 0) ;
}

static void test3() {
	node *head = NULL ;
	node *np1 = NULL ;
	node *np2 = NULL ;

	newtest("list_put_at functions") ;

	printf("    Put 1 at head\n") ;
	head = list_put_at_head(head, 1) ;
	assert(head->contents == 1) ;

	printf("    Put 2 at head\n") ;
	head = list_put_at_head(head, 2) ;
	assert(head->contents == 2 && head->next->contents == 1) ;

	printf("    Put 9 at tail\n") ;
	head = list_put_at_tail(head, 9) ;
	assert(head->contents == 2 &&
		head->next->contents == 1 &&
		head->next->next->contents == 9) ;
	assert(head->next->next->next == NULL) ;

	printf("    Put 99 at 1\n") ;
	head = list_put_at_pos(head, 99, 1) ;
	assert(head->contents == 2) ;
	assert(head->next->contents == 99) ;
	assert(head->next->next->contents == 1) ;
	assert(head->next->next->next->contents == 9) ;

	printf("\nTrim list size to 2\n") ;
	np1 = head->next ;
	np2 = np1->next ; np1->next = NULL ;
	np1 = np2->next ; free_node(np2) ;
	np2 = np1->next ; free_node(np1) ;
	printf("    final node pointer is NULL\n") ;
	assert(np2 == NULL) ;
	printf("    two areas still allocated\n") ;
	assert(allocated_area_count() == 2) ;
	printf("    length of list == 2\n") ;
	assert(list_length(head) == 2) ;

	printf("    put -1 at 100 (end of the list)\n") ;
	head = list_put_at_pos(head, -1, 100) ;
	assert(head->next->next->contents == -1) ;

	printf("    put 55 at 0 (front of list)\n") ;
	head = list_put_at_pos(head, 55, 0) ;
	assert(head->contents == 55 && head->next->contents == 2) ;

	printf("\nCleanup - 0 areas allocated at end\n") ;
	np1 = head->next ; free_node(head) ; head = np1 ;
	np1 = head->next ; free_node(head) ; head = np1 ;
	np1 = head->next ; free_node(head) ; head = np1 ;
	np1 = head->next ; free_node(head) ;
	assert(np1 == NULL) ;
	assert(allocated_area_count() == 0) ;
}

/*
 * Tests of list_find and list_remove.
 */
static void test4() {
	node *head = NULL ;
	node *np1 = NULL ;
	node *np2 = NULL ;

	newtest("list_find & list_remove") ;

	printf("\nMake a list and ensure its length is 3.\n") ;
	printf("List is 11 -> 22 -> 33 -> NULL\n") ;
	head = list_put_at_tail(
			list_put_at_head(
				list_put_at_head(head, 22),
				11),
			33) ;
	assert(list_length(head) == 3) ;

	printf("\nFind the values in the list\n") ;
	printf("    Find 11 @ 0\n") ;
	assert(list_find(head, 11) == 0) ;
	printf("    Find 22 @ 1\n") ;
	assert(list_find(head, 22) == 1) ;
	printf("    Find 33 @ 2\n") ;
	assert(list_find(head, 33) == 2) ;

	printf("\nRemove the elements from the list\n") ;
	printf("    Remove 22\n") ;
	head = list_remove(head, 22) ;
	assert(list_find(head, 22) == (-1)) ;

	printf("    Remove 33\n") ;
	head = list_remove(head, 33) ;
	assert(list_find(head, 33) == (-1)) ;

	printf("    Remove 11\n") ;
	head = list_remove(head, 11) ;
	assert(list_find(head, 11) == (-1)) ;

	printf("\nHead should be NULL - 0 allocated areas at end\n") ;
	assert(head == NULL) ;
	assert(allocated_area_count() == 0) ;
}
