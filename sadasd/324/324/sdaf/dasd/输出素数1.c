#include<stdio.h>
int main()
{
	int x,a;
	printf("������һ����");
	scanf("%d",&x);
	int s(int x);
	a=s(x);
	return 0;
}
int s(int x)
{
	int isprime,a;
	int i;
	for(i=2;i<x;i++) {
		a=x%i;
		if(a==0) {
			isprime=1;
			break;
		}
	}
	if(isprime==1) {
		printf("��������");
	} else {
		printf("������");
	}
	
}
