#{_Day 1_}
# #print("Hello, Somesh! Welcome to Day 1 of your Python journey.")

#num1=2
#num2=4
#sum=num1+num2 
#print(f"sum of {num1} and {num2} is {sum}")

#name=input("Enter your name : ")
#age=input("Enter yout age : ")
#print(f"His name is {name} and he is {age} years old")

# number=input("Enter a number : ")
# number=int(number)
# if number % 2 == 0 :
#     print(f"The given number {number} is Even")
# else:
#     print(f"The given number {number} is odd")
# if 1 <= number <= 100:
#     print(f"and it is between 1 to 100")
# elif 101 <= number <= 200:
#     print(f"and it is between 100 to 200")
# else :
#     print(f"and it is out of bound")

# number=input("Enter any number : ")
# number=int(number)
# if number % 2 == 0 :
#     print(f"The given number {number} is even")
#     # print(f"The given number {number} is whole number")
# else :
#     print(f"The given number {number} is odd")
# if number <= 0 :
#     print(f"The given number {number} is negative number")
# else :
#     print(f"The given number {number} is positive number")
# if number.is_integer():
#     print(f"The given number {number} is whole number")

###___DAY_2___###
# celsius=input("Enter Celsius : ")
# celsius=float(celsius)
# fahrenheit= (9/5)*celsius+32
# print("The Tempreture in fahrenheit is ", fahrenheit)

# P=input("Enter Principle amount : ")
# P=float(P)
# R=input("Enter Rate of interest : ")
# R=float(R)
# T=input("Enter Duration of time : ")
# T=float(T)
# SI=(P*R/100*T)/100
# Total=P+SI
# EMI=Total/(T*12)
# print("The Interest for given details for 1 month is : ", SI)
# print("The Total amount for given details is : ", Total)
# print("The EMI for given details for 1 month : ", EMI)

# A=input("Enter anything : ")
# try:
#     Value=int(A)
#     print(f"The given data {A} is Integer.")
# except ValueError:
#     try:
#         Value=float(A)
#         print(f"The given data {A} is Floating Integer")
#     except ValueError:
#         if A.lower() in ['true', 'false']:
#             print(f"The given data {A} is Boolean")
#         else :
#             print(f"The given data {A} is string")

# value_1=input("Enter value 1 : ")
# value_1=int(value_1)
# value_2=input("Enter value 2 : ")
# value_2=int(value_2)
# value_3=input("Enter value 3 : ")
# value_3=int(value_3)

# if value_1>value_2 and value_1>value_3:
#     print(f"The given value {value_1} is greater than other values")
# elif value_2>value_1 and value_2>value_3:
#     print(f"The given value {value_2} is greater than other values")
# else :
#     print(f"The given value {value_3} is greater than other values")

# def add(a, b):
#     return a + b
# print(add(2, 3))

###########################___DAY_3___###########################
# n=input("Enter any number : ")
# n=int(n)
# is_prime = True
# if n<=1:
#     is_prime=False
# else :
#     for i in range(2, int(n**0.5) + 1):
#         if n % 1 == 0:
#             is_prime = False
#             break
# if is_prime :
#     print(f"The given number {n} is prime number")
# else :
#     print(f"The given number {n} is not a prime number")

# i=int(input("Enter any number : "))
# if i % 3 == 0 and i % 5 == 0 :
#         print(f"{i} FizzBizz")
# elif i % 3 == 0 :
#         print(f"{i} Fizz")
# elif i % 5 == 0 :
#         print(f"{i} Bizz")
# else : 
#         print(i)

# num=input("Enter a number : ")
# sum_of_digits=0
# for digits in num :
#     sum_of_digits += int(digits)
# print("Sum of given number is ", sum_of_digits)

# rows = 3
# for i in range (1, rows+1):
#     print("*"*i)

###########################___DAY_4___###########################
# a=int(input("Enter number a : "))
# b=int(input("Enter number b : "))

# sum=a+b
# print(f"Sum of {a} and {b} is {sum}")

# dif=a-b
# print(f"Difference of {a} and {b} is {dif}")

# mul=a*b
# print(f"Multiplication of {a} and {b} is {mul}")

# div=a/b
# print(f"Division of {a} and {b} is {div}")

# a=int(input("Enter number a : "))
# b=int(input("Enter number b : "))
# operator=input("Enter operator(+,-,/,*) : ")

# if operator == '+':
#     sum=a+b
#     print(f"Sum of {a} and {b} is {sum}")
# elif operator == '-':
#     dif=a-b
#     print(f"Difference of {a} and {b} is {dif}")
# elif operator == '/':
#     div=a/b
#     print(f"Division of {a} and {b} is {div}")
# elif operator == '*':
#     mul=a*b
#     print(f"Multiplication of {a} and {b} is {mul}")
# else :
#     print("The selected operator is invalid")

# Year=int(input("Enter number a year : "))
# if Year%4==0 and Year%100==0 and Year%400==0:
#     print(f"The given year {Year} is a leap year")
# else :
#     print(f"The given year {Year} is not a leap year")

# Maths=float(input("Marks in Maths : "))
# Science=float(input("Marks in Science : "))
# English=float(input("Marks in English : "))
# Hindi=float(input("Marks in Hindi : "))
# Marathi=float(input("Marks in Marathi : "))

# Average=(Maths+Science+English+Hindi+Marathi)/5
# Percentage=(Average/100)*100

# if Percentage >= 90:
#     print(f"{Percentage} A+ Grade")
# elif Percentage >= 80:
#     print(f"{Percentage} A Grade")
# elif Percentage >= 70:
#     print(f"{Percentage} B+ Grade")
# elif Percentage >= 60:
#     print(f"{Percentage} B Grade")
# elif Percentage >= 50:
#     print(f"{Percentage} C+ Grade")
# elif Percentage >= 40:
#     print("C Grade")
# else:
#     print("Fail")

###########################___DAY_5___###########################
# Grocery_list=[]

# while True:
#     item=input("Enter item name (or 'Done' to finish shopping) : ")
#     if item.lower()=='done':
#         break
#     Quantity=int(input("Enter quantity of item : "))
#     Price=float(input("Enter price per item : "))
#     Grocery_list.append((item,Quantity,Price))

# print("\n--- Grocery List ---")
# print("Item\tQty\tPrice\tTotal")
# grand_total=0
# for item in Grocery_list:
#     item_total=item[1]*item[2]
#     print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item_total}")
#     grand_total += item_total

# print("---------------------")
# print(f"Grand Total : Rs. {grand_total} ")

###########################___DAY_6___########################### 8th Aug

# def convert_types(a, b):
#     int_value = int(a)
#     str_value = str(b)
#     return (int_value, str_value)

# result = convert_types("10", 3.14)
# print(result)

# a=int(input("Enter value of a : "))
# b=int(input("Enter value of b : "))
# x=(a*a+b*b)-(2*a*b)
# print(x)

# def calculations(a, b):
#     result = (a*a+b*b)-(2*a*b)
#     return result
# print(calculations(2,0))

# def formated_output(name, score):
#     name_value = str(name)
#     score_value= int(score)
#     return (name_value, score_value)
# result = formated_output("Somesh",48)
# print = ("Player <name> scored <score> points!", result)


# def process_input(data):
#     name, score = data.split(" ")
#     score = int(score)
#     return f"Player {name} has a score of {score}."

# print(process_input("Somesh 89"))

###########################___DAY_7___########################### 4th Aug


# print("---- Welcome to Ruchi's Bank ----")
# name=str(input("Enter customer's name : "))

# while True:
#     try:
#         Balance=int(input("Availabe Balance in bank account : "))
#         if Balance<0:
#             print("Negative amount is not valid")
#             continue
#         break
#     except ValueError:
#         print("Please enter a valid number")

# while True:
#     print("\n Choose a number : " )
#     print("1. Deposit ")
#     print("2. Withdraw")
#     print("3. View balance")
#     print("4. Exit")

#     Choice=input("Enter choice : ")
#     if Choice=="1":
#         try:
#             amount=int(input("Enter an amount : "))
#             if amount<0:
#                 print("Negative amount is not valid")
#             else:
#                 Balance += amount
#                 print("Deposit is successful")
#         except ValueError:
#             print("Entered amount is invalid")
    
#     elif Choice=="3":
#         print("Current Balance is : ", Balance)

#     elif Choice=="2":
#         try:
#             withdraw=int(input("Enter an amount to withdraw : "))
#             if withdraw<0:
#                 print("Negative withdrwal is not allowed")
#             else:
#                 Balance-=withdraw
#                 print("Withdrwal is succseeful")
#         except ValueError:
#             print("Entered amount is invalid")
    
#     elif Choice == "4":
#         print("\n--- Transaction Summary ---")
#         print(f"Name: {name}")
#         print(f"Final Balance: ₹{Balance:.2f}")
#         print("Thank you for banking with us!")
#         break

#     else:
#         print("Invalid choice. Please select from 1 to 4.")


###########################___DAY_8___########################### 7th Aug
# Indian_Rupee=float(input("Enter Indian Rupee : "))
# USD_rate=0.012
# Euro_rate=0.011
# Japan_rate=1.75
# USD=Indian_Rupee*USD_rate
# Euro=Indian_Rupee*Euro_rate
# Japan=Indian_Rupee*Japan_rate



# print("1. USD ")
# print("2. Euro ")
# print("3. Japan ")
# print("4. All ")
# Choice=input("Enter choice : ")

# if Choice=="1":
#     try:
#         if Indian_Rupee<0:
#             print("Negative value is not allowed")
#         else :
#             print(f"Indian rupee {Indian_Rupee} in USD is {USD}")
#     except ValueError:
#         print("Entered amount is invalid")

# elif Choice=="2":
#     try:
#         if Indian_Rupee<0:
#             print("Negative value is not allowed")
#         else :
#             print(f"Indian rupee {Indian_Rupee} in Euro is {Euro}")
#     except ValueError:
#             print("Entered amount is invalid")

# elif Choice=="3":
#     try:
#         if Indian_Rupee<0:
#             print("Negative value is not allowed")
#         else :
#             print(f"Indian rupee {Indian_Rupee} in Japan is {Japan}")
#     except ValueError:
#             print("Entered amount is invalid")

# elif Choice=="4":
#     try:
#         if Indian_Rupee<0:
#             print("Negative value is not allowed")
#         else :
#             print(f"Indian rupee {Indian_Rupee} in Euro is {Euro}, USD is {USD}, Japan is {Japan}")
#     except ValueError:
#             print("Entered amount is invalid")
        
# else:
#      print("Entered choice is invalid")

# Weight=float(input("Enter your weight in KG: "))
# Height=float(input("Enter your height in Meters: "))
# BMI=Weight/(Height**2)

# if BMI<18.5:
#     print(f"Your BMI is {BMI}. So you are Underweight ")
# elif 18.6 < BMI < 24.9:
#     print(f"Your BMI is {BMI}. So you are Healthy weight ")
# elif 25 < BMI < 29.9 :
#     print(f"Your BMI is {BMI}. So you are Overweight ")
# elif 30 < BMI < 34.9 :
#     print(f"Your BMI is {BMI}. So you are Obese ")
# elif 35 < BMI < 39.9 :
#     print(f"Your BMI is {BMI}. So you are Severly Obese ")

# User_name=str(input("Enter your name : "))
# User_unit=float(input("Enter units used : "))
# Electricity_bill = 0

# if User_unit < 0:
#     print("Invalid Units")
# elif User_unit < 100 :
#     Electricity_bill=User_unit*5
#     print(f"{User_name} Electricity bill is {Electricity_bill} Rs only ")
# elif User_unit < 200 :
#     Electricity_bill=(100*5)+((User_unit-100)*7)
#     print(f"{User_name} Electricity bill is {Electricity_bill} Rs only ")
# elif User_unit >= 201 : 
#     Electricity_bill=(100*5)+(100*7)+((User_unit-200)*10)
#     print(f"{User_name} Electricity bill is {Electricity_bill} Rs only ")

###########################___DAY_9___########################### 9th Aug

# def Check_conditions (a, b, c):
#      if (a>10 and b%2==0) or (c%3==0):
#           return "Valid"
#      else :
#         return "Invalid"
# print (Check_conditions(15, 4, 21))

# def grade_student (marks, attendence, project):
#     if (100>= marks >= 80 and 100>= attendence>=80) and (project):
#         return "Excellent"
#     elif (79>=  marks >= 60 and 79>= attendence>=60) and (project):
#         return "Good"
#     elif (59>=  marks >= 40 and 59>= attendence>=40) and (project):
#         return "Bad"
#     else :
#         return "Failed"

# print(grade_student(90, 95, True))       # Expected: Excellent
# print(grade_student(75, 65, True))       # Expected: Good
# print(grade_student(55, 50, True))       # Expected: Average
# print(grade_student(45, 55, False))      # Expected: Fail

# name=str(input("Enter student name : "))
# def grade_student (Name, Eng, Maths, Science, attendence, project):
#     marks = float((Eng+Maths+Science)/3)
#     if (100>= marks >= 80 and 100>= attendence>=80) and (project):
#          return "Excellent"
#     elif (79>=  marks >= 60 and 79>= attendence>=60) and (project):
#          return "Good"
#     elif (59>=  marks >= 40 and 59>= attendence>=40) and (project):
#          return "Bad"
#     else :
#          return "Failed"
    
# print(grade_student("Somesh", 90, 99, 97, 95, True))       # Expected: Excellent
# print(grade_student("Ruchi", 75, 55, 88, 65, True))       # Expected: Good
# print(grade_student("Rohini", 55, 55, 60, 56, False))       # Expected: Average
# print(grade_student("Kalyani", 45, 34, 37, 55, False))      # Expected: Fail

###########################___DAY_10___########################### 12th Aug
# Emp_name = str(input("Enter employee name : "))
# Emp_exp= float(input("Enter employee experience : "))
# Emp_rating=float(input("Enter employee rating : "))
# Emp_dept=str(input("Enter employ deptartment : ").strip().upper())


# if Emp_exp < 0 or Emp_rating < 0 or Emp_rating > 5 or Emp_dept not in ["QA", "Dev", "HR", "Sales"]:
#     print("Invalid input. Please check the values entered.")
# else:
#     if Emp_dept == "QA":
#         base_salary = 100000
#     elif Emp_dept == "Dev":
#         base_salary = 80000
#     elif Emp_dept == "HR":
#         base_salary = 65000
#     elif Emp_dept == "Sales":
#         base_salary = 55000


# if 5 >=Emp_rating >= 4.5 and Emp_exp >= 7 :
#     Bonus=0.20
# elif 4.4 >=Emp_rating >= 3.5 and 6.9 >= Emp_exp >= 5 :
#     Bonus=0.15
# elif 3.4 >=Emp_rating >= 2 and 4.9 <= Emp_exp >= 3.5 :
#     Bonus=0.10
# elif 1.9 >=Emp_rating >= 1 and 3.4 >= Emp_exp >= 1.9 :
#     Bonus=0.05
# elif Emp_rating >= 0.9 and Emp_exp <= 2 :
#     Bonus=0

# Bonus_salary = Bonus*base_salary
# Total_salary = Bonus_salary + base_salary

# print(f"Employee {Emp_name} from {Emp_dept} department has got rating {Emp_rating} with experience {Emp_exp} years. So his bonus is {base_salary} and total salary is {Total_salary}")

