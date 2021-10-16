import java.util.Scanner;
class Atm
{
public static void main(String args[])
{
Scanner sc=new Scanner(System.in);
int a,b,c,d,e,f,g,s=0,p;
a=sc.nextInt();
b=a/500;
a=a%500;
c=a/200;
a=a%200;
d=a/100;
a=a%100;
e=a/50;
a=a%50;
f=a/20;
a=a%20;
g=a/10;
a=a%10;
p=a+b+c+d+e+f+g;
s=s+p;
System.out.println("Notes required="+s);
}
}