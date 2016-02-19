/***
 * Functions for the DMV customer scheduling and service application.
 * Interface file.
 ***/

#ifndef DMV_SCHEDULE_H
#define DMV_SCHEDULE_H

/*
 * A given customer has a ticket number that uniquely identifies
 * him or her plus a pointer to the next customer in the list (NULL
 * for the last customer in a list).
 */
struct customer {
	int ticket_number ;
	struct customer *next_customer ;
} ;

/*
 * A service_line has a priority ('A', 'B', 'C') and a pointer to the
 * first customer in the line for that priority.
 */
struct service_line {
	char priority ;
	struct customer *head_of_line ;
} ;

/*
 * The number of service lines and the array of service lines (one
 * per priority, 'A', 'B', 'C').
 */
#define NLINES (3)

extern struct service_line line[NLINES] ;

/*
 * Value returned when no customers are in the desired line(s).
 */
#define NO_CUSTOMER (0)

/*
 * Initialize the service lines so that (a) line[0] has priority 'A'
 * through line[2] having priority 'C' and (b) there are no customers
 * in any line.
 */
extern void init_service_lines() ;

/*
 * Return the next ticket number.
 * 	The first customer gets ticket number 1.
 *	The number increases by 1 on each call.
 */
extern int next_ticket() ;

/*
 * A new customer arrives with the given <priority> and
 * <ticket_number>. The customer is placed at the end of
 * the appropriate service line.
 */
extern void new_customer(char priority, int ticket_number) ;

/*
 * Return the ticket number of the first customer in the
 * line for <priority> after removing the customer from the
 * associated service_line.
 *
 * Return NO_CUSTOMER if there are no customers in the indicated line.
 */
extern int serve_customer(char priority) ;

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
extern int serve_highest_priority_customer() ;

/*
 * Return the number of customers in the service line for <priority>
 */
extern int customer_count(char priority) ;

/*
 * Return the number of customers in all service lines.
 */
extern int customer_count_all() ;

#endif
