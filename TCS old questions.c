#include<stdio.h>
#include<conio.h>
//int main(){
//	int x=0,y=0,n,i,steps=0,flage=0,flago=0;
//	printf("Enter the value of n");
//	scanf("%d",&n);
//	for(i=0;i<n;i++)
//	{
//		if(i%2==0)
//		{
//			if(flage==0)
//			{
//				steps=steps+10;
//				x=x+steps;
//				flage=(flage+1)%2;
//			}
//			else{
//				steps=steps+10;
//				x=x-steps;
//				flage=(flage+1)%2;
//			}
//		}
//		else{
//			if(flago==0){
//				steps=steps+10;
//				y=y+steps;
//				flago=(flago+1)%2;
//			}
//			else{
//				steps=steps+10;
//				y=y-steps;
//				flago=(flago+1)%2;
//			}
//		}
//	}
//	printf("%d___%d",x,y);
//}

//                              TCS direction sequence question  
//int main()
//{
//	int x=0,y=0,n,i=0,steps=0;
//	printf("Enter the value of n ");
//	scanf("%d",&n);
//	for(i=0;i<n;i++)
//	{
//		steps=steps+10;
//		switch(i%5)
//		{
//			case 0: x=x+steps;
//					break;
//			case 1: y=y+steps;
//					break;
//			case 2: x=x-steps;
//					break;
//			case 3: y=y-steps;
//					break;
//			case 4: x=x+steps;
//					break;		
//		}
//	}
//	printf("%d  %d",x,y);
//}
//					TCS Jar problem
//int main()
//{
//	int i=0,n=10,sold,avail,req;
//	printf("Enter the no. of candies");
//	scanf("%d",&req);
//	if(req<1 || req>=5)
//	{
//		printf("invalid input\n");
//		printf("NUMBER OF CANDIES LEFT = %d\n",n);
//	}
//	else{
//		printf("NUMBER OF CANDIES SOLD = %d\n",req);
//		printf("NUMBER OF AVAILABLE = %d\n",(n-req));
//	}
//}


//    Trainee Problem

//int main()
//{
//	int i,j,x,a[3]={0,0,0},max=0;
//	for(i=1;i<=3;i++)
//	{
//		for(j=1;j<=3;j++)
//		{
//			printf("enter oxygen value of trainee %d for round %d\n",j,i);
//			scanf("%d",&x);
//			if(x<1 || x>100)
//			{
//				a[j-1]=a[j-1]+0;
//			}
//			else{
//				a[j-1]=a[j-1]+x;
//			}
//		}
//	}
//	for(i=1;i<=3;i++)
//	{
//		a[i-1]=a[i-1]/3;
//	}
//	max=a[0];
//	for(i=0;i<3;i++)
//	{
//		for(j=i;j<3;j++)
//		{
//			if(max<a[j]){
//				max=a[j];
//			}
//		}
//		if(max==a[i])
//		{
//			printf("Trainee Number : %d \n",i+1);
//		}
//	}
//	if(max<70)
//	{
//		printf("trainees are unfit");
//	}
//}

int main()
{
	int k=8;
	int x = 0==1 && k++;
	printf("%d  %d",x,k);
}
