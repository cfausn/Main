/*
 * Home Security System
 */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#include "hs_config.h"
#include "hs_util.h"

/*
 * Room event information
 * 	Total number of events that have been logged
 * 	Index of the newest event (if any)
 * 	Index of the oldest event (if any)
 * 	Buffer of (up to) MAX_EVENTS most recent events
 */
struct room_t {
	int event_count ;
	int newest ;
	int oldest ;
	struct event_t buffer[MAX_EVENTS] ;
} ;

/*
 * Rooms being monitored.
 */
#define MAX_ROOMS (5)
static struct room_t rooms[MAX_ROOMS] ;

/*
 * Local support functions (static).
 * Feel free to add more to make your work easier!
 */
static void process_a_reading(struct reading_t reading) ;
static void init_rooms() ; 

/*
 * Main driver function.
 *
 * First, initialize global data structures (rooms array).
 *
 * Next, read lines of text representing readings, parse these, and if there
 * are no syntax errors, record the associated events. Syntactically incorrect
 * input reading lines are silently discarded.
 */
int main() {
	char next_line[MAX_LINELENGTH+1] ;
	struct reading_t reading ;

	init_rooms() ;

	/*
	 * Read a line of text into next_line, then attempt to parse
	 * it as a reading line. If the line is parsable, get the
	 * last reading structure and process it according to the
	 * specification for the appropriate level.
	 * See hs_util.h for useful utility functions
	 */
	/* Your code here */
	return 0 ;
}

/*
 * Given a reading, process the included event for the room in the reading.
 * T_PRINT readings are really commands; once executed they are discarded.
 * For all other readings check to see whether an alert should be printed,
 * then add the event to as the newest event in the room's circular buffer.
 */
static void process_a_reading(struct reading_t reading) {
	/* Your code here */
}

/*
 * Initialize the information on all rooms so that no rooms
 * have any events associated with them.
 */
static void init_rooms() {
	int room_id ;

	/*
	 * Initialize rooms array so that all rooms have no
	 * events associated with them.
	 */

	for( room_id = 0 ; room_id < MAX_ROOMS ; room_id++ ) {
		rooms[room_id].event_count = 0 ;
		rooms[room_id].newest = 0 ;
		rooms[room_id].oldest = 0 ;
	}
}
