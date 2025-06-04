#slicing
greet="Good Morning"
print(greet[0:5])
print(greet[2:])

#concatenated
print(greet+" World")

#string function
me="Python is fun"
print(me)
print(me[1])
print(me[:6])
print(me[7:])
print(me*3)
print(me+" Let's Learn")

#count
print(me.count("n"))
print(me.count("n",8))

#endwith
print(me.endswith("fun"))
print(me.endswith("fun",3))
print(me.endswith("fun",3,10))

#isalph
print(me.isalpha())

#isalnum
print(me.isalnum())

#isdigit
me1="1562"
print(me1.isdigit())

#islower
me2="sjsjsDd"
print(me2.islower())

#isupper
me3="HELLO"
print(me3.isupper())

#join
n="*"
me4=("World")
print(n.join(me4))

#replace
print(me)
print(me.replace("fun","fun more"))

#len
print(len(me))

#task1
print("Animals".lower())
print("Badger".lower())
print("Honey bee".lower())
print("Honey Badger".lower())

#task2
print("Animals".upper())
print("Badger".upper())
print("Honey bee".upper())
print("Honey Badger".upper())

#task3
print("   Filet Mignon   ".replace(" ","") )
print("Brisket   ".rstrip())
print("  cheeseberger".lstrip())

#task4
print("Becomes".startswith("be"))
print("becomes".startswith("be"))
print("BEAR".startswith("be"))
print("  becomes".startswith("be"))
 
#task4
s1="Becomes"
s2="becomes"
s3="Bear"
s4="   becomes"
l1=(s1.lower())
l2=(s3.lower())
s7=(s4.strip())
print(l1.startswith("be"))
print(l2.startswith("be"))
print(s2.startswith("be"))
print(s7.startswith("be"))

#Task1
st1="Welcome "
print(len(st1))

#Task2
st2="Hello World! "
print(st1+st2)

#list
st=[12,34,23,67,56]
print(st)
print(st[0])
print(st[-1])
print(st[2:5])

#append
st.append(40)
print(st)

#insert
st.insert(2,55)
print(st)

#remove
st.remove(23)
print(st)

#pop
st.pop()
print(st)

#len
print(len(st))

#in
li=["h","e","l","l","o"]
print("l" in li)

#extend
li1=["h","e","l","l","o"]
li1.extend([1,2,3,4,5])
print(li1)

#reverse
li1=["h","e","l","l","o"]
li1.reverse()
print(li1)

#sort
li1=["h","e","l","l","o"]
li1.sort()
print(li1)
li1=[4,8,2,6,9,-2]
li1.sort()
print(li1)

#concatinate
li1=["h","e","l","l","o"]
print(li1+["a","b","c","d","e"])

#duplicate
li1=["h","e","l","l","o"]
print(li1*3)

#task1
fruits=["apple","banana","cherry","mango","orange"]
print(fruits)
#task2
print(fruits[2])
#task3
fruits[2]="grapes"
print(fruits)
#task4
fruits.append("kiwi")
print(fruits)
#task5
fruits.insert(2,"pineaple")
print(fruits)
#task6
fruits.remove("banana")
print(fruits)
#task7
print(fruits[:3])
#task8
print("apple" in fruits)
#task9
fruits.sort()
print(fruits)
#task10
fruits.reverse()
print(fruits)

#tuple
li1=("h","e","l","l","o")
print(li1)
print(li1[0])
#len
print(len(li1))

#in
print("h" in li1)

#multiplicate tuple
print(li1*3)

#task1
lang=("python","java","c")
print(lang)
#task2
device=("laptop","tablet","smartphone","smartwatch")
print(device)
print(device[1])
print(device[-1])
#task3
cities=("mumbai","delhi","chennai","kolkata")
print("delhi" in cities)
#task4
sports=("cricket","football","hockey","tennis","badminton")
print(sports)
print(len(sports))
#task5
la=("python ")
print(la*3)
#task6
del la
#task7
cou=("india","usa","uk")
print(cou)
print(cou[0:2])
#task8
t1=("h","e","l","l","o")
t2=(5,2,6,3,4)
print(t1+t2)
#task9
my1=[1,2,3,4]
my2=tuple(my1)
print(my2)
#task10
print("india" in cou)
#task11
print(len(cou))
#task12
del cou