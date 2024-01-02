#include<stdio.h>
#include<string.h>
int main()
{
	char a[1000];
	scanf("%s",a);
	int cnt=0;
	for(int i=0;a[i]!='\0';i++)
	{
		cnt++;
	}
	printf("total word of string:%d\n",cnt);
}