#include <stdio.h>
#include "bag.h"

/* 
 * Acceptance tests for bag library
 *
 * Tests output to the console in the recommended order. That is:
 * (1) make_node
 * (2) insert_value
 * (3) total_count
 * (4) remove_value
 * (5) garbage_collect
 *
 * Do not edit this function.
 *
 */
int main(){
	printf("\n===Testing make_node===\n");
	struct node* bobby = make_node("bobby");
	if(bobby != NULL && bobby->count==1 && strcmp(bobby->value,"bobby")==0 && bobby->next == NULL){
		free(bobby->value);
		free(bobby);
		printf("\tNode successfully created! Good work. Keep going...\n");
	}else {
		printf("\tError! Node incorrectly made. Pointer must be non-null, count must be 1, next must be null. Exiting with error.\n");
		return 1;
	}

	printf("\n===Insert Value===\n");
	printf("Adding ann...\n");
	insert_value("ann");
	print_bag();

	printf("Adding zeke\n");
	insert_value("zeke");
	print_bag();

	printf("Adding zeke again...\n");
	insert_value("zeke");
	print_bag();

	printf("\n===Total Count===\n");
	printf("Total count should be 3: %i\n", total_count());
	printf("Adding mike...\n");
	insert_value("mike");
	print_bag();
	printf("Total count should be 4: %i\n",total_count());

	printf("\n===Remove===\n");
	printf("Removing first zeke...\n");
	remove_value("zeke");
	print_bag();
	printf("Removing second zeke...\n");
	remove_value("zeke");
	print_bag();
	printf("Try to remove zeke a third time...\n");
	remove_value("zeke");
	print_bag();
	printf("Total count should be 2: %i\n",total_count());

	printf("\n===Garbage Collect===\n");
	printf("Garbage collect zeke\n");
	garbage_collect();
	print_bag();

	printf("Remove mike and garbage collect.\n");
	remove_value("mike");
	garbage_collect();
	print_bag();
	printf("Total count should be 1: %i\n",total_count());

	printf("\n===Clean house===\n");
	remove_value("ann");
	garbage_collect();
	print_bag();
	printf("Total count should be 0: %i\n",total_count());
	return 0; //successful exit
}
