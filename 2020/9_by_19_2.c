#include <stdio.h>
#include <stdlib.h>

void t(void * ptr)
{
  printf("%i\n", (unsigned short)ptr);
}

int main(void)
{
  int x = 9, y = 9, z = 9;
  int *** a = malloc(sizeof *a * x + sizeof **a * x * y + sizeof ***a * x * y * z);
  t(a);
  a[0] = (void *)(a + x);
  t(a[0]);

  for(int i=1; i<x; i++)
  {
    a[i] = a[i-1] + y;
    t(a[i]);
  }
  a[0][0] = (void *)(a[0] + x*y);
  printf("%d %d ", 0, 0);
  t(a[0][0]);
  for(int i=1; i<x; i++)
  {
    a[i][0] = a[i-1][0] + z;
    printf("%d %d ", i, 0);
    t(a[i][0]);
  }
  for(int i=0; i<x; i++)
  {
    for(int j=1; j<y; j++)
    {
      a[i][j] = a[i][j-1] + x*z;
      printf("%d %d ", i, j);
      t(a[i][j]);
    }
  }

  for(int i=0; i<x; i++)
  {
    for(int j=0; j<y; j++)
    {
      for(int k=0; k<z; k++)
      {
        a[i][j][k] = (i+1)*100+(j+1)*10+(k+1);
      }
    }
  }
  
  for(int i=0; i<x; i++)
  {
    for(int j=0; j<y; j++)
    {
      for(int k=0; k<z; k++)
      {
        printf("%4i", a[i][j][k]);
      }
      putchar(10);
    }
    putchar(10);
  }
  

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
