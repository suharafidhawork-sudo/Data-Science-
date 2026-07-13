#...........................................LOOOPS AND ITERATION..............................................................>>>>


#learning traversal in list 

# a=["red",1,2,3,"blue"]
# for i in a:
#     print(i)


# b="hello world"
# for i in b:
#     print(i)

#q7
# #HOSPITAL PATIENT REGISTRATION
# count_child=0
# count_adults=0
# count_senior=0
# n=int(input("enter the number of patients: "))
# for i in range(n):
#     name=input("enter the name:")
#     age=int(input("enter the age: "))
#     if age<18:
#         count_child+=1
#     elif age>18 and age<60:
#         count_adults+=1
#     else:
#         count_senior+=1 
# print("NO OF CHILDREN :",count_child)
# print("NO OF ADULTS: ",count_adults)  
# print("NO OF SENIORS:",count_senior)     



#cricket score board

num=int(input("enter the number of balls played: "))    
total=0
count_4=0
count_6=0
for i in range(1,num+1):
    print("RUN ",i)
    s=int(input(" score: "))
    total+=s
    if s==4:
        count_4+=1
    if s==6:
        count_6+=1
print("TOTAL SCORES:",total)   
print("NO OF 4 :",count_4)    
print("NO OF 6: ",count_6) 
            
       
        
    
    
   
