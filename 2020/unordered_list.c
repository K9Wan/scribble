#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Unordered_list_{
    void * arr;
    size_t size;
    int max;
    int cnt;
}uol;

void init(uol * list, size_t size, int max)
{
    list->arr = calloc(max, size);
    list->size = size;
    list->max = max;
    list->cnt = 0;
}

void terminate(uol * list)
{
    free(list->arr);
    list->max = 0;
    list->cnt = 0;
}

void insert(uol * list, void * data)
{
    if(list->cnt >= list->max)
    {
        return;
    }
    memcpy((char *)(list->arr)+list->size*list->cnt, data, list->size);
    list->cnt++;
    return;
}

void delete_index(uol * list, int index, void * deleted)
{
    if(index<0 || index>=list->cnt)
    {
        return;
    }
    if(index == list->cnt-1)
    {
        if(deleted) memcpy(deleted, (char *)(list->arr)+list->size*index, list->size);
        list->cnt--;
        return;
    }
    if(deleted) memcpy(deleted, (char *)(list->arr)+list->size*index, list->size);
    memcpy((char *)(list->arr)+list->size*index, (char *)(list->arr)+list->size*(list->cnt-1), list->size);
    list->cnt--;
}

void dump(uol * list)
{
    for(int i=0; i<list->cnt; i++)
    {
        for(unsigned j=0; j<list->size; j++)
        {
            printf("%i ", *((char *)(list->arr)+i*list->size+j));
        }
        putchar(10);
    }
    putchar(10);
}

int find(uol * list, void * data);

void update_index(uol * list, int index, void * data);



int main(void)
{
    uol * l = malloc(sizeof *l);
    init(l, sizeof(char), 10);

    char arr[] = {3,24,55,14,66,17,33};

    insert(l, arr+1);
    dump(l);
    insert(l, arr);
    dump(l);
    insert(l, arr+3);
    insert(l, arr+2);
    insert(l, arr+5);
    insert(l, arr+4);
    dump(l);
    delete_index(l, 2, 0);
    dump(l);
    delete_index(l, 3, 0);
    dump(l);
    delete_index(l, 0, 0);
    dump(l);
    char *p = arr;
    delete_index(l, 1, p);
    dump(l);
    printf("deleted: %i\n", *p);

    terminate(l);
    free(l);

    return 0;
}
