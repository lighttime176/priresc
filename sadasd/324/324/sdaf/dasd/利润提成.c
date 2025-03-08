#include<stdio.h>
int main()
{
	int a,i,b,x;
	printf("«Î ‰»Î¿˚»Û");
	scanf("%d",&i);
	if (x<100000) {
		a=1;
	} else if (x<200000) {
		a=2;
	} else if (x<400000) {
		a=3;
	} else if (x<600000) {
		a=4;
	} else if (x<1000000) {
		a=5;
	} else if (x>1000000) {
		a=6;
	}
	switch (a) {
		case 1:b=i*0.1+i;break;
		case 2:b=i*0.1+i+100000*0.075;break;
		case 3:b=i*0.1+i+100000*0.075+200000*0.05;break;
		case 4:b=i*0.1+i+100000*0.075+200000*0.05;break; 
	}
	printf("%d",b);
	return 0;
}
