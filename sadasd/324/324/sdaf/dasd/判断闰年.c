#include <stdio.h>
int main()
{
	int a,b,c,d;
	printf("���������\n");
	scanf("%d",&b);
	a=b%4;
	if (a=0) { 
		c=b%100;
		if (c>0) {
				d=b%400;
				if (d=0) {
						printf("��һ�겻������");
				}
		
              }
       }
	else {printf("��һ��������");
	}
	return 0;
}
