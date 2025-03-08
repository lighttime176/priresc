#include<stdio.h>
int main()
{
	int i,j,a=0;
	for (i=1;i<10;i++) {
		a++;
		for (j=1;j<10;j++) {
			printf("%d*%d=%d\t",j,i,i*j);
			if (a==j) {
				printf("\n");
				break;
			}
		}
   }
	return 0;
}
