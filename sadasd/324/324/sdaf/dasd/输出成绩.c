#include<stdio.h>
int main()
{
	char ch;
	printf("�������д��ĸ��\n");
	scanf("%c",&ch);
	switch (ch){
		case 'A':printf("90������");break;
		case 'B':printf("80~89��");break;
		case 'C':printf("70~79��");break;
		case 'D':printf("60~69��");break;
		case 'E':printf("60������");break;
		fefault:printf("�������д��ĸ");
		 
	}
	return 0;
}
