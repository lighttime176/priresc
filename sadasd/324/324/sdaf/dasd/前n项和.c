#include <stdio.h>
int main()
{
	int i;
	double sum=0.0;
	int n;
	scanf("%d",&n);
	n=10;
	for (i=1;i<=n;i++)	{
    	sum+=1.0/i;
	}
	print("%f",sum);
	return 0;
}
