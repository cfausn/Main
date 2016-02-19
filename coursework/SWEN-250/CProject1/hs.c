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
	int line = 0;
	int parsed_line;//determines if the line is correctly formatted
	int i = 0;	//accumulator for CSVs
   	char * pch;	//char pointer for CSVs (had to research this one!)
	char strs[MAX_EVENTS][MAX_TIMESTRING +1]; //list of strings (split from CSVs)
	int counter = 0;//used for the buffers arrays
	int index;	//used for the for loop when printing
	line = read_line(next_line,MAX_LINELENGTH); //reads the line from the utility function
		
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
	  
	  //Now to send things to the buffer. I know I am supposed to use a 
	  //specific function here but I am having trouble understanding how
	  //to use it. 
	  if(atoi(strs[3]) == T_TEMPERATURE || atoi(strs[3]) == T_CO){
	    counter = rooms[atoi(strs[0])].event_count;

	    if(counter >= MAX_EVENTS){
		rooms[atoi(strs[0])].buffer[0] = rooms[atoi(strs[0])].buffer[1];
		rooms[atoi(strs[0])].buffer[1] = rooms[atoi(strs[0])].buffer[2];
		rooms[atoi(strs[0])].buffer[2] = rooms[atoi(strs[0])].buffer[3];
		rooms[atoi(strs[0])].buffer[3] = rooms[atoi(strs[0])].buffer[4];
	        rooms[atoi(strs[0])].buffer[4].sensor = atoi(strs[1]);
	        strcpy(rooms[atoi(strs[0])].buffer[4].time_stamp,strs[2]);
	        rooms[atoi(strs[0])].buffer[4].event_id = atoi(strs[3]);
	        rooms[atoi(strs[0])].buffer[4].event_info = atoi(strs[4]);
		rooms[atoi(strs[0])].event_count +=1;

		if(atoi(strs[3]) == T_TEMPERATURE && (rooms[atoi(strs[0])].buffer[4].event_info > MAX_TEMP ||
					rooms[atoi(strs[0])].buffer[4].event_info < MIN_TEMP)){
		  printf("Temperature alert @ %s: room %s / sensor %s / %s degrees.\n",
							strs[2],strs[0],strs[1],strs[4]);
		}
		else if(atoi(strs[3]) == T_CO && rooms[atoi(strs[0])].buffer[4].event_info > CO_LIMIT){
	           printf("Carbon monoxide alert @  %s: room %s / sensor %s / %s PPB.\n",
							strs[2],strs[0],strs[1],strs[4]);
		}
	    }
	    else{
	      rooms[atoi(strs[0])].buffer[counter].sensor = atoi(strs[1]);
	      strcpy(rooms[atoi(strs[0])].buffer[counter].time_stamp,strs[2]);
	      rooms[atoi(strs[0])].buffer[counter].event_id = atoi(strs[3]);
	      rooms[atoi(strs[0])].buffer[counter].event_info = atoi(strs[4]);
	      rooms[atoi(strs[0])].event_count += 1;

	      if(atoi(strs[3]) == T_TEMPERATURE && (rooms[atoi(strs[0])].buffer[counter].event_info > MAX_TEMP || 
				    rooms[atoi(strs[0])].buffer[counter].event_info < MIN_TEMP)){
	         printf("Temperature alert @ %s: room %s / sensor %s / %s degrees.\n",
					           strs[2],strs[0],strs[1],strs[4]);
	      }
	      else if(atoi(strs[3]) == T_CO && rooms[atoi(strs[0])].buffer[counter].event_info > CO_LIMIT){
	         printf("Carbon monoxide alert @  %s: room %s / sensor %s / %s PPB.\n",
						      strs[2],strs[0],strs[1],strs[4]);
	      }
	    }

    	  }

	  else if(atoi(strs[3]) == T_INTRUDER){
	    counter = rooms[atoi(strs[0])].event_count;
	    if(counter == MAX_EVENTS){
		rooms[atoi(strs[0])].buffer[0] = rooms[atoi(strs[0])].buffer[1];
		rooms[atoi(strs[0])].buffer[1] = rooms[atoi(strs[0])].buffer[2];
		rooms[atoi(strs[0])].buffer[2] = rooms[atoi(strs[0])].buffer[3];
		rooms[atoi(strs[0])].buffer[3] = rooms[atoi(strs[0])].buffer[4];
	        rooms[atoi(strs[0])].buffer[4].sensor = atoi(strs[1]);
	        strcpy(rooms[atoi(strs[0])].buffer[4].time_stamp,strs[2]);
	        rooms[atoi(strs[0])].buffer[4].event_id = atoi(strs[3]);
	        printf("Intruder alert @ %s: room %i / sensor %i\n",rooms[atoi(strs[0])].buffer[4].time_stamp, 
							 atoi(strs[0]),rooms[atoi(strs[0])].buffer[4].sensor);
		rooms[atoi(strs[0])].event_count += 1;

	    }
	    else{
 
	      rooms[atoi(strs[0])].buffer[counter].sensor = atoi(strs[1]);
	      strcpy(rooms[atoi(strs[0])].buffer[counter].time_stamp, strs[2]);
	      rooms[atoi(strs[0])].buffer[counter].event_id = atoi(strs[3]);
	      rooms[atoi(strs[0])].event_count += 1;
	      printf("Intruder alert @ %s: room %i / sensor %i\n",rooms[atoi(strs[0])].buffer[counter].time_stamp,
						       atoi(strs[0]),rooms[atoi(strs[0])].buffer[counter].sensor);
	    }
	  }
	  //print now 
	  else if(atoi(strs[3]) == T_PRINT){
	    printf("*****\nHome Security System: Room %s @ %s\n",strs[0],strs[2]);
	    printf("Triggered by sensor %s\n",strs[1]);
	    printf("%i total room events\n",rooms[atoi(strs[0])].event_count);

	    for(index = rooms[atoi(strs[0])].event_count; index != -1; index--){
		if(rooms[atoi(strs[0])].buffer[index].event_id == 1){
		  printf("Sensor %i @ %s temperature reading %i degrees\n",
			rooms[atoi(strs[0])].buffer[index].sensor, rooms[atoi(strs[0])].buffer[index].time_stamp,
			rooms[atoi(strs[0])].buffer[index].event_info);
		}
		else if(rooms[atoi(strs[0])].buffer[index].event_id == 2){
		  printf("Sensor %i @ %s carbon monoxide reading %i PPB\n",
			rooms[atoi(strs[0])].buffer[index].sensor, rooms[atoi(strs[0])].buffer[index].time_stamp,
			rooms[atoi(strs[0])].buffer[index].event_info);
		}
		else if(rooms[atoi(strs[0])].buffer[index].event_id == 3){
		  printf("Sensor %i @ %s intruder alert\n",rooms[atoi(strs[0])].buffer[index].sensor, 
			rooms[atoi(strs[0])].buffer[index].time_stamp);
		}
		
		 
	    }
	    
	    
	  }
	
	
	strcpy(next_line,""); 
	i = 0;
	line = read_line(next_line,MAX_LINELENGTH);
	
	parsed_line = parse_line(next_line); 
	}	
	
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
	//I didn't use this. Decided to use if statements instead because
	//I didn't understand how to use the reading_t struct.
	//what's the point of using the reading_t struct? It's so much
	//simpler to use the rooms array directly...
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
