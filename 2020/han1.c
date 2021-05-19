#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  char h[4];
  char u8[4];
  int u;
  int c;
  union {
    char map[3];
    struct {
      char x;
      char y;
      char z;
    };
  };
} han;

int main(void)
{
  int x = 19, y = 21, z = 28;
  han *** a = malloc(sizeof *a * x + sizeof **a * x * y + sizeof ***a * x * y * z);
  if(!a)
  {
    fprintf(stderr,"malloc failed\n");
    exit(EXIT_FAILURE);
  }
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
        a[i][j][k].x = i;
        a[i][j][k].y = j;
        a[i][j][k].z = k;
      }
    }
  }

  han * b = a[0][0];

  for(int i=0; i<x*y*z; i++)
  {
      b[i].u = 0xAC00+i;
  }
  
  for(int i=0; i<x; i++)
  {
    for(int j=0; j<y; j++)
    {
      for(int k=0; k<z; k++)
      {
        printf("%5x", a[i][j][k].u);
      }
      putchar(10);
    }
    putchar(10);
  }
  
  free(a);
  
  return 0;
}
