#include<stdio.h>
#include<math.h>
int main()
{
	int a,b;
	printf("请输入一个小于1000的数\n");
	scanf("%d",&a);
	if (a>1000) {
		
		do {
			printf("您输入的有误，请重新输入\n");
			scanf("%d",&a);
		}
		while (a>1000);
		b=sqrt(a);
		printf("%d",b);
	}
	else {
	b=sqrt(a);
	printf("%d",b);
	}
	return 0;
}
