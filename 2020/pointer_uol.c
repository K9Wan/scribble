#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    for(int i=0;i<list->cnt;i++)
    {
        printf("%p ", list->arr[i]);
    }
    putchar(10);
}

int find(upl * list, void * data);

void update_index(upl * list, int index, void * data);



int main(void)
{
    upl * l = malloc(sizeof *l);
    init(l, 50);

    char a, b, c, d, e, f;
    char* arr[] = {&a, &b, &c, &d, &e, &f};
    
    insert(l, arr[1]);
    insert(l, arr[3]);
    insert(l, arr[5]);
    insert(l, arr[2]);

    print(l);

    printf("%p\n", delete_index(l, 1));
    print(l);
    printf("%p\n", delete_index(l, 0));
    print(l);

    terminate(l);
    free(l);

    return 0;
}
