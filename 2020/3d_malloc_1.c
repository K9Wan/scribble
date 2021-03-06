#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int x = 8, y = 7, z = 9;
  int *** a = malloc(sizeof *a * x + sizeof **a * x * y + sizeof ***a * x * y * z);
  a[0] = (void *)(a + x);
  for(int i=1; i<x; i++)
  {
    a[i] = a[i-1] + y;
  }
  a[0][0] = (void *)(a[0] + x*y);
  for(int i=1; i<x; i++)
  {
    a[i][0] = a[i-1][0] + z;
  }
  for(int i=0; i<x; i++)
  {
    for(int j=1; j<y; j++)
    {
      a[i][j] = a[i][j-1] + x*z;
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
