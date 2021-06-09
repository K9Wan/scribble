#include <stdio.h>
#include <stdlib.h>
#include "alloc.h"

int main(void)
{
    init(20);

    int m, n;
    m = n = 0x10;
    int **p = alloc(sizeof *p * m + sizeof **p * m * n);
    for(int i=0; i<m; i++)
    {
        p[i] = (int *)(p+m) + i * n;
    }

    for(int i=0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
            p[i][j] = (i+j) % 16;
        }
    }
    for(int i=0; i<m; i++)
    {
        for(int j=0; j<n; j++)
        {
            printf("%2X", p[i][j]);
        }
        putchar(10);
    }
    putchar(10);

    mfree(p);


    terminate();

    return 0;
}
