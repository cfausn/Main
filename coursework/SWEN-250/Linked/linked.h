/*
 * Interface to a linked list module (nodes simply contain integers).
 */

#ifndef LINKED_H
#define LINKED_H

#include <stdbool.h>

/*
 * Structure of a list node.
 */
typedef struct _node {
	int contents ;
	struct _node *next ;
} node ;

/*
 * Return a pointer to a node with <value> as its contents and
 * a NULL next link.
 */
extern node *make_node(int value) ;

/*
 * Free the node addressed by <p_node>.
 */
extern void free_node(node *p_node) ;

/*
 * Return the length of the list headed by <p_head>.
 */
extern int list_length(node *p_head) ;

/*
 * Put a node with the given <value> at a specific location in the
 * list headed by <p_head> and return the (possibly) new head
 * of the list.
 *
 * In the case of putting at a position, the new node goes immediately
 * before the node at position <pos> (the first node is position 0).
 */
extern node *list_put_at_head(node *p_head, int value) ;
extern node *list_put_at_tail(node *p_head, int value) ;
extern node *list_put_at_pos(node *p_head, int value, int pos) ;

/*
 * Find the first node with a given <value> in the list headed by
 * <p_head> and return its index in the list (the head element is
 * at position 0). Returns (-1) if the value is not in the list.
 */
extern int list_find(node *p_head, int value) ;

/*
 * Remove the first node whose contents equal <value> and return
 * a pointer to the head of the resulting list.
 * Has no effect if the given <value> is not in the list.
 * The node space for the removed <value>, if any, is freed.
 */
extern node *list_remove(node *p_head, int value) ;

#endif
