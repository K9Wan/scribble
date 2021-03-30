#include <stdlib.h>
#include <stdio.h>

typedef struct node_ {
	int n;
	struct node_ * l;
	struct node_ * r;
}node, *pNode;

pNode add(pNode root, int n, int (*cmp)(int, int))
{
	pNode new = malloc(sizeof *new);
	new->n = n;
	new->l = NULL;
	new->r = NULL;

	if(!root)
	{
		return new;
	}

	if(cmp(n, root->n)<0)
	{
		root->l = add(root->l, n, cmp);
	}
	else
	{
		root->r = add(root->r, n, cmp);
	}
	
	return root;
}

void p(pNode root)
{
	if(root)
	{
		p(root->l);
		printf("%i ", root->n);
		p(root->r);
	}
}

void p2(pNode root, int *a)
{
    // don't do this
    static int i;
	if(root)
	{
		p2(root->l, a);
        a[i++] = root->n;
		p2(root->r, a);
	}
}

void free_tree(pNode root)
{
	if(root)
	{
		free_tree(root->l);
		free_tree(root->r);
		free(root);
	}
}

int cmp(int a, int b)
{
    return (a>b)-(a<b);
}

int cmp1(int a, int b)
{
    return cmp(a/10, b/10);
}

int cmp2(int a, int b)
{
    return cmp(a%10, b%10);
}

void printIntArr(int * a, int n)
{
    for(int i=0; i<n; i++)
    {
        printf("%d ", a[i]);
    }
    putchar(10);
}

int main(void)
{
	int a[] = {41, 93, 12, 9, 89, 48, 82, 87, 62, 1, 4, 13, 5, 87, 48};
	int n = sizeof a / sizeof a[0];
	pNode t = NULL;
	for(int i=0; i<n; i++)
	{
		t = add(t, a[i],&cmp2);
	}

	p2(t, a);
    printIntArr(a, n);
    t = 0;
	for(int i=0; i<n; i++)
	{
		t = add(t, a[i],&cmp1);
	}

	p(t);
	
	free_tree(t);

	return 0;
}
