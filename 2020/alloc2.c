#include <stdio.h>
#include <stdlib.h>

typedef struct Node_{
    void * p;
    struct Node_ * next;
} node, *pNode;

static pNode head;

static void insert(void * p)
{
    if(!p)
    {
        return;
    }
    pNode new = malloc(sizeof *new);
    if(!new)
    {
        fprintf(stderr,"malloc failed");
        exit(EXIT_FAILURE);
    }
    new->p = p;
    new->next = NULL;
    if(!head)
    {
        head = new;
        return;
    }
    pNode cur = head;
    for(; cur->next; cur=cur->next);
    cur->next = new;
    return;
}

static void * delete_p(void * p)
{
    if(!p || !head)
    {
        return NULL;
    }
    pNode cur = head;
    pNode prev = NULL;
    while(cur)
    {
        if(cur->p == p)
        {
            break;
        }
        prev = cur;
        cur = cur->next;
    }
    if(!cur)
    {// p not found;
        return NULL;
    }
    if(!prev)
    {// p in head;
        head = cur->next;
        free(cur);
        return p;
    }
    prev->next = cur->next;
    free(cur);
    return p;
}

void * alloc(size_t size)
{
    void * p = malloc(size);
    if(!p)
    {
        fprintf(stderr, "allocation failed\n");
        exit(EXIT_FAILURE);
    }
    insert(p);
    return p;
}

int mfree(void *p)
{
    if(!p)
    {
        return 1;
    }
    void * d = delete_p(p);
    if(!d)
    {// p not found;
        return 1;
    }
    free(p);
    return 0;
}

void free_all(void)
{
    while(head)
    {
        pNode c = head;
        free(delete_p(c->p));
    }
}

static void print(void)
{
    pNode cur = head;
    if(!cur)
    {
        puts("empty");
    }
    while(cur)
    {
        printf("%p ", cur->p);
        cur = cur->next;
    }
    putchar(10);
}

/*/
int main(void)
{
    int * a = alloc(3*sizeof *a);
    char ** c = alloc(sizeof *c);
    pNode ** lp = alloc(sizeof *lp);
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
    printf("try freeing c: code %i\n", mfree(c));
    print();
    free_all();
    print();
    return 0;
}
//*/
