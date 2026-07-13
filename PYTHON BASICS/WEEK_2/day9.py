#PRACTICE QUESTIONS

#BLOOD PRESSURE CHECKER
#Q1 — Blood Pressure Checker
# Take systolic and diastolic pressure as input.
# Below 90/60 → Low Blood Pressure
# 90/60 to 120/80 → Normal
# 120/80 to 140/90 → Pre-Hypertension
# Above 140/90 → Hypertension
# Print the category. 

# systolic=int(input("enter the the higest pressure: "))
# diastolic=int(input("enter the lowest pressure: "))
# if systolic <90 and diastolic < 60:
#     print("LOW BLOOD PRESSURE")
# elif systolic<120 and systolic >80:
#     if diastolic <90 and diastolic>60:
#         print("NORMAL ")   
# elif systolic< 140 and systolic>90:
#     if diastolic <120 and diastolic>80:
#         print("pre- hypertension")
# elif systolic>140 and diastolic>90:
#     print("HYPERTENSION")        
# else:
#     print("invalid input!!!")

#------------------------------------------------------------------------------------------------------------------------------#

#Q2
# Q2 — Internet Speed Classifier
# Take download speed in Mbps as input.

# Below 5 → Very Slow
# 5 to 25 → Basic
# 25 to 100 → Fast
# Above 100 → Ultra Fast
# Print category and whether it's suitable for video streaming (needs minimum 25 Mbps).        
             
# speed=int(input("enter the speed of the network(please write in Mbps):  "))
# if speed <= 5 :
#     print("very slow , not suitable for streaming min 25Mbps is required")
# elif speed >5 and speed<25:
#     print("basic,suitable for streming....")
# elif speed >25 and speed <100:
#     print("fast,suitable for streaming....") 
# elif speed >100:
#     print("ultra fast, suitable for streaming......")
# else :
#     print("invalid input") 

#-----------------------------------------------------------------------------------------------------------------------------#


#q3
# 3 — Currency Converter
# Take amount in INR and destination country as input (UAE/Qatar/USA/UK).

# 1 INR = 0.044 AED (UAE)
# 1 INR = 0.044 QAR (Qatar)
# 1 INR = 0.012 USD (USA)
# 1 INR = 0.0097 GBP (UK)
# Print converted amount with currency symbol. 

# amount=int(input("enter the amount in rupees :"))
# n=input("enter the country the amount is to be converted:\n 1.qatar \n2. UAE \n3. USA \n4. UK\n ")
# if n=="1":
#     m=amount*0.044
#     print("conerted amount:",m,"QAR")
# elif n=="2":
#     m=amount*0.044
#     print("conerted amount:",m,"AED")
# elif n=="3":
#     m=amount*0.012
#     print("converted amount:",m,"USD")
# elif n=="4":
#     m=amount*0.0097
#     print("converted amount:",m,"GBP")

#-----------------------------------------------------------------------------------------------------------------------------#

#Q4
# Q4 — Flight Seat Pricing
# Take seat class as input (Economy/Business/First).
# Take whether it's a weekend as input (yes/no).
# Weekend flights cost 20% extra on all classes.

# Economy → ₹5000
# Business → ₹15000
# First → ₹40000
# Print final ticket price.


# c=input("CHOOSE THE SEAT CLASS :\n1. Economy \n2. Business \n3. First \n")
# d=input("is it weeknd or not[y/n] :")
# if d=="y":
#     if c=="1":
#         amount=5000+5000*20/100
#         print("TOTAL COST: ",amount)
#     elif c=="2":
#         amount=15000+15000*20/100
#         print("TOTAL COST: ",amount)
#     elif c=="3":
#         amount=40000+40000*20/100
#         print("TOTAL COST:",amount) 
#     else:
#         print("invalid")
# elif d=="n":
#     if c=="1":
#         print("TOTAL COST : 5000 Rs") 
#     elif c=="2":
#         print("TOTAL COST: 15000 Rs")
#     elif c=="3":
#         print("TOTAL COST: 40000 Rs") 
#     else:
#         print("invalid")
# else:
#     print("invalid")                                   

#-----------------------------------------------------------------------------------------------------------------------------

#Q5
# Q5 — Job Application Eligibility
# Take age, degree, and years of experience as input.

# Age must be between 21 and 35
# Must have a degree (yes/no)
# Experience must be above 2 years
# Print ELIGIBLE or exactly which condition failed.

# age=int(input("enter the age:"))
# if age>21 and age<35:
#     degree=input("If you have a degree or not [y/n]: ")
#     if degree=="y":
#         exp=int(input("enter the year of experience"))
#         if exp>2:
#             print("ELIGIBLE")
#         else:
#             print("not eligible need experience more than 2")
#     else:
#         print("not eligible need a degree")
# else:
#     print("not eligible under age ")                    

#-----------------------------------------------------------------------------------------------------------------------------


#Q6
# Q6 — Cab Fare Calculator
# Take distance in km and time of day as input.

# Base fare → ₹50
# Per km → ₹15
# Night charge (10pm to 6am) → add 20% surcharge
# If distance above 30km → add ₹100 toll
# Print final fare.

distance=int(input("enter the distance:"))
time=input("enter the time:")
if time>"10pm" :
    print("worked") 
else:
    print("invalid")    
                       