
/*
 * Implementation of functions that find values in strings.
 *****
 * YOU MAY NOT USE ANY FUNCTIONS FROM <string.h>
 *****
 */

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#include "find.h"

#define NOT_FOUND (-1)	// integer indicator for not found.

/*
 * Return the index of the first occurrence of <ch> in <string>,
 * or (-1) if the <ch> is not in <string>.
 */
int find_ch_index(char string[], char ch) {
	int index = -1;
	int tChar;
	int i = 0;

	tChar = string[i];
	for(i = 0; tChar != '\0';++i){
	  
	  tChar = string[i]; 
	  if(tChar == ch){
	    return i;
	  }
	
	}
	
	return NOT_FOUND;	// placeholder
}

/*
 * Return a pointer to the first occurrence of <ch> in <string>,
 * or NULL if the <ch> is not in <string>.
 *****
 * YOU MAY *NOT* USE INTEGERS OR ARRAY INDEXING.
 *****
 */
char *find_ch_ptr(char *string, char ch) {
	char *point = string;

	while(*point != '\0'){
	  if(*point == ch) return point;
	  else point++;
	}
	return NULL;	// placeholder
}

/*
 * Return the index of the first occurrence of any character in <stop>
 * in the given <string>, or (-1) if the <string> contains no character
 * in <stop>.
 */

int find_any_index(char string[], char stop[]) {
	int sIndex = 0;
	int stopIndex = 0;
	
	int tChar = string[0];

	while(tChar != '\0'){
	  int sChar = stop[stopIndex];
	  while(sChar != '\0'){
	    if(sChar == tChar){ 	
		return sIndex;	
	    }
	    stopIndex++;
	    sChar = stop[stopIndex];
	  }
	  sIndex++;
	  tChar = string[sIndex];
	  stopIndex = 0;
	}
	return NOT_FOUND ;	// placeholder
}

/*
 * Return a pointer to the first occurrence of any character in <stop>
 * in the given <string> or NULL if the <string> contains no characters
 * in <stop>.
 *****
 * YOU MAY *NOT* USE INTEGERS OR ARRAY INDEXING.
 *****
 */
char *find_any_ptr(char *string, char* stop) {
	char *point = string;
	
	while(*point != '\0'){
	  char *sPoint = stop;
	  while(*sPoint != '\0'){
	    if(*point == *sPoint) return point;
	    else sPoint++;
	  }
	  point++;
	  
	}	
	return NULL ;	// placeholder
}

/*
 * Return a pointer to the first character of the first occurrence of
 * <substr> in the given <string> or NULL if <substr> is not a substring
 * of <string>.
 * Note: An empty <substr> ("") matches *any* <string> at the <string>'s
 * start.
 *****
 * YOU MAY *NOT* USE INTEGERS OR ARRAY INDEXING.
 *****
 */
char *find_substr(char *string, char* substr) {
	char *point = string;
	if(*substr == '\0'){
	  return string;
	}

	while(*point != '\0'){
	  char *sPoint = substr;
	  if(*sPoint == *point){
	     char *tempPoint = point;

	     while(sPoint != '\0'){
	       if(*sPoint == '\0')return point;
	       else if(*sPoint != *tempPoint)break;
	       else{
		 sPoint++; 
		 tempPoint++;
	       }
 	     }
	     
	     
	  }
	  point++;
	  
	}
	
	return NULL ;	// placeholder
}
