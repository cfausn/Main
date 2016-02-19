#include <stdlib.h>
#include <stdio.h>

int main(){
  puts("Fahrenheit-Celsius");
  int far = 0;
  float cel = 0;
  int intCel = 0;

  
  while(far <= 300){ 
    cel = (far-32);
    intCel = (int)((cel * 5)/9);
    printf("    %-7d%-7d\n",far,intCel);
    far += 20; 
  }
  return 0;
}
