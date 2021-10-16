import java.util.Scanner;
class Money1
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int B,b,p,R,R1;
int Mon=20;
b=sc.nextInt();
p=sc.nextInt();
int M1=3;
int M2=4;
int L1=b/M1;
R=b%10;
int L2=p/M2;
R1=p%10;
int A=L1+L2;
int S=Mon-A;
System.out.println("Total Monkeys left="+S);
int E=R+R1;
System.out.println("Extra Bananas and peanuts left="+E);
}
}