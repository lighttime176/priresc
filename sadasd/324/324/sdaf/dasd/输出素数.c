#include<stdio.h>
int main()
{
	int n,i,isprime;
	printf("请输入一个数");
	scanf("%d",&n);
	for (i=2;i<n;i++)
	{
		if (n%i==0)
		{
			isprime=1;
		}
		else
		{
			isprime=0;
		}
	 } 
	 if (isprime==1) 
	 {
	 	printf("不是素数"); 
	 }
	 else
	 {
	 	printf("是素数");
	 }
	 return 0;
}
