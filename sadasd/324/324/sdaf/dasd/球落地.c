#include<stdio.h>
int main()
{
	int x=0;
	double i;
	for (i=100;i!=0.0;i/=2.0,x++)
	{
		//i/=2.0;
		if (x==10)
		{
			printf("��ʮ��%f\n",i);
		 } 
		 if (x==11) 
		 {
		 	printf("��ʮһ��%f\n",i);break;
		 }
		
	}
	return 0;
}
