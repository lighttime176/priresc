#include <stdio.h>
int main()
{
	int x;
	int i=0;
	int a=1;
	printf("请输入一个数"); 
	scanf("%d",&x);
	
	for (i=2;x>i;i++) {	if (x%i==0) {	a=0;break;
	}
	}
	if (a==0) {	printf("是素数");}
	else {	printf("不是素数");

	}
	return 0;
}
