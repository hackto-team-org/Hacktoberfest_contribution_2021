import java.util.Scanner;
class Add
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int a,b,c,d,e,p;
int n=sc.nextInt();
a=n%10;
n=n/10;
b=n%10;
n=n/10;
c=n%10;
n=n/10;
d=n%10;
n=n/10;
e=n%10;
n=n/10;
p=a+c+e;
System.out.println("Add 3 nos="+p);
}
}