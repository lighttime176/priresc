#include <stdio.h>
int main()
{
	int i;
	for (i=1;i<=20;i++) {
		printf("%d ",i);
		if (i%5==0) {
			printf("\n");
		}
	}
	return 0;
}
