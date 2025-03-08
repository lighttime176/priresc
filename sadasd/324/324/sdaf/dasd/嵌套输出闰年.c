#include<stdio.h>
int main()
{
	int year,leap;
	printf("请输入一个年份");
	scanf("%d",&year);
	if (year%4==0) {
		if (year%100==0) {
			leap=1;
		} else {
			if (year%400==0) {
				leap=1;
			}else leap=0;
		}
	}leap=0;
	if ("leap==1") {
		printf("是闰年");
	} else {
		printf("不是闰年");
	}
	return 0;
}
