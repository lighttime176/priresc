#include<stdio.h>
int main()
{
	int n,i,isprime;
	printf("������һ����");
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
	 	printf("��������"); 
	 }
	 else
	 {
	 	printf("������");
	 }
	 return 0;
}
