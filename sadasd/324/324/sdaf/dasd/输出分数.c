#include<stdio.h>
int main()
{
	char ch;
	printf("请输入A到D的大写字符");
	scanf("%c",&ch);
	if (ch>='A'&&ch<='D') {
		switch (ch) {
			case 'A':printf("85分以上");break;
			case 'B':printf("70~84分之间");break;
			case 'C':printf("60~69分之间");break;
			case 'D':printf("60分以下");break;
		} 
	} else {
		printf("数据有误");
	}
	return 0;
}
