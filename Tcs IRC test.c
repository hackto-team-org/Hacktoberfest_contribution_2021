#include <stdio.h>

int main(){
	char a[100],b[100],i;
	printf("Enter the string for encoding");
	gets(a);
	printf("Enter the string for decoding");
	gets(b);
	for(i=0;a[i]!='\0';i++)
	{
		if(a[i]>=65 && a[i]<=90 || a[i]>=97 && a[i]<=122)
		{	
			a[i]=a[i]+5;
			printf("%c ",a[i]);
		}
		else if(a[i]==' ' || a[i]=='.' || a[i]==',')
		{
			printf("%c ",a[i]);
		}
		else
		{
			printf("Invalid Input");
			break;
		}
	}
	printf("\n");
	for(i=0;b[i]!='\0';i++)
	{
		if(b[i]>=65 && b[i]<=90 || b[i]>=97 && b[i]<=122)
		{	
			b[i]=b[i]-5;
			printf("%c ",b[i]);
		}
		else if(b[i]==' ' || b[i]=='.' || b[i]==',')
		{
			printf("%c ",b[i]);
		}
		else
		{
			printf("Invalid Input");
			break;
		}
	}
}
