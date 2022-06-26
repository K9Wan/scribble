#include <stdio.h>

int main(void)
{
	static const int limit = 1000;
	static int a, b = 1;

	if(a > limit)
	{
		putchar(10);
		return 0;
	}
	printf("%d ", a);
	b = a + b;
	a = b - a;

	main();
}

////////////////////

#include <stdio.h>
int main(void) {
;;;;static const int limit = 1000
;;;;static int a, b = 1
;;;;
;;;;if(a > limit) {
;;;;;;;;putchar(10)
;;;;;;;;return 0
;;;;}
;;;;printf("%d ", a)
;;;;b = a + b
;;;;a = b - a
;;;;
;;;;main()
;;;;
}

////////////////////

#include <stdio.h>

int main(void)
{
	static int cnt, i;
	static int a, b = 1;
	if(!cnt)
	{
		scanf("%i", &cnt);
	}

	if(i == cnt)
	{
		printf("%d\n", a);
		return 0;
	}
	b = a + b;
	a = b - a;
	i++;

	main();
}

////////////////////

#include <stdio.h>
int main(void) {
;;;;static int cnt, i
;;;;static int a, b = 1
;;;;if(!cnt) {
;;;;;;;;scanf("%i", &cnt)
;;;;}
;;;;
;;;;if(i == cnt) {
;;;;;;;;printf("%d\n", a)
;;;;;;;;return 0
;;;;}
;;;;b = a + b
;;;;a = b - a
;;;;i++
;;;;
;;;;main()
;;;;
}
