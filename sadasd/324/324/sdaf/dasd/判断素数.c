#include <stdio.h>
int main()
{
	int x;
	int i=0;
	int a=1;
	printf("������һ����"); 
	scanf("%d",&x);
	
	for (i=2;x>i;i++) {	if (x%i==0) {	a=0;break;
	}
	}
	if (a==0) {	printf("������");}
	else {	printf("��������");

	}
	return 0;
}
