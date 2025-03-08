#include <stdio.h>
int main()
{
	int j,i,a;
	for (j=1;j<=4;j++)
	for (i=1;i<=5;i++)
	{
		a=j*i;
		printf("%5d",a);
		if (i%5==0)
		{
			printf("\n");
		}
	}
	printf("\n");
	return 0;
}
