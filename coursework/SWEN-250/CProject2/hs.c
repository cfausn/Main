/*
400
 * Home Security System
 */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#include "hs_config.h"
#include "hs_util.h"

/*
 * An event node on the linked list of events for
 * a room. Consists of an event as gathered from a
 * reading and a link to the next node on the list
 * (if any).
 */
struct evnode_t {
	struct event_t event ;
	struct evnode_t *next ;
} ;

/*
 * Room event information
 * 	The room number.
 * 	Total number of events that have been logged.
 * 	Pointer to the most recent reading's node (if any).
 * 	Pointer to the next room (if any).
 */
struct room_t {
	int room ;
	int ecount ;
	struct evnode_t *evl_head ;
	struct room_t *next_room ;
} ;

/*
 * Head of the list of rooms being monitored.
 */
static struct room_t *room_list = NULL ;

/*
 * Local support functions (static).
 * You have to fill in the details.
 * Feel free to add more to make your work easier!
 */
static void process_a_reading(struct reading_t reading) ;

static struct room_t *find_room(int room) ;

static struct room_t *add_new_room(char strs[5][MAX_TIMESTRING +1], int events); 

static struct room_t *append_to_room(int room, char strs[5][MAX_TIMESTRING +1]);


static void trim_list(int room, int keep, char timestamp[]) ;

static struct evnode_t *make_event_node() ;


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

	/*
	 * Read a line of text into next_line, then attempt to parse
	 * it as a <reading> line. If the line is parsable, get the
	 * last reading structure and process it according to the
	 * specification for the appropriate level.
	 * See hs_util.h for useful utility functions.
	 */
	
	// FILL IN THE BODY
	
	int parsed_line;//determines if the line is correctly formatted
	int i = 0;	//accumulator for CSVs
   	char * pch;	//char pointer for CSVs (had to research this one!)
	char strs[5][MAX_TIMESTRING +1]; //list of strings (split from CSVs)
	int found;
	
	read_line(next_line,MAX_LINELENGTH); //reads the line from the utility function
	
	parsed_line = parse_line(next_line); 

	while(parsed_line == 1){
	 
 	  //The following is a fancy way I found out how to parse CSV values into an array.
	  //it uses pointers which we haven't learned, but I understand it and it makes 
	  //the process easier.
	 
  	  pch = strtok(next_line,",");
	   
	  if(*pch == '0'){ 
	    strcpy(strs[i],"0");
	    i++;
	    pch = strtok(NULL, ",");
	  }
	  while(pch != NULL){
	    strcpy(strs[i],pch);
	    i++;
  	    pch = strtok(NULL, ",");
	  }
	  
	  found = 0;
	  struct reading_t theReading;
	  struct room_t *cursor = room_list;

	  //if the list is empty initialize it (with malloc of course)
	  if(!(room_list)){ 

	    if((atoi(strs[3]) != 9)){

	       room_list = malloc(sizeof(struct room_t));
	       room_list =  add_new_room(strs,0);
	       theReading.room_id = room_list->room;
	       theReading.event = room_list->evl_head->event;
	       process_a_reading(theReading);
	       }
	    else{
		//just print
	       theReading.room_id = atoi(strs[0]);
	       theReading.event.sensor = atoi(strs[1]);
	       strcpy(theReading.event.time_stamp,strs[2]); 
	       theReading.event.event_id = atoi(strs[3]);
	       theReading.event.event_info = atoi(strs[4]);
	    
	       process_a_reading(theReading);
	    }
	  }

	 
	  else{
	    //add a catch for the first room
	    if(cursor->room == atoi(strs[0])){
	      found = 1;
	    }
	    //loop through every room
	    while(cursor->next_room){
	      if(cursor->room == atoi(strs[0])){
	        found = 1;
		break;
	      }
	      else{
		 cursor = cursor->next_room;
		 if(cursor->room == atoi(strs[0])){
		    found = 1;
		  }
		}
	    }
	    if(found == 1){
	      //if the room is there append
	      struct room_t *tempCursor = append_to_room(atoi(strs[0]),strs);
	      if((atoi(strs[3]) != 9) && (tempCursor)){
		
	        cursor->ecount = tempCursor->ecount;
                cursor->evl_head = tempCursor->evl_head;
	        cursor->next_room = tempCursor->next_room;
	        theReading.room_id = cursor->room;
	        theReading.event = cursor->evl_head->event;

	        process_a_reading(theReading);
	      }
	      else if(tempCursor){
		//just print
                theReading.event.event_id = T_PRINT;
		theReading.room_id = atoi(strs[0]);
	  	theReading.event.sensor = atoi(strs[1]);
		strcpy(theReading.event.time_stamp,strs[2]);
		process_a_reading(theReading);
              }
               


    
	    }
	    else{
		//if the room isn't there make a new one
		if((atoi(strs[3]) != 9)){
		   cursor->next_room = malloc(sizeof(struct room_t));

		   cursor->next_room = add_new_room(strs,0);

	           theReading.room_id = cursor->next_room->room;
	           theReading.event = cursor->next_room->evl_head->event;
	           
		   process_a_reading(theReading);

	         }
		else{
		  //just print	    
	  	  theReading.room_id = atoi(strs[0]);
	  	  theReading.event.sensor = atoi(strs[1]);
	  	  strcpy(theReading.event.time_stamp,strs[2]); 
	   	  theReading.event.event_id = atoi(strs[3]);
	  	  theReading.event.event_info = atoi(strs[4]);

	    
	  	  process_a_reading(theReading);
		 }
		}
	  } 
	
	  //check if last added value requires action

	  strcpy(next_line,"");
	  
	  i = 0;
	  read_line(next_line,MAX_LINELENGTH); //reads the line from the utility function
    
          parsed_line = parse_line(next_line);
	  

	}
	return 0 ;
}

/*
 * Given a reading, process the included event for the room in the reading.
 * T_PRINT and T_TRIM readings are really commands; once executed they are
 * discarded.
 * For all other readings check to see whether an alert should be printed,
 * then add the event to as the newest event in the room's event list.
 */
static void process_a_reading(struct reading_t reading) {

	int index;
        struct room_t *cursor = find_room(reading.room_id);
	struct evnode_t *tCurs;
	

	tCurs = malloc(sizeof(struct evnode_t));
	//same logic as last project...
	if(reading.event.event_id == T_TEMPERATURE){
	 //weird issues with && here... just made another if statement inside
	  if(reading.event.event_info > MAX_TEMP || reading.event.event_info < MIN_TEMP){
	    printf("Temperature alert @ %s: room %i / sensor %i / %i degrees.\n",
		reading.event.time_stamp, reading.room_id, reading.event.sensor, reading.event.event_info);
	  }
	}
	else if(reading.event.event_id == T_CO && reading.event.event_info > CO_LIMIT){
	    printf("Carbon monoxide alert @  %s: room %i / sensor %i / %i PPB.\n",
		reading.event.time_stamp, reading.room_id, reading.event.sensor, reading.event.event_info);

	}
	else if(reading.event.event_id == T_INTRUDER){
	    printf("Intruder alert @ %s: room %i / sensor %i\n",
		reading.event.time_stamp, reading.room_id, reading.event.sensor);

	}
	else if(reading.event.event_id == T_PRINT){
	   // Time to print!!

	    
	    printf("*****\nHome Security System: Room %i @ %s\n",reading.room_id,reading.event.time_stamp);
            printf("Triggered by sensor %i\n",reading.event.sensor);
	    if(cursor){
              printf("%i total room events\n",cursor->ecount);
	    }
	    else{
              printf("%i total room events\n",0);
	    }

	    if(cursor){
	      if(cursor->evl_head){
 	        tCurs->event = cursor->evl_head->event;
	        tCurs->next = cursor->evl_head->next;
	     }
	     //else is really important after the TRIM command
	     else{return;}

	    //change to look for room number later
	
            for(index = cursor->ecount ; index != 0; index--){
	        if(index != cursor->ecount){
		 
		   tCurs = tCurs->next;
		
		}
		if(tCurs){reading.event = tCurs->event;}
		else{break;}

                if(reading.event.event_id == T_TEMPERATURE){
                  printf("Sensor %i @ %s temperature reading %i degrees\n",
                        reading.event.sensor, reading.event.time_stamp, reading.event.event_info);
                }
                else if(reading.event.event_id == T_CO){
                  printf("Sensor %i @ %s carbon monoxide reading %i PPB\n",  
		        reading.event.sensor, reading.event.time_stamp, reading.event.event_info);

		}
                else if(reading.event.event_id == T_INTRUDER){
                  printf("Sensor %i @ %s intruder alert\n",reading.event.sensor, reading.event.time_stamp);
                }



            }
	   }
	
	}


	return ;
}

/*
 * Find the specified <room> in the <room_list>, returning a pointer to the
 * found room_t structure or NULL if there is no such <room> in the list.
 */
static struct room_t *find_room(int room) {
	struct room_t *the_room ;
	the_room = room_list;
	//Pretty simple function, added some checks to make sure
	//the room actually exists.

	if(!room_list){
	  return NULL;
	}
	if(the_room->room == room){
	  return the_room;
	}
	else{
	  the_room = the_room->next_room;
	  while(the_room->room != room){
	    the_room = the_room->next_room;
	  }
	}
	if(the_room){
	  return the_room ;
	}
	else return NULL;
}

/*
 * Create a new room_t node for <room>, initialize its fields, and append
 * the node to the end of the <room_list>.
 * Returns a pointer to the new room's structure.
 */
static struct room_t *add_new_room(char strs[5][MAX_TIMESTRING +1], int events) {

	struct room_t *new_room ; // ptr. to new room structure
	new_room = malloc(sizeof(struct room_t));
	
	new_room->room = atoi(strs[0]);
	
	//set events (case for T_PRINT just in case)
	if(atoi(strs[3]) == T_PRINT){
	  new_room->ecount = events;
	}
	else{
	  new_room->ecount = events + 1;
	}

 
	struct event_t event;
	struct evnode_t *evnode;
	  
	evnode = malloc(sizeof(struct evnode_t));
	  
	//set event info
	event.sensor = atoi(strs[1]);
	strcpy(event.time_stamp,strs[2]); 
	event.event_id = atoi(strs[3]);
        if(atoi(strs[3]) != T_INTRUDER && atoi(strs[3]) != T_PRINT && atoi(strs[3]) != T_TRIM) {
	  event.event_info = atoi(strs[4]);
        }
	else event.event_info = 0;
	   
	evnode->event = event;
	evnode->next = NULL;
	new_room->evl_head = evnode; 
	new_room->next_room = NULL;

	

	return new_room ;
}

/*
 * Append a new node for <room>,
 * Returns a pointer to the appended room's structure.
 * COMMANDS WILL RUN THROUGH THIS FUNCTION.
 * if the command is "TRIM" then the function returns NULL, otherwise
 * there is a catch in the main function to not append a PRINT command
 * to the room.
 */

static struct room_t *append_to_room(int room, char strs[5][MAX_TIMESTRING +1]) {

	struct room_t *newHead;
	struct room_t *cursor;
	cursor = find_room(room);
	newHead = malloc(sizeof(struct room_t));

	newHead->room = cursor->room;

	//case for T_PRINT
	if(atoi(strs[3]) == T_PRINT){
	  newHead->ecount = cursor->ecount;
	}
	else{
	  newHead->ecount = cursor->ecount + 1;
	}
	newHead->next_room = cursor->next_room;

	struct event_t event;
	struct evnode_t *evnode;

	evnode = malloc(sizeof(struct evnode_t));
	
	event.sensor = atoi(strs[1]);
        strcpy(event.time_stamp,strs[2]); 
        event.event_id = atoi(strs[3]);
        if(atoi(strs[3]) != T_INTRUDER && atoi(strs[3]) != T_PRINT && atoi(strs[3]) != T_TRIM){
	   event.event_info = atoi(strs[4]);
	}
	else if(atoi(strs[3]) == T_TRIM){
	  //case for the TRIM command
	  trim_list(atoi(strs[0]), atoi(strs[4]), strs[2]);
	  return NULL;
	}
	else event.event_info = 0;

	evnode->event = event;
	evnode->next = cursor->evl_head;

	newHead->evl_head = evnode;

		
	return newHead;
}




/*
 * If the <room> is in the <room_list>, trim the room's event node list
 * to at most <keep> entries. As the list is ordered from newest to
 * oldest, the oldest entries are discarded.
 *
 * Whether the room exists or not, and whether or not the list holds
 * anything, the specified "Trim log" message must be printed. Obviously,
 * for a non-existent room nothing is actually trimmed (removed).
 *
 * Note - dynamically allocated space for event nodes removed from
 *        the list must be freed.
 */
static void trim_list(int room, int keep, char timestamp[]) {

	struct room_t *the_room;
	struct room_t *the_room_copy; //used to not mess with a pointer, copies instead

	struct evnode_t *eventArr[20];
	int index = 0;

	the_room_copy = malloc(sizeof(struct room_t));
	the_room = find_room(room);
	
	the_room_copy->room = the_room->room;
	the_room_copy->ecount = the_room->ecount;
	the_room_copy->evl_head = the_room->evl_head;
	
	int counter;
	int removed = 0;
	
	//look through the nodes. Print if empty
	for(counter = 0; counter != keep; counter++){
	 if(!(the_room_copy) || !(the_room_copy->evl_head->next)){
           printf("Trim log @ %s: room %i log trimmed to length %i (%i entries removed)\n",
		timestamp, room, keep, removed);
	   return;
	 }
	 the_room_copy->evl_head = the_room_copy->evl_head->next;
	}

	//set to the array and look through the room
	while(the_room_copy->evl_head){
	  eventArr[index] = the_room_copy->evl_head;
	  the_room_copy->evl_head = the_room_copy->evl_head->next;
	  index++;
	  removed++;
	}
	
	//free the nodes
	for(index = 0; index < removed; index++){
	  free(eventArr[index]);
	}

	//Terminate now
	int i;
	struct evnode_t *node_to_terminate = the_room->evl_head;
	if(keep == 0){
	 the_room->evl_head  = NULL;
	}
	  else{
	    for (i = 1; i < keep; ++i){
    	      node_to_terminate = node_to_terminate->next;
	    }
	
	  node_to_terminate->next = NULL;
	}


	//print now!
        printf("Trim log @ %s: room %i log trimmed to length %i (%i entries removed)\n",
		timestamp, room, keep, removed);

	
        return ;
}

