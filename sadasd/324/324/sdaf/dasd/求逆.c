#include<stdio.h>
int main()
{
	int x,a,t=0;
	printf("请输入一个数");
	scanf("%d",&x);
	do {
		a=x%10;
		t=t*10+a;
		x/=10;
		
	} while(x!=0);
	printf("%d",t);
	return 0;
}
