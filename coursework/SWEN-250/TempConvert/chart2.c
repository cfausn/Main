#include <stdlib.h>
#include <stdio.h>

int main(){
  puts("Fahrenheit-Celsius");
  int far = 0;
  float cel = 0;
  float newCel = 0;

  
  while(far <= 300){ 
    cel = (far-32);
    newCel = ((cel * 5)/9);
    printf("%5d%12.1f\n",far,newCel);
    far += 20; 
  }
  return 0;
}
