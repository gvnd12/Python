# # Odd or Even
# a=int(input("Enter a number: "))
# if a%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")



# # Largest of 2 numbers
# a=input("Enter first number: ")
# b=input("Enter second number: ")
# if a>b:
#     print("First number is larger than the second number")
# else:
#     print("Second number is larger than the first number")



# # Largest of 3 numbers
# a=input("Enter first number: ")
# b=input("Enter second number: ")
# c=input("Enter third number:" )
# if b>a and b>c:
#     print("Second number is the largest number")
# elif a>b and a>c:
#     print("First number is the largest number")
# else:
#     print("Third number is the largest number")



# # Grade according to marks
# a= int(input("Enter your marks: "))
# if 90 <= a <= 100:
#     print("Grade is A+")
# elif 80<=a<90:
#     print("Grade is A")
# elif 70<=a<80:
#     print("Grade is B")
# elif 60<=a<70:
#     print("Grade is C")
# elif 50<=a<60:
#     print("Grade is D")
# else:
#     print("Failed")



# #Last digit of a number
# a=int(input("Enter a number: "))
# b=int(a%10)
# print("Last digit of the number is:",b)



# #Check divisibility of a number by 2 and 5
# a= int(input("Enter a number: "))
# if a%2 == 0 and a%5 == 0:
#     print("The number is divisible by 2 and 5")
# elif a%2 == 0 and a%5 != 0:
#     print("The number is divisible by 2 but NOT by 5")
# elif a%2 != 0 and a%5 == 0:
#     print("The number is NOT divisible by 2 but divisible by 5")
# else:
#     print("The number is NOT divisible by 2 and 5")



# #Nested if
# #Check divisibility of a number by 2 and 5
# a= int(input("Enter a number: "))
# if a%2==0:
#     if a%5==0:
#         print("The number is divisible by 2 and 5")
#     else:
#         print("The number is divisible by 2 but not by 5")
# else:
#     if a%5==0:
#         print("The number is not divisible by 2 but divisible by 5")
#     else:
#         print("The number is NOT divisible by 2 and 5")



# #Nested if
# #Check if a number is positive or negative and odd or even
# a=int(input("Enter a number: "))
# if a>0:
#     if a%2==0:
#         print("The number is positive and even")
#     else:
#         print("The number is positive and odd")
# else:
#     if a==0:
#         print("The number is zero")
#     else:
#         print("The number is negative")



# #Nested if
# #Check for largest of 3 numbers
# a1=int(input("Enter 1st number: "))
# a2=int(input("Enter 2nd number: "))
# a3=int(input("Enter 3rd number: "))
# if a1>a2:
#     if a1>a3:
#         print("1st number is the largest")
#     else:
#         print("3rd number is the largest")
# else:
#     if a2>a3:
#         print("2nd number is the largest")
#     else:
#         print("3rd number is the largest")