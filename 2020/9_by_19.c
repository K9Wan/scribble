#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int h = 9, w = 19;
  int * * p = malloc(sizeof(*p) * h + sizeof(**p) * h * w);

  p[0] = (void *)(p+h);
  for(int i=1; i<h; i++)
  {
    p[i] = p[i-1] + w;
  }// from comment on https://panty.run/malloc/ by 은하

  /*/
  for(int i=0; i<h; i++)
  {
    p[i] = (void *)((char *)(p+h)+sizeof **p * i * w);
  }// my original
  /*/

  /*/
  for(int i=0; i<h; i++)
  {
    p[i] = (int *)(p+h)+ i * w;
  }// my old original: short but hardcoded typecasting
  /*/
  
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
