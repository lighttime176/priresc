#include<stdio.h>
int main()
{
	int a[3][4]={{1,2,3,4},{12,23,34,45},{5,6,7,8}};
	int i,j,row,colum,max;
	max=a[0][0];
	for (i=0;i<3;i++)
	for (j=0;j<4;j++) {
		if (a[i][j]>max) {
			max=a[i][j];
			row=i;colum=j;
		}
	/*	if (a[i][j]>a[i+1][j+1]) {
			max=a[i][j];
			row=i;
			colum=j;
		}
		else {
			max=a[i+1][j+1];
			row=j;
			colum=i;
		}*/
	}
	printf("max is %d\n",max);
	printf("row=%d\ncolum=%d",row,colum);
	return 0;
}
