/*
 * Implementation of the read_data module.
 *
 * See read_data.h for a description of the read_data function's
 * specification.
 *
 * Note that the parameter declarations in this module must be
 * compatible with those in the read_data.h header file.
 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "read_data.h"

void read_data(int *intPoint, char *charPoint, double *dubPoint) {
	
	char line[26];
	int next_char;
	int i = 0;
	int dollarNum = 0;
	
	
	while( (next_char = getchar()) != '\n' && next_char != EOF){
		if(next_char == '$'){
		    if(dollarNum == 0){
		      *charPoint = line[0];
		    }
		    else if(dollarNum == 1){
		      line[i] = '\0';
		      *intPoint = atoi(line);
		    }
		    else if(dollarNum == 2){
		      line[i] = '\0';
		      *dubPoint = atof(line);
		    }
		    i = 0;
		    char line[26];
		    dollarNum++;
		}
		else{line[i] = next_char; i++;}
	}
	
	return ;
}
