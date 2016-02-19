/*
 * Implementation of functions that filter values in strings.
 *****
 * YOU MAY NOT USE ANY FUNCTIONS FROM <string.h> OTHER THAN
 * strcpy() and strlen()
 *****
 */

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "filter.h"

#define NUL ('\0')

/*
 * YOU MAY FIND THIS FUNCTION USEFUL.
 * Return true if and only if character <c> is in string <s>.
 */
static bool includes(char c, char *s) {
	while( *s && c != *s ) {
		s++ ;
	}
	return c == *s ;
}

/*
 * YOU MAY ALSO FIND THIS FUNCTION USEFUL.
 * Return true if and only if string <pre> is a prefix of string <s>.
 */
static bool prefix(char *s, char *pre) {
	while( *pre && *s == *pre ) {
		s++ ;
		pre++ ;
	}
	return *pre == NUL ;
}

/*
 * Copy <string> to <result> while removing all occurrences of <ch>.
 */
void filter_ch_index(char string[], char result[], char ch) {
	int i = 0;
	int index = 0;
	int cha;
	cha = string[i];

	while(cha != '\0'){
	  if(cha != ch){
	    result[index] = cha;
	    index++;
	  }
	 
	  cha = string[++i];

	}
	result[index++] = '\0';
}	

/*
 * Return a pointer to a string that is a copy of <string> with
 * all occurrences of <ch> removed. The returned string must occupy
 * the least possible dynamically allocated space.
 *****
 * YOU MAY *NOT* USE INTEGERS OR ARRAY INDEXING.
 *****
 */
char *filter_ch_ptr(char *string, char ch) {
	char *copy;
	char *hardCopy;

	copy = malloc(strlen(string) + 1);
	hardCopy = malloc(strlen(string) + 1);
	while(*string != '\0'){
	  if(*string != ch){
	    *copy = *string;
	    strcpy(hardCopy,hardCopy);
	    strcpy(hardCopy + strlen(hardCopy), copy);
	    copy++;
	  }
	  
	  string++;
	}
	
	return hardCopy; // placeholder
}

/*
 * Copy <string> to <result> while removing all occurrences of
 * any characters in <remove>.
 */
void filter_any_index(char string[], char result[], char remove[]) {
	int sIndex = 0;
	int stopIndex = 0;
	int add = 0;
	int addIndex = 0;
	
	char temp[strlen(string)];
	int tChar = string[0];
	
	while(tChar != '\0'){
	  int sChar = remove[stopIndex];
	  while(sChar != '\0'){
	    if(sChar == tChar){ add = 1;}
	    sChar = remove[++stopIndex];
	  }
	  if(add == 0) result[addIndex++] = tChar;
	  tChar = string[++sIndex]; 
	  add = 0;
	  stopIndex = 0;
	}
	result[addIndex] = '\0';
}

/*
 * Return a pointer to a copy of <string> after removing all
 * occurrrences of any characters in <remove>.
 * The returned string must occupy the least possible dynamically
 * allocated space.
 *****
 * YOU MAY *NOT* USE INTEGERS OR ARRAY INDEXING.
 *****
 */
char *filter_any_ptr(char *string, char* remove){
	char *copy;
	char *hardCopy;
	bool tf = false;
	char *remCopy;
	
	remCopy = malloc(strlen(string) + 1);
	copy = malloc(strlen(string) + 1);
	hardCopy = malloc(strlen(string) + 1);

	strcpy(remCopy, remove);
	while(*string != '\0'){
	  while(*remCopy != '\0'){
	    if(*string == *remCopy){
	      tf = true;
	    }
	    remCopy++;
	  }
	  if(tf == false){
	    *copy = *string;
	    strcpy(hardCopy,hardCopy);
	    strcpy(hardCopy + strlen(hardCopy), copy);
	    copy++;

	  }
	  remCopy = malloc(strlen(string) + 1);
	  strcpy(remCopy,remove);
	  string++;
	  tf = false;
	}
	
	return hardCopy; // placeholder

}

/*
 * Return a pointer to a copy of <string> after removing all
 * occurrrences of the substring <substr>.
 * The returned string must occupy the least possible dynamically
 * allocated space.
 *****
 * YOU MAY *NOT* USE ARRAY INDEXING.
 *****
 */
char *filter_substr(char *string, char* substr) {

	char *copy;
	char *hardCopy;
	bool tf = false;
	char *subCopy;
	
	subCopy = malloc(strlen(substr) + 1);
	strcpy(subCopy, substr);	
	copy = malloc(strlen(string) + 1);
	hardCopy = malloc(strlen(string) + 1);

	
	
	if(*substr == '\0') return string;
	
	char *point = string;
	while(*point != '\0'){
	  char *sPoint = substr;
	  if(*sPoint == *point){
	    char *tempPoint = point;
	    while(sPoint != '\0'){
	      if(*sPoint == '\0'){tf = true;point += (strlen(substr) - 1); break;}
	      else if(*sPoint != *tempPoint) break;
	      else{sPoint++; tempPoint++;}
	    }
	  }
	  if(tf == false){
	    *copy = *point;
	    strcpy(hardCopy,hardCopy);
	    strcpy(hardCopy + strlen(hardCopy), copy);
	    copy++;

	  }
	  
	  tf = false;
	
	point++;
	}

	return hardCopy;	
     }
      

