#include<stdio.h>
int main()
{
	int a,b,c,d;
	scanf("%d,%d,%d",&a,&b,&c);
	//(a>b)?d=a:(d=b);
	//(a>c)?d=a:(d=c);
	//(b>c)?d=b:(d=c);
	d=(a>b)?a:b;
	d=(a>c)?a:c;
	d=(b>c)?b:c; 
	printf("%d",d);
	return 0;
}
