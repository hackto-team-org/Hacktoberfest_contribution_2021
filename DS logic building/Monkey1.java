import java.util.Scanner;
class Monkey1
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int b,p;
int Mon=sc.nextInt();
b=sc.nextInt();
p=sc.nextInt();
int M1=sc.nextInt();
int M2=sc.nextInt();
int L1=b/M1;
int L2=p/M2;
int A=L1+L2;
int S=Mon-A;
int E=b%M1+p%M2;
if(E>0)
{
S=S-E;
}
System.out.println("Extra Bananas and peanuts left="+S);
}
}

//error