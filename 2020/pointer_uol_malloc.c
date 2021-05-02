#include <stdio.h>
#include <stdlib.h>

typedef struct Unordered_pointer_list_{
    void ** arr;
    size_t size;
    int max;
    int cnt;
}upl;

void init(upl * list, int max)
{
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

void terminate(upl * list)
{
    free(list->arr);
    list->max = 0;
    list->cnt = 0;
}

void insert(upl * list, void * data)
{
    if(list->cnt >= list->max)
    {
        return;
    }
    list->arr[list->cnt] = data;
    list->cnt++;
    return;
}

void * delete_index(upl * list, int index)
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

static void print(upl * list)
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

int find(upl * list, void * data)
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

void update_index(upl * list, int index, void * data);

void * my_malloc(upl * list, size_t size)
{
    void * p = malloc(size);
    if(!p)  //prevent inserting NULL to list
    {
        fprintf(stderr, "allocation failed.\n");
        exit(EXIT_FAILURE);
    }
    insert(list, p);
    return p;
}

int my_free(upl * list, void * p)
{
    if(p == NULL)
    {
        return 1;
    }
    void * d = delete_index(list, find(list, p));
    if(d == NULL)   // pointer p not found
    {
        return 1;
    }
    free(p);
    return 0;
}

int my_free2(upl * list, void ** p)
{
    if(*p == NULL)
    {
        return 1;
    }
    void * d = delete_index(list, find(list, *p));
    if(d == NULL)   // pointer p not found
    {
        return 1;
    }
    free(*p);
    *p = NULL;
    return 0;
}

void free_all(upl * list)
{
    int cnt = list->cnt;
    for(int i=0; i<cnt; i++)
    {
        free(delete_index(list, 0));
    }
}

int main(void)
{
    upl * l = malloc(sizeof *l);
    init(l, 50);
/*/
    char a, b, c, d, e, f;
    char* arr[] = {&a, &b, &c, &d, &e, &f};
    
    insert(l, arr[1]);
    insert(l, arr[3]);
    insert(l, arr[5]);
    insert(l, arr[2]);

    print(l);

    char * pd = &d;
    printf("%p\n", delete_index(l, find(l, pd)));
    print(l);
    printf("%p\n", delete_index(l, 0));
    print(l);
/*/
    int * a = my_malloc(l, 3*sizeof *a);
    char ** c = my_malloc(l, sizeof *c);
    upl ** lp = my_malloc(l, sizeof *lp);
    float * f = my_malloc(l, sizeof *f);
    *f = 3.2;
    a[0] = 5;
    a[1] = 3;
    a[2] = 2;
    printf("%i %i\n", a[2], a[0]);
    double d = 3.1416;
    double * pd = &d;
    print(l);
    printf("try freeing a: code %i\n", my_free(l, a));
    print(l);
    printf("try freeing pd: code %i\n", my_free(l, pd));
    print(l);
    printf("try freeing c: code %i\n", my_free2(l, (void **)&c));
    printf("%i\n", c == NULL);
    print(l);
    free_all(l);
    print(l);

    terminate(l);
    free(l);

    return 0;
}
