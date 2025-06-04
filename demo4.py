try:
    age=int(input("Enter your age: "))
    print("your age is",age)
except:
    print("Invalid input")
try:
    n=int(input("Enter number: "))
    print("Result",10/n)
except:
    print("Can't divide by zero")


cart={"apple":30,"banana":20,"milk":10}
i=str(input("Enter the item:"))
try:
    if i in cart:
        print("Price of",i,"is",cart[i])
except:
        print("Invalid input")
        
try:
    age=int(input("Enter your age: "))
    print("your age is",age)
except:
    print("Invalid input")
try:
    n=int(input("Enter number: "))
    print("Result",10/n)
except:
    print("Can't divide by zero")


cart={"apple":30,"banana":20,"milk":10}
i=str(input("Enter the item:"))
try:
    if i in cart:
        print("Price of",i,"is",cart[i])
except:
        print("Invalid input")
        
#task1
for i in range(1,101):
    print(i)

#task2
num=int(input("Enter the number:"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
#task3
num=int(input("Enter the factorial number:"))
fact,i=1,1
while i<=num:
    fact=fact*i
    i=i+1
print("Factorial of",num,"is",fact)
    
#task4
for i in range(1,50):
    if(i%2==0):
        print(i)
#task5
num=int(input("Enter the sum of  number:"))
sum=0
while(num>0):
    ld=num%10
    sum=sum+ld
    num=num//10
print("Sum of digits of is",sum)
#task6
num=int(input("Enter the prime number:"))
for i in range(2,num):
    if(num%i==0):
        print(num,"is not a prime number")
        break
    else:
        print(num,"is a prime number")
        break
#task7
rad=int(input("Enter the radius:"))
def area(r):
    return 3.14*rad*rad
print("Area of circle is",area(rad))
#task8
n1=int(input("Enter the num1:"))
n2=int(input("Enter the num2:"))
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print("GCD of",n1,"and",n2,"is",gcd(n1,n2))
#task9
def count_vowels(s):
    count = 0
    for char in s:
        if char in 'aeiouAEIOU':
            count += 1
    return count
b=str(input("Enter the string:"))
print("Number of vowels in the string is",count_vowels(b))
#task10
b=str(input("Enter the string:"))
def reverse(s):
    return b[::-1]
print("Reverse of string is",reverse(b))
#task11
a=int(input("Enter num1:"))
b=int(input("Enter num2:"))
try:
    c=a/b
    print("Result is",c)
except:
    print("Error: Division by zero is not allowed")
#task12
a=int(input("Enter the number:"))
try:
    print("Age",a)
except:
    print("Number only allowed")