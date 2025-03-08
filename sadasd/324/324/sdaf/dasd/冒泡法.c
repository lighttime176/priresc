#include <stdio.h>
int main()
{

	int number[5];
	int x;
	int i;
	int j,t;
	for (i=0;i<5;i++) {	scanf("%d",&number[i]);
	}
	printf("\n");
	for (j=0;j<4;j++) 
	for (i=0;i<4-j;i++)
	if (number[i]>number[i+1]) {	t=number[i];number[i]=number[i+1];number[i+1]=t;
	}
	for (i=0;i<5;i++) {	printf("%d ",number[i]);
	}
	
	
	return 0;
}
