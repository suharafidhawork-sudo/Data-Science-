#sample questions


#print all the even numbers between a range

# num=int(input("enter the range :"))
# for i in range(num) :
#     if i%2 == 0:
#         print(i)

#find the sum of all numbers between 1 to 100

# num=int(input("enter the number:"))
# count=0
# for i in range(num):
#     count+=i
# print(count)    


#print students grade based upom their marks

# mark=int(input("enter the marks:"))
# if mark>=90:
#     print(" A GRADE")
# elif mark>=80:
#     print("B GRADE")
# elif mark>=50:
#     print("C GRADE")
# else:
#     print("D GRADE")         


# #calculate simple interest from givent principal, rate amd time
# p=int(input("enter the principal amount:"))
# rate=int(input("enter the rate:"))
# time=int(input("enter the time:"))

# si=(p*rate*time)/100
# print("simple interest: ",si)


#largest of three numbers
# print("LARGEST OF 3 NUMBERS")
# num1=int(input("enter the first number"))
# num2=int(input("enter the second number:"))
# num3=int(input("enter the third number:"))
# if num1>num2:
#     if num1>num3:
#         print("the largest number is: ",num1)
#     else:
#         print("the largest number is :",num3)
# elif num2>=num1:
#     if num2>num3:
#         print("the largest number is :",num2)
#     else:
#         print("largest number is :,",num3)    
     
    
# #multiplication               
# num=int(input("enter the number:"))
# print("MULTIPLICATION TABLE OF ",num)

# for i in range(1,11):
#     print(i,"*",num,":",i*num)

# #how many vowels in a word
# s=input("enter the string: ")
# count=0
# for letter in s:
#     if letter=="a"or letter=="A" or letter=="e" or letter=="E" or letter=="i" or letter=="I" or letter=="O" or letter=="o" or letter=="U" or letter=="u":
#         count+=1
# print("the number of vowels in the string :",count)        
        
#not getting the logic string traversal???

#palindrome of a string 

# s=input("enter the string")     
# if s==s[::-1]:
#     print("is a palindrome")
# else:
#     print("not a palindrome")          

#reverse a string 
 
# s=input("enter the string:")
# r=s[::-1]
# print(r)

# A shop gives 10% discount if bill is above ₹500. Take bill amount as input and print final amount after discount.

# amount=int(input("enter the amount: ")) 
# if amount>500 :
#     dis_amn=amount*10/100
#     upd_amn=amount-dis_amn
#     print(upd_amn)
# else:
#     print("discount cannot be applied")   


 #VVOWELS IN A STRING
# s=input("enter the string: ")
# count=0
# for letter in s:
#     if letter in "aeiouAEIOU": 
#         count+=1
# print("the number of vowels in the string :",count)        
        
 
        