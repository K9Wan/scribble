#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int x = 4, y = 7, z = 9, w = 6;
  double **** a = malloc(sizeof * a * x + sizeof * * a * x * y + sizeof * * * a * x * y * z + sizeof * * * * a * x * y * z * w);
  for(int i=0; i<x; i++)
  {
    a[i] = (void *)((char *)(a+x) + sizeof **a*i*y);
    for(int j=0; j<y; j++)
    {
      a[i][j] = (void *)((char *)(a[0] + x*y) + sizeof ***a*(i*y*z + j*z));
      for(int k=0; k<z; k++)
      {
        a[i][j][k] = (void *)((char *)(a[0][0] + x*y*z) + sizeof ****a*(i*y*z*w + j*z*w + k*w));
      }
    }
  }

  for(int i=0; i<x; i++)
  {
    for(int j=0; j<y; j++)
    {
      for(int k=0; k<z; k++)
      {
        for(int l=0; l<w; l++)
        {
          a[i][j][k][l] = (i+1)*1000+(j+1)*100+(k+1)*10+(l+1);
        }
      }
    }
  }
  
  for(int i=0; i<x; i++)
  {
    for(int j=0; j<y; j++)
    {
      for(int k=0; k<z; k++)
      {
        for(int l=0; l<w; l++)
        {
          printf("%5.0lf", a[i][j][k][l]);
        }
        putchar(10);
      }
      putchar(10);
    }
    putchar(10);
  }

  free(a);
  
  return 0;
}
