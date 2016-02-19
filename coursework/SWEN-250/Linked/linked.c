/*
 * Implementation of the linked list module.
 */

#include <stdlib.h>
#include <stdbool.h>

#include "memory.h"
#include "linked.h"
;
/*
 * Return a pointer to a node with <value> as its contents and
 * a NULL next link.
 */
node *make_node(int value) {
	node *nv;
	nv = malloc(sizeof(node));
	nv->contents = value;
	nv->next = NULL;
	
	return nv;	// placeholder
}

/*
 * Free the node addressed by <p_node>.
 */
void free_node(node *p_node) {
	free(p_node);
	return ;
}

/*
 * Return the length of the list headed by <p_head>.
 */
int list_length(node *p_head) {
	if(!p_head) return 0;
	int counter = 0;
	
	counter++;
	
	while(p_head->next){
	  p_head = p_head->next;
	  counter++;
	}
	
	return counter;
}

/*
 * Put a node with the given <value> at the front of the list
 * headed by <p_head>, returning a pointer to the resulting
 * head of the list.
 */
node *list_put_at_head(node *p_head, int value) {
	/* YOUR CODE HERE */
	node *head;
	head = malloc(sizeof(node));
	head->next = p_head;
	head->contents = value;
	return head;	// placeholder
}

/*
 * Put a node with the given <value> at the end of the list
 * headed by <p_head>, returning a pointer to the resulting
 * head of the list.
 */
node *list_put_at_tail(node *p_head, int value) {
	/* YOUR CODE HERE */
	
	node *tail;
	node *nHead = p_head;
	tail = make_node(value);

	if(!p_head) return tail;
	
	while(nHead->next){
	  nHead = nHead->next;
	  
	}
	nHead->next = tail;
		
	return p_head;	// placeholder
}

/*
 * Put a node with the given <value> before the node at position
 * <pos> in the list headed by <p_head>, returning a pointer to
 * the resulting head of the list.
 * 	1. 0 is the head position.
 * 	2. <pos> >= list_length(p_head) then the new node
 * 	   is placed at the end of the list.
 */
node *list_put_at_pos(node *p_head, int value, int pos) {
	if(pos >= list_length(p_head)){
	  return list_put_at_tail(p_head, value);
	}
	else if(pos == 0){
	  return list_put_at_head(p_head, value);
	}

	int counter = 0;
	node *nHead = p_head;
	node *newNode = make_node(value);
	while(pos != counter){
	  counter++;
	  if(pos != counter){ nHead = nHead->next;}
	}
	newNode->next = nHead->next;
	nHead->next = newNode;
	
	return p_head ;	// placeholder
}

/*
 * Find the first node with a given <value> in the list headed by
 * <p_head> and return its index in the list (the head element is
 * at position 0). Returns (-1) if the value is not in the list.
 */
int list_find(node *p_head, int value) {
	/* YOUR CODE HERE */
	if(!p_head) return -1;
	int counter = 0;
	if(p_head->contents == value) return counter;
	while(p_head->next){
	  counter++;
	  p_head = p_head->next;
	  if(p_head->contents == value) return counter;
	}
	return (-1) ;	// placeholder
}

/*
 * Remove the first node whose contents equal <value> and return
 * a pointer to the head of the resulting list.
 * Has no effect if the given <value> is not in the list.
 * The node space for the removed <value>, if any, is freed.
 */
extern node *list_remove(node *p_head, int value) {
	/* YOUR CODE HERE */

	if(!p_head) return NULL;

	if(p_head->contents == value){
	  node *nHead;
	  nHead = p_head->next;
	 
	  free(p_head);
	  return nHead;
	}
	
	p_head->next = list_remove(p_head->next,value);

	


	return p_head ;	// placeholder
}
