#include <stdio.h>
int main()
{
	int a,b,c,d;
	printf("请输入年份\n");
	scanf("%d",&b);
	a=b%4;
	if (a=0) { 
		c=b%100;
		if (c>0) {
				d=b%400;
				if (d=0) {
						printf("这一年不是闰年");
				}
		
              }
       }
	else {printf("这一年是闰年");
	}
	return 0;
}
