/*
 * bag.h
 * Defines the internal data structures and private functions
 * used by the implementation.
 */

#ifndef BAG_H
#define BAG_H

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

/*
 * A node in the linked list consists of a string value, an occurrence count,
 * and a pointers to the next node in the list.
 */

struct node {
	char *value ;
	unsigned int count ;
	struct node *next ;
} ;

/*
 * The first node in the list (if any). An empty list has first == NULL.
 * Actually defined in bag.c
 */

extern struct node *first ;

/*
 * Public interface to the bag implementation. Bags are sets that allow duplicates. 
 * This implementation maintains duplicates via counts to save space.
 *
 */
extern struct node *make_node(char *value) ;
extern unsigned int total_count() ;
extern void insert_value(char *value) ;
extern void remove_value(char *value) ;
extern void garbage_collect();
extern void print_bag();

#endif
