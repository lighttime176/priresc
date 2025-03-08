#include<stdio.h>
int main()
{

	int isprime;
	int a[100];
	a[0]=1;
	int i;
	for (i=1;i<100;i++) {
		a[i]=i;
    	
	}
	
	for (i=2;i<100;i++) {
		
		if (a[i]%i==0) {
			isprime=1;
		} else {
			isprime=0;
		}
		if (isprime==0) {
			printf("%d\n",a[i]);
		}
	}
	return 0;
	
}
