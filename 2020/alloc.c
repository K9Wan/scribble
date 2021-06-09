#include <stdio.h>
#include <stdlib.h>
#include "alloc.h"

typedef struct Unordered_pointer_list_{
    void ** arr;
    size_t size;
    int max;
    int cnt;
}upl;

static upl * list;

void init(int max)
{
    if(!list)
    {
        list = malloc(sizeof *list);
    }
    size_t size = sizeof (void *);
    list->arr = calloc(max, size);
    if(!list->arr)
    {
        fprintf(stderr, "allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    list->size = size;
    list->max = max;
    list->cnt = 0;
}

void terminate(void)
{
    free(list->arr);
    list->max = 0;
    list->cnt = 0;
    free(list);
    list = NULL;
}

static void insert(void * data)
{
    if(list->cnt >= list->max)
    {
        return;
    }
    list->arr[list->cnt] = data;
    list->cnt++;
    return;
}

static void * delete_index(int index)
{
    void * deleted = 0;
    if(index<0 || index>=list->cnt)
    {
        return NULL;
    }
    if(index == list->cnt-1)
    {
        deleted = list->arr[list->cnt];         //return arr[cnt--]
        list->cnt--;
        return deleted;
    }
    deleted = list->arr[index];
    list->arr[index] = list->arr[list->cnt-1];  //--cnt
    list->cnt--;
    return deleted;
}

static void print(void)
{
    if(!list->cnt)
    {
        puts("printed empty list");
    }
    for(int i=0;i<list->cnt;i++)
    {
        printf("%p ", list->arr[i]);
    }
    putchar(10);
}

static int find(void * data)
{
    for(int i=0; i<list->cnt; i++)
    {
        if(list->arr[i] == data)
        {
            //printf("found: %p\n", data);
            return i;
        }
    }
    return -1;
}

//void update_index(int index, void * data);

void * alloc(size_t size)
{
    void * p = malloc(size);
    if(!p)  //prevent inserting NULL to list
    {
        fprintf(stderr, "allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    insert(p);
    return p;
}

int mfree(void * p)
{
    if(p == NULL)
    {
        return 1;
    }
    void * d = delete_index(find(p));
    if(d == NULL)   // pointer p not found
    {
        return 1;
    }
    free(p);
    return 0;
}

int my_free2(void ** p)
{
    if(*p == NULL)
    {
        return 1;
    }
    void * d = delete_index(find(*p));
    if(d == NULL)   // pointer p not found
    {
        return 1;
    }
    free(*p);
    *p = NULL;
    return 0;
}

void free_all(void)
{
    int cnt = list->cnt;
    for(int i=0; i<cnt; i++)
    {
        free(delete_index(0));
    }
}
/*/
int main(void)
{
    init(50);

    int * a = alloc(3*sizeof *a);
    char ** c = alloc(sizeof *c);
    upl ** lp = alloc(sizeof *lp);
    float * f = alloc(sizeof *f);
    *f = 3.2;
    a[0] = 5;
    a[1] = 3;
    a[2] = 2;
    printf("%i %i\n", a[2], a[0]);
    double d = 3.1416;
    double * pd = &d;
    print();
    printf("try freeing a: code %i\n", mfree(a));
    print();
    printf("try freeing pd: code %i\n", mfree(pd));
    print();
    printf("try freeing c: code %i\n", my_free2((void **)&c));
    printf("%i\n", c == NULL);
    print();
    free_all();
    print();

    terminate();

    return 0;
}
//*/
