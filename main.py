"""
Program Name: Insurance Quote Generator App
Author: Chris Martinez
Program Purpose: A user friendly tool that will ask customers basic questions like their age and driving history,
and then it will calculate their car insurance price depending on their answer, and then it will save that data into a profile.
Resources Used: Python Crash Course (Chapters 1-7)
Date: June 17 2026
"""

print("********************************")
print("   Welcome to MTZ Insurance!   ")
print("********************************")

#User Input Section

Customer_name = input(("Please enter your full name: ")).strip()
age = int(input("Please enter your age: "))
car_year = int(input("Please enter the year of your car: "))    
salary = float(input("Please enter your annual salary in digits: "))   
driving_years = int(input("How many years have you been driving? ")) 
accidents = int(input("How many vehicle accidents have you gotten in? ")) 

base_insurance = 100.00
final_insurance = base_insurance

#If Statement #1 (A surcharge of $25 for young drivers that are 25 and under.)
if age <= 25:
    final_insurance += 25.00
else:
    pass;   

#If Statement #2 (A discount of $15 for cars older then 15 years old and a $15 addition for cars newer 2023.)
if car_year <= 2011:
    final_insurance -= 15.00
elif car_year >= 2024:
    final_insurance += 15.00
else:
    pass

#If Statement #3 (A 10 percent surcharge is given for those who make over $200,000 annualy and a 10 discount for those who make $40,000 or less a year.)
if salary >= 200000:
    final_insurance += final_insurance * 0.10
elif salary <= 40000:
    final_insurance -= final_insurance * 0.10    
else:
    pass

#If Statement #4 (A extra 10 percent discount is given to drivers who drove a car for atleast 5 years or more.)
if driving_years >= 5:
    final_insurance -= final_insurance * 0.10
else:
    pass

#If Statement #5 (A extra 5 percent surcharge is given for those who had gotten into 2 or more car accidents.)
if accidents >= 2:
    final_insurance += final_insurance * 0.05
else:
    pass    
