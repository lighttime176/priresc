#include<stdio.h>
int main()
{
	int i,n;
	printf("������һ����");
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
		printf("��������");
	}
	else 
	{
		printf("������");
	}
	return 0;
}
