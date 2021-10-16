import java.util.Scanner;
class Monkey
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int B,b,p;
int Mon=20;
b=12;
p=12;
int M1=3;
int M2=4;
int L1=b/M1;
int L2=p/M2;
int A=L1+L2;
int S=Mon-A;
System.out.println("Total Monkeys left="+S);
}
}