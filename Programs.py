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



# #While loop
# #Check for Prime
# num=int(input("Enter number to be checked: "))
# i=2
# if num!=1:
#     while num>i:
#         if num%i==0:
#             print("Number is not prime")
#             break
#         i+=1
#     else:
#         print("Number is prime")
# else:
#     print("The entered number is 1, which is neither prime nor composite")



# #Factorial
# n=int(input("Enter the number whose factorial is to be found: "))
# num=1
# while n>=1:
#     num=n*num
#     n-=1
# print(num)



#Palindrome
# num=int(input("Enter a number to check if it is palindrome: "))
# z=num
# a=0
# n=0
# while num>0:
#     n=num%10
#     a=a*10+n
#     num//=10
# if z==a:
#     print("Number is a palindrome")
# else:
#     print("Number is not a palindrome")



# #Reverse of a number
# num=int(input("Enter a number to be reversed: "))
# a=0
# n=0
# while num>0:
#     n=num%10
#     a=a*10+n
#     num//=10
# print("The reverse of the number is:",a)



# #Amstrong number
# num=int(input("Enter the number to be checked: "))
# x=num
# z=num
# ams=0
# n=0
# count=0

# while num>0:
#     count+=1
#     num//=10

# while x>0:
#     n=x%10
#     ams=ams+n**count
#     x//=10

# if z==ams:
#     print("The entered number is amstrong number")
# else:
#     print("The entered number is not amstrong number")



# #For loop
# #Print * pyramid
# n=int(input("Enter number of rows to print the pattern: "))
# for i in range(n+1):
#     for j in range(i):
#         print('*',end=' ')
#     print()


# #Print inverted * pyramid 
# n=int(input("Enter number of rows to print the pattern: "))
# for i in range(n+1):
#     for j in range(n-i):
#         print('*',end='')
#     print()



# #Print number pyramid
# n=int(input("Enter number of rows to print the pattern: "))
# for i in range(n+1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()



# # Print inverted number pyramid
# n=int(input("Enter number of rows to print the pattern: "))
# for i in range(n+1):
#     for j in range(1,n-(i-1)):
#         print(j,end=' ')
#     print()


# #Print same number in all rows pyramid
# n=int(input("Enter number of rows to print the pattern: "))
# for i in range(n+1):
#     for j in range(i):
#         print(n,end=' ')
#     print()


# #Print one number in each row pyramid
# n=int(input("Enter number of rows to print the pattern: "))
# for i in range(1,n+1):
#     num=i
#     for j in range(1,i+1):
#         print(num,end='')
#     print()



# #Print one number in each row pyramid inverted
# n=int(input("Enter number of rows to print the pattern: "))
# for i in range(n,0,-1):
#     num=i
#     for j in range(n-i):
#         print(num,end='')
#     print()


# #Display prime numbers in a imit
# n=int(input("Enter the limit: "))
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


# #Reverse a string
# org_str=input("Enter a string: ")
# rev_str=''
# for i in org_str:
#     rev_str=i+rev_str
# print(rev_str)



# #Given 2 strings, s1, and s2 return a new string made of the first, middle and last characters each input string
# #A=abcde  B=uvwxyz   Out­­­­=> aucxez

# s1=input("Enter first string: ")
# s2=input("Enter second string: ")
# ms1=len(s1)//2
# ms2=len(s2)//2
# new_s=s1[0]+s2[0]+s1[ms1]+s2[ms2]+s1[-1]+s2[-1]
# print(new_s)



# #Count all lower case, upper case, digits, and special symbols from a given string
# s=input("Enter a string: ")
# upper=0
# lower=0
# special=0
# digit=0
# for i in s:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower+=1
#     elif i.isdigit():
#         digit+=1
#     else:
#         special+=1
# print("Uppercase=",upper)
# print("Lowercase=",lower)
# print("Digit=",digit)
# print("Special character=",special)



# #Given two strings, s1 and s2, create a mixed String
# #s1 = "Abc"
# #s2 = "Xyz"
# #Out => AzbycX
# s1=input("Enter first string: ")
# s2=input("Enter second string: ")
# max_len=max(len(s1),len(s2))
# mix_str=''
# for i in range(max_len):
#     if i<len(s1):
#         mix_str+=s1[i]
#     if i<len(s2):
#         mix_str+=s2[-i-1]
# print("Mixed string=",mix_str)



# #Find the index of the first occurrence of a substring in a string
# s1=input("Enter the string: ")
# s2=input("Enter the substring: ")
# f=s1.find(s2)
# if f>=0:
#     print("Substring is found at index",f)
# else:
#     print("Substring not found")



# #Write a Python program to add 'ing' at the end of a given string
# #If the given string already ends with 'ing' then add 'ly' instead.
# str=input("Enter a string: ")
# if str.endswith('ing') and len(str)>3:
#         print(str+'ly')
# else:
#     print(str+"ing")


# #Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$'
# str=input("Enter a string: ")
# strf=input("Enter the character to be replaced wiht $: ")
# newstr=str[0]+str[1:].replace(strf,'$')
# print(newstr)