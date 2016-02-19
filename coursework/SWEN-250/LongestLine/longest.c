#include <stdlib.h>
#include <stdio.h>

#define MAXLINE 80   /* maximum input line size */

/* function declarations */
int readline( char line[], int max );
void copy( char to[], char from[] );

/* print longest input line */

int main()
{
	int len;	       	   /* current line length */
	char line[MAXLINE];    /* current input line */
	char prevLine[MAXLINE];
	int prevLen = 0;

	while ( (len = readline( line, MAXLINE )) > 0 ) {
		if(len > prevLen){
		   prevLen = len;
		   copy(prevLine,line);
		}
		}
	printf("\n%s\n",prevLine);
	return 0;
}

/* readline: read a line into s, return length */
int readline( char s[], int lim )
{
    int i = 0;
    int ch;
    for(ch = getchar(); ch!= '\n' && ch != EOF; ch = getchar()){
	if(i < lim){
	  s[i++] = ch;
	}
    }
    s[i] = '\0'; 
 
    return i;
}

/* copy: copy 'from' into 'to'; assume to is big enough */
void copy( char to[], char from[] )
{
	int i;
	for(i = 0; to[i] = from[i]; i++);
	
}



