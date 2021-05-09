#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int x = 8, y = 7, z = 9;
  int *** a = malloc(sizeof *a * x + sizeof **a * x * y + sizeof ***a * x * y * z);
  for(int i=0; i<x; i++)
  {
    a[i] = (void *)((char *)(a+x) + sizeof **a*i*y);
    for(int j=0; j<y; j++)
    {
      a[i][j] = (void *)((char *)(a[0] + x*y) + sizeof ***a*(i*y*z + j*z)); // i*y*z + j*z, i*z + j*x*z both works, but will have different mapping: horizontal and vertical
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

  free(a);
  
  return 0;
}
