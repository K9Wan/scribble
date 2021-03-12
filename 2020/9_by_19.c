#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int h = 9, w = 19;
  int * * p = malloc(sizeof(*p) * h + sizeof(**p) * h * w);
  for(int i=0; i<h; i++)
  {
    p[i] = (char *)(p+h)+sizeof **p * i * w;
  }
  
  for(int i=0;i<h;i++)
  {
    for(int j=0;j<w;j++)
    {
      p[i][j] = (i+1)*(j+1);
    }
  }
  for(int i=0;i<h;i++)
  {
    for(int j=0;j<w;j++)
    {
      printf("%4i", p[i][j]);
    }
    putchar(10);
  }
  
  free(p);
  
  return 0;
}
