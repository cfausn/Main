#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

typedef enum {false, true} bool;
#define MAXLINESIZE 20   /* maximum input line size */


// Do NOT modify the following functions declarations or the number or type of parameters below:
void julius(char string[]);
int readline(char s[], int lim);

int main() {
	// ADD YOUR CODE BELOW
	// Declare any variables, including arrays you need here:
	int num = 1;
	
	char theline[MAXLINESIZE+1];

// BEGIN OF SIMPLE TEST
// Consider the following statements as way to get started
// Comment them out once you get julius working
//	char testline[MAXLINESIZE+1] = "Hello!\n";
//	julius(testline);
//	printf("%s\n", testline);  // outputs the enciphered line and adds back the newline
// END OF TEST


	// General instruction:
	// Read lines from standard input until EOF is encountered.
	// Note: (readline shall discard the newline character and properly terminate the
	//  string holding the line).	
	while(num != 0){
	  
	  num = readline(theline, MAXLINESIZE);
	  julius(theline);
	  printf("%s\n",theline);
	  char theline[MAXLINESIZE+1];
	}
		// Upon receiving a line, call julius with the string to encipher the text
		// Print out the resulting string as a separate line to standard output


	return 0 ;
}

bool is_end(int ch){
	return (ch == '\n') || (ch == EOF);
}


/* readline: 
 *	Read a line of limited size lim into s, 
 *	Return 0 if EOF was encountered, 1 otherwise. 
 *	Terminate with a null character. Discard the newline character. 
 */
int readline( char s[], int lim ) {
	int i = 0;
	int counter;
	// ADD YOUR CODE BELOW
	int ch;
	ch = getchar();
	
	while(!(is_end(ch)) || (i > lim)){
	  
	  s[i] = ch; 
	  ch = getchar(); 
	  i++;
	}
        
	
	s[i] = '\0';
	
	if(ch == EOF){
	  i = 0;
	}
	else { i = 1;}
	return i;
}

/* 
 * julius: 
 *	Perform the rotation encipher on the characters in the string
 * 	passed in as a character array.
 */
void julius(char string[]) 
        
{
	// Loop through the array, substituting characters
	// as per the algorithm, until the end of string.
	// Ignore any character not in the table (e.g. spaces)

	// ADD YOUR CODE BELOW
	int i;
	for(i = 0; !(string[i] == EOF); ++i){
	  
	  if(string[i] >= 80){
	    string[i] = string[i] - 47;	
	  }
	  else if(string[i] < 80 && string[i] >= 33){
	    string[i] = string[i] + 47;
	  }
	}

	return ;
}
