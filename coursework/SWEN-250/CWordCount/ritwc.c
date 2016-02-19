#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

#define FALSE (0)
#define TRUE  (1)

int main() {
	int tot_chars = 0 ;	/* total characters */
	int tot_lines = 0 ;	/* total lines */
	int tot_words = 0 ;	/* total words */

	/* REPLACE WITH ADDITIONAL VARIABLE DECLARATIONS YOU NEED */
	int nChar;
	/* REPLACE WITH THE CODE FOR WORD COUNT */
	
	while((nChar = getchar()) != EOF){
	  tot_chars++;
	  if(isspace(nChar)) {
	    tot_words++;
	    }
	  if(nChar == '\n'){
	    tot_lines++;
	    tot_words++;
	    }
	  }
	printf(" %i %i %i",tot_lines,tot_words,tot_chars);
	return 0;
}
