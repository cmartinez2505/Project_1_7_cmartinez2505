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

base_insurance = 50.00
final_insurance = base_insurance

#If Statement #1 (A surcharge for young drivers that are 25 and under.)
if age <= 25:
    final_insurance += 25.00
    

