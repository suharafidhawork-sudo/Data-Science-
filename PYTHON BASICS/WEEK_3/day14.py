# #----------------------------------------PATTERNS USING FOR LOOP----------------------------------------------------
# #star pattern
# n1=int(input("enter the number of rows: "))
# for i in range(1,n1+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print() 


# #number pattern
# n2=int(input("enter the number of rows: "))    
# for i in range(1,n2+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()  


# #number pattern
# n3=int(input("enter the number of rows: "))    
# for i in range(1,n3+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()       


# #SQUARE PATTERN
# n4=int(input("enter the number: "))
# for i in range(1,n4+1):
#     for j in range(1,n4+1):
#         print("*",end=" ")
#     print() 

     

# #INVERTED TRIANGLE
# n5=int(input("enter the no of rows: ")) #5
# for i in range(1,n5+1): #(1,6)
#     for j in range(1,n5-i+2): 
#         print("#",end=" ")
#     print()    


      
# #inverted trinagle numbers
# n6=int(input("enter the no of rows: ")) #5
# for i in range(1,n6+1): #(1,6)
#     for j in range(1,n6-i+2): 
#         print(j,end=" ")
#     print()    
      
      
      
# n1=int(input("enter the number of rows: "))
# for i in range(1,n1+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print() 

# n1=int(input("enter the number of rows: "))
# for i in range(n1+1,1,-1):
#     for j in range(1,i):
#         print("*",end=" ")
#     print() 
    
    
# n=int(input("enter the no of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i):
#         if j%2==0:
#             print(j,end=" ")
#     print()        

# n=int(input("enter the no of rows:"))
# for i in range(1,n+1,2):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()            

rows=5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==1  or   j==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()            
 
rows=5
for i in range(1,rows+1):
    for j in range(1,rows):
        if i==1 or i==3 or j==1 or i==rows or i==j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    

#PRINT ALPHABETS PATTERNS  
r=int(input("enter the no of rows:"))
for i in range(1,r+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()    
    
    
    
            
                
