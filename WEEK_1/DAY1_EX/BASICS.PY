print("hello world")

#define variables
integer=10
float=3.14
string="AI"
list=[1,2,3]
tuple={4,5,6,}
dict ={"name":"fidha","age":22}
print("string:", string  + " BOOTCAMP")
list.append(4)
print("list:",list)
print(dict["name"])

#count = int(input("enter the number for count down:"))
#while count > 0 :
    #print(count)
    #count-=1
    
#print("outside loop")  

#for i in range(10):
    #if(i==6):
        #break
    #print(i)
#print("outside loop")    

#for i in range(10):
    #if(i==5):
        #continue
    #print(i)
#print("out side the loop!")    

#num=int(input("enter the range of the odd numbers :"))

#for i in range(num):
    #if i % 2 == 0:
        #continue
    #print(i)
#print("outside the looop")    


#num= int(input("enter the damn number:"))
#if num >1:
    #for i in range(2, int(num**0.5)+1):
        #if num % i == 0:
            #print(f"{num}is not a prime number")
            #break
    #else:
        ##print(f"{num}is a prime NUMBEEERR!!!")
#else:
    #print(f" {num}    is not a prime.......")    
    
def add(a,b):
    return a+b

def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    print("/nMENU")
    print("1.ADD")
    print("2.SUB")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5.EXIT")
    
    choice=int(input("enter the choice number:"))
    if choice==5:
        print("exiting........")
        break
    
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    
    if choice == 1:
        print("addition result:",add(num1,num2))
    if choice ==2:
        print("sub result:",sub(num1,num2))
    if choice == 3:
        print("multi result:",multi(num1,num2))
    if choice == 4:
        print("division result:",div(num1,num2))
               
    
    
                
                    
    
    
    
     