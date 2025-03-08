#include<stdio.h>
int main()
{
	int i,n;
	printf("请输入一个数");
	scanf("%d",&n);
	for (i=2;i<n;i++) 
	{
		if (n%i==0)
		{
			break;
		}
	}
	if (i<n)
	{
		printf("不是素数");
	}
	else 
	{
		printf("是素数");
	}
	return 0;
}
