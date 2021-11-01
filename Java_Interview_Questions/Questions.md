# Java Basic Interview Questions

```
1. Why is Java a platform independent language?
```
Java language was developed in such a way that it does not depend on any hardware or software due to the fact that the compiler compiles the code and then converts it to platform-independent byte code which can be run on multiple systems.
The only condition to run that byte code is for the machine to have a runtime environment (JRE) installed in it.
```
2. Why is Java not a pure object oriented language?
```
Java supports primitive data types - byte, boolean, char, short, int, float, long, and double and hence it is not a pure object-oriented language.

```
3. Pointers are used in C/ C++. Why does Java not make use of pointers?
```
Pointers are quite complicated and unsafe to use by beginner programmers. Java focuses on code simplicity, and the usage of pointers can make it challenging. Pointer utilization can also cause potential errors. Moreover, security is also compromised if pointers are used because the users can directly access memory with the help of pointers.
Thus, a certain level of abstraction is furnished by not including pointers in Java. Moreover, the usage of pointers can make the procedure of garbage collection quite slow and erroneous. Java makes use of references as these cannot be manipulated, unlike pointers.

```
4. What do you understand by an instance variable and a local variable?
```
Instance variables are those variables that are accessible by all the methods in the class. They are declared outside the methods and inside the class. These variables describe the properties of an object and remain bound to it at any cost.

All the objects of the class will have their copy of the variables for utilization. If any modification is done on these variables, then only that instance will be impacted by it, and all other class instances continue to remain unaffected.

```java
Example:

class Athlete {
public String athleteName;
public double athleteSpeed;
public int athleteAge;
}
```
Local variables are those variables present within a block, function, or constructor and can be accessed only inside them. The utilization of the variable is restricted to the block scope. Whenever a local variable is declared inside a method, the other class methods don’t have any knowledge about the local variable.

```java
Example:

public void athlete() {
String athleteName;
double athleteSpeed;
int athleteAge;
}
```
```
5. What do you mean by data encapsulation?
```
Data Encapsulation is an Object-Oriented Programming concept of hiding the data attributes and their behaviors in a single unit.
It helps developers to follow modularity while developing software by ensuring that each object is independent of other objects by having its own methods, attributes, and functionalities.
It is used for the security of the private properties of an object and hence serves the purpose of data hiding.

```
6. Tell us something about JIT compiler.
```
JIT stands for Just-In-Time and it is used for improving the performance during run time. It does the task of compiling parts of byte code having similar functionality at the same time thereby reducing the amount of compilation time for the code to run.
The compiler is nothing but a translator of source code to machine-executable code. But what is special about the JIT compiler? Let us see how it works:
First, the Java source code (.java) conversion to byte code (.class) occurs with the help of the javac compiler.
Then, the .class files are loaded at run time by JVM and with the help of an interpreter, these are converted to machine understandable code.
JIT compiler is a part of JVM. When the JIT compiler is enabled, the JVM analyzes the method calls in the .class files and compiles them to get more efficient and native code. It also ensures that the prioritized method calls are optimized.
Once the above step is done, the JVM executes the optimized code directly instead of interpreting the code again. This increases the performance and speed of the execution.

```
9. Briefly explain the concept of constructor overloading
```
Constructor overloading is the process of creating multiple constructors in the class consisting of the same name with a difference in the constructor parameters. Depending upon the number of parameters and their corresponding types, distinguishing of the different types of constructors is done by the compiler.

```java
class Hospital {
    int variable1, variable2;
    double variable3;
    public Hospital(int doctors, int nurses) {
     variable1 = doctors;
     variable2 = nurses;
    }
    public Hospital(int doctors) {
     variable1 = doctors;
    }
    public Hospital(double salaries) {
     variable3 = salaries
    }
}
```
