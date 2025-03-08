#include<stdio.h>
int main()
{
	int i,a,b,c,sum;
	
	for (i=100;i<1000;i++)
	{
		c=i;
		a=c%10;
		c=c/10;
		b=c%10;
		c=c/10;
		sum=a*a*a+b*b*b+i*i*i;
		if (sum=c) 
		{
			printf("%d\n",sum);
			
		}
	}
	return 0;
 } 
