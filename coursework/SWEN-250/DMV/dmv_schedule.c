/***
 * Functions for the DMV customer scheduling and service application.
 * Implementation file.
 ***/

#include <stdlib.h>
#include "dmv_schedule.h"

/*
 * Actual definition of the line array of service lines.
 */
struct service_line line[NLINES] ;

/*
 * Initialize the service lines so that (a) line[0] has priority 'A'
 * through line[2] having priority 'C' and (b) there are no customers
 * in any line.
 * NOTES: As usual, an empty list is signified by a NULL pointer.
 */
void init_service_lines() {
	// Placeholder for your code

	//since there's only 3 lines, simply set values with this code.
	//if it was more complex I would have considered a loop.
	line[0].priority = 'A';
	line[0].head_of_line = NULL;
	line[1].priority = 'B';
	line[1].head_of_line = NULL;
	line[2].priority = 'C';
	line[2].head_of_line = NULL;
	
}

/*
 * Return the next ticket number.
 * 	The first customer gets ticket number 1.
 *	The number increases by 1 on each call.
 * Local (static) int ticket holds the current ticket value.
 */
static int ticket = 1 ;
int next_ticket() {
	//make a copy of ticket.
	int holdVal = ticket;
	//update ticket
	ticket++;
	return holdVal ;	//return the copy
}



/*
 * A new customer arrives with the given <priority> and
 * <ticket_number>. The new customer is placed at the end of
 * the appropriate service line.
 */
void new_customer(char priority, int ticket_number) {
	// Placeholder for your code.
	//Hint: Add comments first to clarify your steps
	//and consider creating a helper functions to determine the right line
	
	int i = 0; //index for line[].
	while(i < NLINES){
	  //if the priorities are the same...
	  if(priority == line[i].priority){
	    struct customer *cust = line[i].head_of_line;
	    
	    if(!cust){
	      //no customer has been made yet. Make a new one.
	      cust = malloc(sizeof(struct customer));
	      cust->ticket_number = ticket_number;
	      cust->next_customer = NULL;
	      line[i].head_of_line = cust;
	      return;
	    }
	    else{
	      //customer exists. Loop through to put at end.
	      struct customer *tempCust = cust;
	      while(tempCust->next_customer){
	        tempCust = tempCust->next_customer;
	      }
	      //malloc the new customer...
	      tempCust->next_customer = malloc(sizeof(struct customer));	     
	      tempCust->next_customer->ticket_number = ticket_number;
	      tempCust->next_customer->next_customer = NULL;
	      //set cust (not tempCust) to the head of the line
	      line[i].head_of_line = cust;

	      return;
	    }
	  }
	  i++;
	}
}

/*
 * Return the ticket number of the first customer in the
 * line for <priority> after removing the customer from the
 * associated service_line.
 *
 * Return NO_CUSTOMER if there are no customers in the indicated line.
 */
int serve_customer(char priority) {
	int i = 0;
	int ticketNum = 0;
	//same logic as above...
	while(i < NLINES){
	  if(line[i].priority == priority){
	    if(!line[i].head_of_line){return NO_CUSTOMER;}
	    else{
	      //after making a copy of the next customer, free the current customer
	      //and assign it's place to next_customer on the line.

	      struct customer *cust = line[i].head_of_line->next_customer;
	      ticketNum = line[i].head_of_line->ticket_number;
	      free(line[i].head_of_line);
	      line[i].head_of_line = cust;
	    }


	  }

	  i++;
	}

	return ticketNum ; // the freed customer's ticket number.
}

/*
 * Return the ticket number of the first customer in the highest
 * priority line that has customers after removing the customer
 * from the line. 'A' is highest priority and 'C' is lowest.
 *
 * Return NO_CUSTOMER if there are no customers in any of the lines.
 *
 * Example: if there are 0 customers in the 'A' line, 3 customers in the 'B'
 *          line and 2 customers in the 'C' line, then the first customer in
 *          the 'B' line would be removed and his/her ticket number returned.
 */
int serve_highest_priority_customer() {
	
	int i = 0;
		
	while(i < NLINES){
	  //just use the functions before to accomplish this task.
	  if(customer_count(line[i].priority) != 0){
	    return serve_customer(line[i].priority);
	  }
	  i++;
	}
	return NO_CUSTOMER ;
}

/*
 * Return the number of customers in the service line for <priority>
 */
int customer_count(char priority) {

	int count = 0;
	int i = 0;
	
	//same logic as adding a customer but this time I'm keeping a 
	//counter
	while(i < NLINES){
	  if(line[i].priority == priority){
	    struct customer *cust = line[i].head_of_line;
 	    if(!cust){return NO_CUSTOMER;}
	    count++;
	    if(!cust->next_customer){return count;}
	    while(cust->next_customer){
	      count++;
	      cust = cust->next_customer;
	      
	    }
	    
	    return count;
	
	  }
	  i++;
	}

	

	return NO_CUSTOMER ; // Placeholder just in case
}

/*
 * Return the number of customers in all service lines.
 */
int customer_count_all() {

	int count = 0;
	int i = 0;
	//just use customer_count and run through the number of lines.

	while(i < NLINES){
	  count+= customer_count(line[i].priority);
	  i++;
	}
	return count;


}
