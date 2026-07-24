#----------------------------------------------------COMPREHENSION--------------------------------------------------------------

#LIST COMPREHENSION
num=[x for x in range(5)]
print(num)

#even numbers
nums=[x for x in range(5) if x%2==0]
print(nums)

#ODD NUMBERS
num1=[x for x in range(10) if x%2!=0]
print("LIST OF ODD NUMBERS:",num1)


#POWER OF NUMBERS
pow=[x**2 for x in range(10)]
print("POWER OF NUMBERS: ",pow)

#CUBE  OF NUMBERS
cube=[x**3 for x in range(10)]
print("CUBE :",cube)

#SUM OF NUMBERS
sum=sum([x for x in range(11) ])
print("SUM :",sum)

#TUPLE COMPREHENSION
t=tuple(x for x in range(10))
print(t)

#SET COMPREHENSION
s={x for x in range(10)}
print(s)

s1={x%3 for x in range(6)}
print(s1)

#DICTIONARY COMPREHENSION
d={x:x*x for x in range(10)}
print("square of numbers till 10",d)
d1={x:x*x for x in range(10) if x%2==0}
print("square of even numbers:",d1)


#----------------------------------------STRING METHODS---------------------------------------------------------------

#LOWER CASE
s1="Hello World"
print(s1.lower())

#UPPER CASE
s2="Hello World"
print()


