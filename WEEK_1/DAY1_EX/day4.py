# #CONTROL FLOW STATEMENTS

# # conditional statement

# # #if statement
# # a=18
# # if a>=18:
# #     print("eligible ")
    
# # #if-else statement
# age1=18
# if age>=18:
#     print("adult")  
# else:
#     print("minor")

                                           #QUESTIONS

# #program1
# num=-4          
# if num<0:
#      print(num,"negative number")
# else:
#     print(num,"positive number") 

# #program2

# num2=5
# if num%2==0:
#     print(num2,"not an odd number")
# else:
#     print(num2,"is an odd number")
    
    
# #program 3
# n=10
# if num%2==0:
#     print(n,"is an even number")
# else:
#     print(n,"not an even number")

# #program 4
# num1=25
# if num1%5==0:
#     print(num1,"number i sdivisible by 5")
# else:
#     print(num1,"not divisible by 5")

# #program 5
# password="hello"
# if len(password)==5:
#     print("password created")
# else:
#     print("only 5 characters allowed") 

# #program 6
# age=18
# learners=1
# if age>=18 and learners==1:
#     print("can apply for liecense")      
# else:
#     print("not applicable") 
    
# #program 7
# num1=18
# num2=56
# if num1>num2:
#     print("greatest number:",num1) 
# else:
#     print("greatest number is :",num2) 
    
# #program 8
# string1="hello"
# string2="fidha"              
# if len(string1)==len(string2):
#     print("string of same length",len(string1))
# else:
#     print("not same length ")    

# #INPUT FROM THE USER

# #USING SAME PROGRAM AS ABOVE BUT WITH USER INPUT

# #program1
# num=int(input("enter the number:"))          
# if num<0:
#      print(num,"negative number")
# else:
#     print(num,"positive number") 

# #program2

# num2=int(input("enter the number"))
# if num%2==0:
#     print(num2,"not an odd number")
# else:
#     print(num2,"is an odd number")
    
    
# #program 3
# n=int(input("enter the number"))
# if num%2==0:
#     print(n,"is an even number")
# else:
#     print(n,"not an even number")

# #program 4
# num1=int(input("enter the number"))
# if num1%5==0:
#     print(num1,"number i sdivisible by 5")
# else:
#     print(num1,"not divisible by 5")

# #program 5
# password=input("enter the string")
# if len(password)==5:
#     print("password created")
# else:
#     print("only 5 characters allowed") 

# #program 6
# age=int(input("enter the age: "))
# learners=int(input("do you have learners or not,if yes type 1 else type 0: "))
# if age>=18 and learners==1:
#     print("can apply for liecense")      
# else:
#     print("not applicable") 
    
# #program 7
# num1=int(input("enter the first number: "))
# num2=int(input("enter the second number: "))
# if num1>num2:
#     print("greatest number:",num1) 
# else:
#     print("greatest number is : ",num2) 
    
# #program 8
# string1=input("enter the first string: ")
# string2=input("enter the second string: ")              
# if len(string1)==len(string2):
#     print("string of same length",len(string1))
# else:
#     print("not same length")  


#q1 a company decided to give bonus of 5% of salary to an employee if his/her year of service is more than 5
salary=int(input("enter the salary : "))
num=int(input("enter the number of years worked:"))
if num> 5:
    bonus=salary*5/100
    new_salary=salary+bonus
    print("SALARY WITH BONUS:",new_salary)   
else:
    print("NO BONUS")                
                
     