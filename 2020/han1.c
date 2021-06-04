#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  unsigned char h[4]; //strcpy-ed 
  unsigned char u8[4];
  unsigned u;
  union {
    unsigned c;
    unsigned char cp9[2];
  };
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
  han *** a = calloc(1, sizeof *a * x + sizeof **a * x * y + sizeof ***a * x * y * z);
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

  for(int i=0; i<x*y*z; i++)
  {
    unsigned u = b[i].u;
    b[i].u8[2] = (u&0x3F) | 0x80;
    u >>= 6;
    b[i].u8[1] = (u&0x3F) | 0x80;
    u >>= 6;
    b[i].u8[0] = u | 0xE0;  //(u&0x0F) & 0xE0;
  }
  
  for(int i=0; i<x; i++)
  {
    for(int j=0; j<y; j++)
    {
      for(int k=0; k<z; k++)
      {
        //printf("%5x", a[i][j][k].u);
      }
      putchar(10);
    }
    putchar(10);
  }
/*/
  a[0][0][0].cp9[1] = "가"[0];
  a[0][0][0].cp9[0] = "가"[1];
  for(int i=0; i<2; i++)
  {
    printf("%hhx ", "가"[i]);
  }
  printf("%#x\n", a[0][0][0].c);
/*/ //environment: cp949;
//*/
  for(int i=0; i<x; i++)
  {
    for(int j=0; j<y; j++)
    {
      for(int k=0; k<z; k++)
      {
        printf("%s", a[i][j][k].u8);
      }
      putchar(10);
    }
    putchar(10);
  }
//*/ //environment: utf-8
  strcpy(a[0][0][0].h, "가");
  for(int i=0; i<4; i++)
  {
    printf("%x ", a[0][0][0].h[i]);
  }
  putchar(10);
  free(a);
  
  return 0;
}
