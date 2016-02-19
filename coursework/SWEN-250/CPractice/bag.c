#include "bag.h"
#include <stdio.h>
#include <string.h>

struct node *first = NULL ;		/* initially the list is empty */


/* make_node
 * 
 * Creates a new node: with (a COPY of) a string, a count of 1, and NULL next 
 * link.
 *
 * Hint: strlen returns the length of a string, which is helpful for calculating
 * how much memory to allocate for the strig copy
 */

struct node *make_node(char *value) {
	/* YOUR CODE HERE */
	struct node *np = NULL;
	np = malloc(sizeof(struct node));
	
	np->value = malloc(strlen(value));
	np->count = 1;
	np->next = NULL;	

	strcpy(np->value, value);
	return np ;
}



/* insert_value
 * 
 * Traverse the linked list looking for a node matching the provided
 * string. We stop when (a) we find a matching string or (b) we hit the
 * end of the list. 
 *
 * Case (a) increments the node count and returns.
 * Case (b) insert a new node with count 1, via calling make_node
 *
 * Hint: strcmp(a,b) == 0 when strings a and b are equal
 */

void insert_value(char *value) {
	/* YOUR CODE HERE */
	struct node *nodeHead = make_node(value);
	struct node *cursor = first;
	if(!first){
	  first = nodeHead;
	  return;
	}
	else{	
	  while(cursor->next){
	    if(strcmp(cursor->value, value) != 0){
	      cursor = cursor->next;
	    }
	    else{
	      cursor = cursor->next;
	      cursor->count += 1;
	      break;
	    }
		
  	  }
 	  if(strcmp(cursor->value, value) == 0){
	    cursor->count += 1;
	  }
	  else if(cursor->next == NULL){
            cursor->next = nodeHead;
          }

	}  
//	if(cursor->next == NULL){
//	  cursor->next = nodeHead;
//	}
}

/* total_count
 *
 * Traverse the linked list totaling the number of items.
 *
 * Case (a) returns the total count of all items in the bag
 * Case (b) return 0 if the list is empty
 */


unsigned int total_count() {
	int count = 0;
	/* YOUR CODE HERE */
	struct node *cursor = first;
	if(!first){ return count;}
	else{
	  if(cursor->next){
	    while(cursor->next){
	      count += cursor->count;
	      cursor = cursor->next;
	
	    }
	    count += cursor->count;
	  }
	  else{return cursor->count;}
	}
	return count;
}

/* remove_value
 * 
 * Traverse the nexted list looking for a node matching the provided
 * string. We stop when (a) we find a matching string or (b) we hit the
 * end of the list 
 *
 * Case (a) decrements the node count (no lower than 0);
 * Case (b) simply returns.
 *
 * Note that when the count reaches 0 the node is NOT removed from the list.
 *
 */

void remove_value(char *value) {
	/* YOUR CODE HERE */

        struct node *cursor = first;
        if(!first){
           return;
        }
        else{
          while(cursor->next){
            if(strcmp(cursor->value, value) != 0){
              cursor = cursor->next;
            }
            else{
	      if(cursor->count > 1){
		cursor->count -= 1;
		break;
	      }
	      else{
                cursor = cursor->next;
                
                break;
	      }
            }

          }
          if(strcmp(cursor->value, value) == 0){
            cursor->count -= 1;
          }
          

        }


}


/* garbage_collect
 *
 * Remove and free all zero-count strings from the bag
 *
 * Traverse the list looking for a node that has a count of 0 or less. 
 * Re-assign pointers so that the linked list integrity remains intact. 
 * Free all unused memory.
 *`
 * Hint: keep an extra pointer to the PREVIOUS item in the list
 */
void garbage_collect(){
	/* YOUR CODE HERE */
	if(!first){return;}
	struct node *cursor = first;
	struct node *prevCurs = cursor;
	
	if(cursor->count <= 0){
	  struct node *nHead;
	  
	  nHead = cursor->next;
	  free(cursor);
	  cursor = NULL;
	  if(nHead){
	    cursor = malloc(sizeof(struct node));
	    cursor->count = nHead->count;
	    cursor->next = nHead->next;
	    cursor->value = nHead->value;
	  }
	}
	else{
	  while(cursor->next){
	    if(cursor->count <= 0){
	      struct node *nHead;
	  
	      nHead = cursor->next;
	      free(cursor);
	      cursor = NULL;
	
	      
	      if(nHead){
	        cursor = malloc(sizeof(struct node));
	        cursor->count = nHead->count;
	        cursor->next = nHead->next;
	        cursor->value = nHead->value;
	      }
	      else{
		if(prevCurs){
		  prevCurs->next = NULL;
	        }

	      }
	    }
	    else{
	      struct node *prevCurs = cursor;
	      cursor = cursor->next;
	    }
	  }
	  if(cursor->count <= 0){
	    struct node *nHead;
	  
	    nHead = cursor->next;
	    free(cursor);
	    cursor = NULL;
	    if(nHead){
	      cursor = malloc(sizeof(struct node));
	      cursor->count = nHead->count;
	      cursor->next = nHead->next;
	      cursor->value = nHead->value;
	    }
	    else{
	      if(prevCurs){
		prevCurs->next = NULL;
	      }

	    }
	 
	  }
	
	}
	
	
}

/* print_bag
 * 
 * Traverse the list and print it out. 
 * Delimited by tabs and newlines.
 *
 * You do not need to edit this function.
 *
 */
void print_bag(){
	struct node* walker = first;
	while(walker != NULL){
		printf("\t%s\t%i\n", walker->value, walker->count);
		walker = walker->next;
	}
}
