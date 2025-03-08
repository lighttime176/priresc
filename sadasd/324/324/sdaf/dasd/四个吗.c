#include <stdio.h>
int main()
{
	int k1,k2,sum1=0,sum2=0;
	double k3,sum=0.0,sum3=0.0;
	
	for (k1=1;k1<=100;k1++)
	sum1+=k1;
	for (k2=1;k2<=50;k2++)
	sum2=sum2+k2*k2;
	for (k3=1.0;k3<=10;k3++)
	sum3=sum3+1.0/k3;
	sum=sum1+sum2+sum3;
	printf("%f ",sum);
	return 0;
}
