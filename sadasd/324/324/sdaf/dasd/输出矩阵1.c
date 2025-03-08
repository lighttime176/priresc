#include<stdio.h>
int main()
{
	int i,j;
	int m=0;
	for (i=1;i<=4;i++)
	for (j=1;j<=5;j++) {
		printf("%5d",i*j);
		m++;
		if (m%5==0) {
			printf("\n");
		}
	}
	return 0; 
}
