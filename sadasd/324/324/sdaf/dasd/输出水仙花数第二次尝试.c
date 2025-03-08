#include<stdio.h>
#include<math.h>
int main()

{
	int a,b,c,x,sum;
	for (x=100;x<1000;x++)
	{
		a=x*0.01;
		b=(x*0.01-a)*10;
		c=x%10;
		sum=pow(a,3)+pow(b,3)+pow(c,3);
		if (sum==x) 
		{
			printf("%d\n",x);
		}
		
	}
	return 0;
}
