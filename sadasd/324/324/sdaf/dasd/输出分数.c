#include<stdio.h>
int main()
{
	char ch;
	printf("������A��D�Ĵ�д�ַ�");
	scanf("%c",&ch);
	if (ch>='A'&&ch<='D') {
		switch (ch) {
			case 'A':printf("85������");break;
			case 'B':printf("70~84��֮��");break;
			case 'C':printf("60~69��֮��");break;
			case 'D':printf("60������");break;
		} 
	} else {
		printf("��������");
	}
	return 0;
}
