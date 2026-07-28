# #string contact
# a=["a","b","c","d"]
# b=["e"]
# print(a+b)


# a=["a","b","c","d"]
# a=a+["e"]
# print(a)

#HOME WORK 

# num=int(input("enter the number:"))
# a=num
# a=str(num)
# for i in  range(len(a)):
#     r=num%10
#     print(r,end="")
#     num=num//10


# num=123
# while num>0:
#     a=num%10
#     print(a,end="")
#     num=num//10

#AMSTRONG NUMBERS USING WHILE LOOP

num=int(input("enter the number: "))
n=num
amstrong=0
e=len(str(n))
while n>0:
    r=n%10
    amstrong+=r**e
    n=n//10
if amstrong==num:
    print(num,"IS AN AMSTRONG NUMBER")
else:
    print(num,"NOT AN AMSTRONG NUMBER")  
      



    

    
    
    


