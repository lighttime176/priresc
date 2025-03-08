#include<stdio.h>
int main()
{
	char ch;
	printf("请输入大写字母：\n");
	scanf("%c",&ch);
	switch (ch){
		case 'A':printf("90分以上");break;
		case 'B':printf("80~89分");break;
		case 'C':printf("70~79分");break;
		case 'D':printf("60~69分");break;
		case 'E':printf("60分以下");break;
		fefault:printf("请输入大写字母");
		 
	}
	return 0;
}
