#include<stdio.h>
#include<math.h>
int main()
{
	int a,b;
	printf("������һ��С��1000����\n");
	scanf("%d",&a);
	if (a>1000) {
		
		do {
			printf("���������������������\n");
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
