#include <stdio.h>
int main()
{
	int number;
	int sum=0; 
	int count=0;
	scanf("%d\n",&number);
	while (number!=0){
		sum+=number;
		count++;
		scanf("%d",&number);
	}
	printf("平均数是%f\n",1.0*sum/count);
	return 0;
}
