/*
 * Maintain quantitys of animals in the zoo.
 *
 * Animals have a class (mammal, bird, etc.) and a species,
 * both encoded as unsigned integers.
 *
 * The species numbers are only guaranteed to be unique to a given class
 * (that is, a lion could be species 1 in mammal and a turtle could be
 * species 1 in reptile).
 */

#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>

#include "memory.h"
#include "zoo.h"

/*
 * A <animal> records the <class> and <species> integer codes for
 * an animal along with the <quantity> in the collection.
 *
 * There is a link to the <next_animal> in the collection list,
 * which is NULL for the last animal in the list.
 */
typedef struct _animal {
	unsigned class ;
	unsigned species ;
	unsigned quantity ;
	struct _animal *next_animal ;
} animal ;

/*
 * Pointer to the first animal (if any) in the animal list.
 * Initially the list is empty.
 */
static animal *alist_head = NULL ;

/*
 * ***** HELPER FUNCTION YOU MAY FIND USEFUL ********
 *
 * Return true if and only if the animal contents
 * referenced by NON-NULL pointer <p_animal> 
 * match the <class> and <species>.
 */
static bool match(animal *p_animal, unsigned class, unsigned species) {
	return (p_animal->class == class && p_animal->species == species) ;
}

/*
 * Add <number> new animals of the given <class> and <species> 
 * to the zoo's existing collection. That is, increment the zoo's
 * quantity of this animal by <number>.
 *
 * IMPLEMENTATION NOTES:
 *
 * If a animal node is in the list for <class> and <species> then
 * simply increment its <quantity>.
 * Otherwise, create a new animal node, initialize its fields
 * <class> and <species>, set the <quantity> to <number> and
 * place the node at any convenient location in the list.
 ** 
 **  Consider using match() to help compare if what you got
 **  is in your search 
 **
 */
void  add_animals(unsigned class, unsigned species, unsigned number) {
    animal *p_animal = alist_head;
    // ADD YOUR CODE HERE:
	if(!p_animal){
	  p_animal = malloc(sizeof(animal));
	  p_animal->class = class;
	  p_animal->quantity = number;
	  p_animal->next_animal = NULL;
	  p_animal->species = species;
	  alist_head = p_animal;
	  return;
	}
	if(match(p_animal, class, species)){
	  p_animal->quantity += number;
	  return;
	}
	while(p_animal->next_animal){
	  if(match(p_animal,class,species)){
	    p_animal->quantity += number;
	    return;
	  }
	  else{
	    p_animal = p_animal->next_animal;
	  }
	}

	if(match(p_animal, class, species)){
	  p_animal->quantity += number;
	  return;
	}

	else{
	  animal *newAnimal = malloc(sizeof(animal));
	  newAnimal->class = class;
	  newAnimal->species = species;
	  newAnimal->quantity = number;
	  newAnimal->next_animal = NULL;
	  p_animal->next_animal = newAnimal;
	}
	return ;
}

/*
 * Return the count of the given animal (<class> and <species>) held
 * by the zoo.
 *
 * IMPLEMENTATION NOTES:
 * Search the list for the given <class> and <species>; if found, return
 * the associated <quantity>. Otherwise return 0.
 */
unsigned animal_count(unsigned class, unsigned species) {
    // ADD YOUR CODE HERE:
        animal *p_animal = alist_head;
	


	if(!p_animal){ return;}
	
	if(match(p_animal, class, species)){return p_animal->quantity;}

	while(p_animal->next_animal){
	  if(match(p_animal, class, species)){
	    return p_animal->quantity;
	  }
	  else{p_animal = p_animal->next_animal;}
	}
	
	if(match(p_animal, class, species)){return p_animal->quantity;}
	
	return 0 ;	// placeholder
}

/*
 * Return the number of animals belonging to the given <class>
 * held by the zoo.
 *
 * IMPLEMENTATION NOTES:
 * Starting with a total of zero, search the list for any and all
 * animals in the specified <class>, adding the associated <quantity> to
 * the total.
 * At end, return the total.
 */
unsigned class_count(unsigned class) {
    // ADD YOUR CODE HERE:
	animal *p_animal = alist_head;
	int count = 0;
	
	while(p_animal->next_animal){
	  if(p_animal->class == class){
	     count += p_animal->quantity;
	     p_animal = p_animal->next_animal;}
	     
	  
	  else{
	   p_animal = p_animal->next_animal;}
	}

	
	if(p_animal->class == class){count += p_animal->quantity;}
	
	return count ;	// placeholder
}

/*
 * Close the zoo - at the end, the zoo has no animals.
 *
 * IMPLEMENTATION NOTES:
 * Release the storage for all animal nodes in the list, then
 * set the pointer to the head of the list to NULL.
 *
 * BE CAREFUL! Do not release the space for a node until you've
 * saved the pointer to its successor for use on the next iteration.
 */
void close_zoo() {
    // ADD YOUR CODE HERE:
	animal *p_animal = alist_head;
	animal *next_animal = p_animal->next_animal;
	while(next_animal){
	  free(p_animal);
	  p_animal = NULL;
	  p_animal = next_animal;
	  next_animal = next_animal->next_animal;
	}
	free(p_animal);
	p_animal = NULL;	
	alist_head = NULL;
	return ;

}
