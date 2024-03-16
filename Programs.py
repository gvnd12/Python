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



# #Display prime numbers in a limit
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
# newstr=str[0]+str[1:].replace(str[0],'$')
# print(newstr)



# #Reverse the order of the words in the given string
# str=input("Enter a string: ")
# x=str.split(' ')
# newstr=''
# for i in x:
#     newstr=i+' '+newstr
# print('The reversed string is:',newstr)



# #Count vowels and consonants in a string
# str=input("Enter a string: ")
# countv=0
# countc=0
# for i in str:
#     if i in ['a','e','i','o','u','A','E','I','O','U']:
#         countv+=1
#     else:
#         countc+=1
# print('Vowels=',countv)
# print('Consonants=',countc)



# #Remove duplicates in a string
# str=input("Enter a string: ")
# newstr=''
# for i in str:
#     if i not in newstr:
#         newstr=newstr+i
# print(newstr)



# #Count the number of letters in a word using loop
# str=input("Enter a string: ")
# count=0
# for i in str:
#     if i.isalpha():
#         count+=1
# print("The number of letters in the word =",count)



# #Convert lower letter to upper and upper letter to lower in a string
# str=input("Enter a string: ")
# newstr=''
# for i in str:
#     if i.islower():
#         newstr+=i.upper()
#     elif i.isupper():
#         newstr+=i.lower()
# print(newstr)



# #Program to sort letters of word by lower to upper case format
# str=input("Enter a string: ")
# lower=''
# upper=''
# for i in str:
#     if i.islower():
#         lower+=i
#     elif i.isupper():
#         upper+=i
# print("Lowercase letters are:",lower)
# print("Uppercase letters are:",upper)



#Convert all the starting letter of a word in a string
# s=input("Enter a string: ")
# ns=s.split(' ')
# for i in ns:
#     a=i[0].swapcase()+i[1:]
#     print(a,end=' ')



#Input list with loop
# a=int(input("Enter size of array: "))
# x=[]
# for i in range(a):
#     arr=input("Enter element of array: ")
#     x.append(arr)
# print(x)



#Sum of elements of list with loop
# a=int(input("Enter size of array: "))
# arr=[]
# sum=0
# for i in range(a):
#     e=int(input("Enter element of array: "))
#     arr.append(e)
# for i in arr:
#     sum+=i
# print("Sum of elements of the list is:",sum)



#Reverse elements of a list
# a=int(input("Enter size of array: "))
# arr=[]
# x=[]
# for i in range(a):
#     e=input("Enter element of array: ")
#     arr.append(e)
# x=arr[::-1]
# print(x)



# Largest element of a list with loop
# a=int(input("Enter size of array: "))
# arr=[]
# sum=0
# big=0
# for i in range(a):
#     e=int(input("Enter element of array: "))
#     arr.append(e)
# for i  in arr:
#     if i>big:
#         big=i
# print(big)



#Reverse an element in  a list
# a=int(input("Enter size of array: "))
# x=[]
# revword=''
# for i in range(a):
#     arr=input("Enter element of array: ")
#     x.append(arr)
# index=int(input("Enter the position of word to be reversed: "))
# for i in x[index-1]:
#         revword=i+revword
# print("Reversed word is:",revword)



#Sum of corresponding elements of 2 lists
# a=int(input("Enter size of array: "))
# print()
# x=[]
# y=[]
# res=[]
# for i in range(a):
#     arr1=int(input("Enter elements of 1st array: "))
#     x.append(arr1)
# print()
# for i in range(a):
#     arr2=int(input("Enter elements of 2nd array: "))
#     y.append(arr2)
# print()
# for i in range(a):
#     res.append(x[i]+y[i])
# print("Sum of corresponding elements of both lists is:",res)



#Sorting positive and negative elements in a list
# a=int(input("Enter size of array: "))
# x=[]
# pos=[]
# neg=[]
# for i in range(a):
#     arr=int(input("Enter element of array: "))
#     x.append(arr)
# for i in x:
#     if i<0:
#         neg.append(i)
#     elif i>=0:
#         pos.append(i)
# print("Positive elements of the array:",pos)
# print("Negative elements of the array:",neg)



# Sorting even and odd elements in a list
# a=int(input("Enter size of array: "))
# x=[]
# odd=[]
# even=[]
# for i in range(a):
#     arr=int(input("Enter element of array: "))
#     x.append(arr)
# for i in x:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even elements of the array:",even)
# print("Odd elements of the array:",odd)



#Sorting positive and negative elements from a list within a range
# a=int(input("Enter size of array: "))
# x=[]
# pos=[]
# neg=[]
# for i in range(a):
#     arr=int(input("Enter element of array: "))
#     x.append(arr)
# rb=int(input("Enter range beginning to be searched: "))
# re=int(input("Enter range end to be searched: "))
# for i in x[rb:re]:
#     if i<0:
#         neg.append(i)
#     elif i>=0:
#         pos.append(i)
# print("Positive elements of the array:",pos)
# print("Negative elements of the array:",neg)



#Remove duplicate elements in a list
# a=int(input("Enter size of array: "))
# x=[]
# y=[]
# for i in range(a):
#     arr=input("Enter element of array: ")
#     x.append(arr)
# for i in x:
#     for j in x:
#         if j not in y:
#             y.append(j)
# print("The list after removing duplicate elements is:",y)



#Search an element in a list
# a=int(input("Enter size of array: "))
# x=[]
# for i in range(a):
#     arr=input("Enter element of array: ")
#     x.append(arr)
# s=input("Enter element to search: ")
# for i in x:
#     if i==s:
#         res=True
#         break
#     elif i!=s:
#         res=False
# if res==True:
#     print("Element found in the list")
# else:
#     print("Element not found in the list")



#Find the missing number from a list
# a=int(input("Enter size of array: "))
# x=[]
# for i in range(a):
#     arr=int(input("Enter element of array: "))
#     x.append(arr)
# for i in range(1,len(x)):
#     if x[i]-1!=x[i-1]:
#         val=x[i]-1
#         break
# print("Missing element is:",val)



#Find second largest number in a list
# a=int(input("Enter size of array: "))
# x=[]
# for i in range(a):
#     arr=int(input("Enter element of array: "))
#     x.append(arr)
# big=x[0]
# for i in range(a):
#     for j in range(a-i-1):
#         if x[j]<x[j+1]:
#             x[j],x[j+1]=x[j+1],x[j]
# print("Second largest number in the list is:",x[1])



#Find second smallest number in a list
# a=int(input("Enter size of array: "))
# x=[]
# for i in range(a):
#     arr=int(input("Enter element of array: "))
#     x.append(arr)
# big=x[0]
# for i in range(a):
#     for j in range(a-i-1):
#         if x[j]<x[j+1]:
#             x[j],x[j+1]=x[j+1],x[j]
# print("Second smallest number in the list is:",x[-2])



#Convert integer to word
# num=['zero','one','two','three','four','five','six','seven','eight','nine']
# teen=['ten','eleven','twelve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
# tens=['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
# a=input("Enter a number in the range of 0-99: ")
# if a.isnumeric():
#     if 0<=a<10:
#         print("Entered number is:",num[a])
#     elif 10<=a<20:
#         print("Entered number is:",teen[a//10])
#     elif 20<=a<100:
#         print("Entered number is:",tens[a//10]+'-'+num[a%10])
#     elif a>100 or a<0:
#         print("Entered number is out of range")
# else:
#     print("Entered value is not a number")



#Count no of strings from a given list of strings with length two or more characters and first and last character as same
# a=int(input("Enter size of array: "))
# x=[]
# for i in range(a):
#     arr=input("Enter element of array: ")
#     x.append(arr)
# count=0
# for i in x:
#     if len(i)>=2:
#         if i[0]==i[-1]:
#             count+=1
#     else:
#         print("The element at position",x.index(i)+1,"has length less than 2")
#         yn=input("Do you want to continue excluding this value? (Y/N): ")
#         if yn=='y' or 'Y':
#             continue
#         else:
#             exit()
# print("No of elements with length greater than 2 and same first and last character is:",count)



#2D matrix input with for loop
# mat=[]
# r=int(input("Enter number of rows: "))
# c=int(input("Enter number of columns: "))
# print("Enter values row-wise")
# for i in range(r):
#     a=[]
#     for j in range(c):
#         a.append(int(input()))
#     mat.append(a)
# print()
# #                                                   ------To display matrix------
# print('Entered matrix is: ')
# for i in range(r):
#     for j in range(c):
#         print(mat[i][j],end=' ')
#     print()



#2D matrix addition
# mat1=[]
# mat2=[]
# add=[]
# r=int(input("Enter number of rows: "))
# c=int(input("Enter number of columns: "))
# print("Enter values of first matrix row-wise")
# for i in range(r):
#     a=[]
#     for j in range(c):
#         a.append(int(input()))
#     mat1.append(a)
# print("Enter values of second matrix row-wise")
# for i in range(r):
#     a=[]
#     for j in range(c):
#         a.append(int(input()))
#     mat2.append(a)
# for i in range(r):
#     add.append([0]*c)
# for i in range(r):
#     for j in range(c):
#         add[i][j]=mat1[i][j]+mat2[i][j]
# print('Sum of the matrix is: ')
# for i in range(r):
#     for j in range(c):
#         print(add[i][j],end=' ')
#     print()



#2D matrix transpose
# mat=[]
# t=[]
# r=int(input("Enter the number of rows: "))
# c=int(input("Enter the number of columns: "))
# for i in range(r):
#     a=[]
#     for j in range(c):
#         a.append(int(input()))
#     mat.append(a)
# print('Entered matrix is: ')
# for i in range(r):
#     for j in range(c):
#         print(mat[i][j],end=' ')
#     print()
# for i in range(r):
#     t.append([0]*c)
# for i in range(r):
#     for j in range(c):
#         t[j][i]=mat[i][j]
# print('Transpose of the matrix is: ')
# for i in range(r):
#     for j in range(c):
#         print(t[i][j],end=' ')
#     print()



#Simple calculator
# while True:
#     print("Options")
#     print('1.Addition')
#     print('2.Subtraction')
#     print('3.Multiplication')
#     print('4.Division')
#     print('5.EXIT')
#     choice=int(input("Enter your choice: "))
#     if choice==5:
#         print('Exiting the program')
#         break
#     elif 1<=choice<=4:
#         fst=int(input("Enter first number: "))
#         snd=int(input("Enter second number: "))
#         if choice==1:
#             print("Result of addition is:",fst+snd)
#         if choice==2:
#             print("Result of subtraction is:",fst-snd)
#         if choice==3:
#             print("Result of multiplication is:",fst*snd)
#         if choice==4:
#             if snd!=0:
#                 print("Result of division is:",fst/snd)
#             else:
#                 print("Division cannot be done since the second number is zero")
#     else:
#         print("The choice entered is not valid")



#Dictionary
# d=dict()
# name=input("Enter name: ")
# address=input("Enter address: ")
# phone=input("Enter phone number: ")
# d['name']=name
# d['address']=address
# d['phone']=phone
# print(len(d))



#Enter values to dictionary using for loop
# n=int(input("Enter the number of values to be inserted: "))
# m=int(input("Enter the number of keys in each value: "))
# d={}
# num=1
# x=0
# for i in range(n):
#     for j in range(m):
#         nkey=input('Enter key: ')
#         nvalue=input('Enter value: ')
#         d[num,nkey]=nvalue
#     num+=1
# print(d)


#Find length of words using dictionary comprehension
# string=input("Enter the string: ")
# word_len={word:len(word) for word in string.split()}
# print('Word Length:',word_len)



# Implement a Python program that takes a list of integers and returns a new list where each element is replaced by the sum of its digits. 
# For example, [12, 34, 56] would become [3, 7, 11].
# a=int(input("Enter size of array: "))
# x=[]
# for i in range(a):
#     arr=input("Enter element of array: ")
#     x.append(arr)
# print('The entered list is:',x)
# res=[]
# for i in x:
#     numstr=str(i)
#     digitsum=0
#     for x in numstr:
#         digitsum+=int(x)
#     res.append(digitsum)
# print('The result list is:',res)



# Implement a Python program that calculates the cumulative sum of elements in a list. 
# For example, given , the output should be [1, 3, 6, 10].
# a=int(input("Enter size of array: "))
# x=[]
# for i in range(a):
#     arr=input("Enter element of array: ")
#     x.append(arr)
# print('The entered list is:',x)
# res = []
# cum_sum = 0
# for i in range(len(x)):
#     cum_sum += x[i]
#     res.append(cum_sum)
# print(res)



# Remove all characters from a string except integers.
# a=input("Enter a string: ")
# for i in a:
#     if not i.isnumeric():
#         a=a.replace(i,'')
# print("The string after removing all the characters except integers is:",a)



#Calculate the sum and average of the digits present in a string
# a=input("Enter a string: ")
# sum=0
# length=0
# for i in a:
#     if i.isnumeric():
#         length+=1
#         sum+=int(i)
# avg=sum/length
# print("Sum of the numbers in the string is:",sum)
# print("Average of the numbers in the string is:",avg)



#Append new string in the middle of a given string
# a=input("Enter a string: ")
# x=input("Enter the string to be entered in the middle: ")
# for i in range(len(a)):
#     if i==len(a)//2:
#         b=a[:i]+x+a[i:]
# print(b)



#ATM
# acc=0
# while True:
#     print()
#     print("Menu")
#     print("1.Check Balance")
#     print("2.Cash Deposit")
#     print("3.Cash Withdrawal")
#     print("4.Exit")
#     choice=int(input("Enter your choice: "))
#     if choice==1:
#         print("Current account balance is:",acc)
#     elif choice==2:
#         dep=int(input("Enter the amount to be deposited: "))
#         acc+=dep
#         print("Amount deposited")
#         print("Current account balance is:",acc)
#     elif choice==3:
#         wit=int(input("Enter the amount to be withdrawn: "))
#         acc-=wit
#         print("Amount withdrawn")
#         print("Current account balance is:",acc)
#     elif choice==4:
#         break
#     else:
#         print("Invalid choice entered")



#Create a string made of the first, middle and last character
# str=input("Enter the string: ")
# new_str=str[0]+str[len(str)//2]+str[-1]
# print(new_str)



#Write a Python program to sum all the items in a dictionary.
# dict={}
# dict['mark1']=10
# dict['mark2']=20
# dict['mark3']=20
# dict['mark4']=30
# dict['mark5']=15
# print(dict)
# sum=0
# for i in dict.values():
#     sum+=i
# print("Sum of values=",sum)



#Find smallest or largest number in a list (FUNCTION)
# def largest(a):
#     big=a[0]
#     for i  in arr:
#         if i>big:
#             big=i
#     print("Largest number in the list is:",big)

# def scndlargest(a):
#     big=a[0]
#     for i in range(len(a)):
#         for j in range(len(a)-i-1):
#             if a[j]<a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     print("Second largest number in the list is:",a[1])

# def scndsmallest(a):
#     big=a[0]
#     for i in range(len(a)):
#         for j in range(len(a)-i-1):
#             if a[j]<a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     print("Second smallest number in the list is:",a[-2])

# def smallest(a):
#     small=a[0]
#     for i  in arr:
#         if i<small:
#             small=i
#     print("Smallest number in the list is:",small)

# a=int(input("Enter size of array: "))
# arr=[]
# small=0
# for i in range(a):
#     e=int(input("Enter element of array: "))
#     arr.append(e)
# print()
# print("Menu")
# print("1.Find largest number in the list")
# print("2.Find smallest number in the list")
# print("3.Find second largest number in the list")
# print("4.Find second smallest number in the list")
# print()
# choice=int(input("Enter your choice: "))
# if choice==1:
#     largest(arr)
# elif choice==2:
#     smallest(arr)
# elif choice==3:
#     scndlargest(arr)
# elif choice==4:
#     scndsmallest(arr)




# def func(l):
#     res=[]
#     for i in l:
#         if len(i)>=2 and i[0].lower()=='c' and i[1].lower()=='a':
#             res=res+[i]
#     print("The names that begin with 'ca' are: ",res)

# list=[]
# n=int(input("Enter the no of elements in the list: "))
# print("Enter the elements in the list:")
# for i in range(n):
#     e=input()
#     list.append(e)
# func(list)



# Define a function that accepts lowercase words and returns uppercase words.
# def l_ucase(w):
#     print(w.upper())
# w=input("Enter the word to be converted to uppercase: ")
# l_ucase(w)



# Define a function that accepts radius and returns the area of a circle.
# def area(r):
#     a=3.14159*r*r
#     print("Area of the circle=",a,'m^2')
# r=area(float(input("Enter the radius of the circle(in metres): ")))



# Write a function check the nyear enetred is leap year or not
# def leap(yr):
#     if yr%4==0:
#         print("The year",yr,"is a leap year")
#     else:
#         print("It is not a leap year")
# yr=leap(int(input("Enter the year: ")))



#Factorial using function recurssion
# def fact(n):
#     if n<2:
#         return n
#     else:
#         return n*fact(n-1)
# n=int(input("Enter the number whose factorial is to be calculated: "))
# f=fact(n)
# print(f)



#Sum of values of dictionary using function
# def s(**d):
#     s=0
#     for i in d.values():
#         s+=i
#     return s
# sum=s(a=1,b=2,c=3)
# print(sum)



#Calculator using function
# def add(a,b):
#     s=a+b
#     return s
# def sub(a,b):
#     su=a-b
#     return su
# def mult(a,b):
#     m=a*b
#     return m
# def div(a,b):
#     d=a/b
#     return d
# x=True
# while x==True:
#     print('Menu')
#     print('1.Addition')
#     print('2.Subtraction')
#     print('3.Multiplication')
#     print('4.Division')
#     print('5.Exit')
#     choice=int(input("Enter your choice: "))
#     if 1<=choice<=4:
#         fn=int(input("Enter the first number: "))
#         sn=int(input("Enter the second number: "))
#         if choice==1:
#             s=add(fn,sn)
#             print('Sum of the numbers is:',s)
#         elif choice==2:
#             su=sub(fn,sn)
#             print('Difference of the numbers is:',su)
#         elif choice==3:
#             m=mult(fn,sn)
#             print('Product of the numbers is:',m)
#         elif choice==4:
#             if sn!=0:
#                 d=div(fn,sn)
#                 print('Division of the numbers is:',d)
#             else:
#                 print("The second number entered is zero!")
#     elif choice==5:
#         print("Exiting the program")
#         break
#     else:
#         print("The entered choice is invalid")
#     yn = input("Do you want to continue(Y/N): ")
#     if yn.lower()=='n':
#         x = False
#     elif yn.lower()=='y':
#         x = True
#     else:
#         print("Invalid answer")



#Password
# for i in range(4):
#     p=input("Enter the password: ")
#     if p!='password':
#         print("Invalid password")
#     else:
#         print("Unlocked")
#         break
#     if i==3:
#         print("Too many wrong attempts, try again after 30 seconds")



# l=['flower','flow']
# r=''
# min_len=len(l[0])
# for i in l:
#     if len(i)<min_len:
#         min_len=len(i)
# for i in range(min_len):
#     for j in range(1,len(l)):
#         if l[j][i]!=l[0][i]:
#             break
#     else:
#             r+=l[0][i]
# print(r)



# f=open('file.txt','w')
# f.writelines(['flower','flow'])
# f=open(r"C:\Users\Govind\Desktop\Python\file.txt",'r')
# print(f.read())
# f.close()




# str='aaabbbccc'
# count=1
# l=len(str)
# for i in range(l-1):
#     if str[i]==str[i+1]:
#         count+=1
#     elif str[i]!=str[i+1]:
#         print(count,str[i],end=' ')
#         count=1
#     if i==(l-2):
#         print(count,str[i],end=' ')
#         count=1



# class Car:
#     company="BMW"
#     model="m5"
#     price=12030405
#     color="black"
#     def display_details():
#         print("printing all details")
# a=Car()
# b=Car()



# from py.file1 import add
# v=add(3,80)
# print(v)



# Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         ar=3.14*self.radius*self.radius
#         print("Area= ",ar)
#     def per(self):
#         per=2*3.14*self.radius
#         print("Perimeter= ",per)
# r=int(input("Enter the radius of the circle: "))
# c=Circle(r)
# c.area()
# c.per()



# Python program to create a calculator class. Include methods for basic arithmetic operations
# class Calculator:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def add(self):
#         return self.num1+self.num2
#     def sub(self):
#         return self.num1-self.num2
#     def multi(self):
#         return self.num1*self.num2
#     def div(self):
#         return self.num1/self.num2
# print("MENU")
# print("1.Addition")
# print("2.Subtraction")
# print("3.Multiplication")
# print("4.Division")
# print("5.Exit")
# ch=int(input("Enter your choice: "))
# if 1<=ch<=4:
#     num1=int(input("Enter first number: "))
#     num2=int(input("Enter second number: "))
#     if num2==0:
#         print("Second number is zero")
#     else:
#         if ch==1:
#             cal=Calculator(num1,num2)
#             print("Sum of the numbers is:",cal.add())
#         elif ch==2:
#             cal=Calculator(num1,num2)
#             print("Difference of the numbers is:",cal.sub())
#         elif ch==3:
#             cal=Calculator(num1,num2)
#             print("Product of the numbers is:",cal.multi())
#         elif ch==4:
#             cal=Calculator(num1,num2)
#             print("Division of the numbers is:",cal.div())
# elif ch==5:
#     exit
# else:
#     print("Invalid choice")



# Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, rectangle, and square.
# class Shape:
#     class Circle:
#         def __init__(self,radius):
#             self.radius=radius
#         def area(self):
#             return 3.14*self.radius**2
#         def peri(self):
#             return 2*3.14*self.radius
#     class Square:
#         def __init__(self,side):
#             self.side=side
#         def area(self):
#             return self.side**2
#         def peri(self):
#             return 4*self.side
#     class Rectangle:
#         def __init__(self,l,b):
#             self.l=l
#             self.b=b
#         def area(self):
#             return self.l*self.b
#         def peri(self):
#             return 2*(self.l+self.b)
# print("MENU")
# print("1.Circle")
# print("2.Square")
# print("3.Rectangle")
# ch=int(input("Enter your choice: "))
# if 1<=ch<=3:
#     if ch==1:
#         r=int(input("Enter the radius of the circle:"))
#         c=Shape.Circle(r)
#         print("Area of the circle=",c.area())
#         print("Perimeter of the circle=",c.peri())
#     if ch==2:
#         s=int(input("Enter the side length: "))
#         sq=Shape.Square(s)
#         print("Area of the square=",sq.area())
#         print("Perimeter of the square=",sq.peri())
#     if ch==3:
#         l=int(input("Enter the length: "))
#         b=int(input("Enter the breadth: "))
#         re=Shape.Rectangle(l,b)
#         print("Area of the square=",re.area())
#         print("Perimeter of the square=",re.peri())
# else:
#     print("Invalid choice")



# Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
# class Cart:
#     def __init__(self,item,p,n,num,r):
#         self.item=item
#         self.qp={}
#         self.qp['Quantity']=n
#         self.qp['Price']=p
#         self.num=num
#         self.r=r
#     def add(self):
#         for j in range(self.num):
#             cart[self.item]=self.qp
#         return cart
#     def remove(self):
#         del cart[self.r]
#         return cart

# x=True
# while x==True:
#     print("MENU")
#     print("1.Add Item")
#     print("2.Remove Item")
#     ch=int(input("Enter your choice: "))
#     total=0
#     if 1<=ch<=2:
#         if ch==1:
#             cart={}
#             num=int(input("Enter number of item to be added to the cart: "))
#             for i in range(num):
#                 item=input("Enter the item: ")
#                 n=int(input("Enter the quantity of item: "))
#                 p=int(input("Enter price of the item: "))
#                 total+=p*n
#                 a=Cart(item,p,n,num,0)
#                 a.add()
#             print("Current items in the cart are: ",a.add())
#             print("Total price of the cart=",total)
#         elif ch==2:
#             print("Current items in the cart are: ",cart)
#             for i in cart:
#                 total=total+cart[i]['Quantity']*cart[i]['Price']
#             print('Total price of the cart=',total)
#             r=input("Enter item to be removed from the cart: ")
#             total=total-(cart[r]['Quantity']*cart[r]['Price'])
#             re=Cart(0,0,0,0,r)
#             print("Remaining items in the cart are:",re.remove())
#             print("Total price of the cart is: ",total)
#     else:
#         print("Invalid choice")
#     yn=input('Do you want to continue(Y/N)?: ')
#     if yn=='Y' or yn=='y':
#         x=True
#     elif yn=='N' or yn=='n':
#         print('Exiting the program')
#         x=False
#     else:
#         print('Invalid input, exiting the program')
#         break



# Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.
# class Bank:
#     def __init__(self,name,accno,accbal,ndisp,w,d):
#         self.name=name
#         self.det={}
#         self.accno=accno
#         self.accbal=accbal
#         self.ndisp=ndisp
#         self.w=w
#         self.d=d
#         self.det['Account number']=self.accno
#         self.det['Account balance']=self.accbal
#     def add_det(self):
#         bank[self.name]=self.det
#     def display_det(self):
#         for i in bank.keys():
#             if i==self.name:
#                 print("Account holder name: ",i.upper())
#                 for j,k in bank[i].items():
#                     print(j,':',k)
#                 break
#         else:
#             print("The account holder does not exist")
#     def cash_withdraw(self):
#         for i in bank.keys():
#             if i==self.name:
#                 print("Cash withdrawn")
#                 print("Remaining balance=",bank[i]['Account balance']-self.w)
#     def cash_deposit(self):
#         for i in bank.keys():
#             if i==self.name:
#                 print("Cash deposited")
#                 print("Remaining balance=",bank[i]['Account balance']+self.d)

# bank={}
# x=True
# while x==True:
#     print("MENU")
#     print("1.Enter new account details")
#     print("2.Display account details")
#     print("3.Transaction")
#     ch=int(input("Enter your choice: "))
#     if 1<=ch<=3:
#         if ch==1:
#             name=input("Enter account holder's name: ")
#             accno=int(input("Enter account number: "))
#             accbal=int(input("Enter account balance: "))
#             add=Bank(name,accno,accbal,0,0,0)
#             add.add_det()
#             print("Details added successfully!")
#         if ch==2:
#             print("1.Display all accounts")
#             print("2.Display a specific account")
#             ch1=int(input("Enter your choice: "))
#             if ch1==1:
#                 print()
#                 for i in bank.keys():
#                     print("Acoount holder name:",i.upper())
#                     for j,k in bank[i].items():
#                         print(j,':',k)
#             elif ch1==2:
#                 ndisp=input("Enter name of account holder: ")
#                 disp=Bank(ndisp,0,0,0,0,0)
#                 disp.display_det()
#         if ch==3:
#             print("1.Cash withdrawal")
#             print("2.Cash deposit")
#             ch2=int(input("Enter your choice: "))
#             n=input("Enter account holder name: ")
#             print()
#             if n in bank.keys():
#                 if ch2==1:
#                     print("Cash Withdrawal")
#                     for i in bank.keys():
#                         if i==n:
#                             print("Current balance=",bank[i]['Account balance'])
#                     w=int(input("Enter amount to be withdrawn: "))
#                     print()
#                     withdraw=Bank(n,0,0,0,w,0)   
#                     withdraw.cash_withdraw()  
#                 elif ch2==2:
#                     print("Cash Deposit")
#                     for i in bank.keys():
#                         if i==n:
#                             print("Current balance=",bank[i]['Account balance'])
#                     d=int(input("Enter amount to be deposited: "))
#                     print()
#                     deposit=Bank(n,0,0,0,0,d)   
#                     deposit.cash_deposit()
#             else:
#                 print("The account holder does not exist")
#     else:
#         print("Invalid choice")
#     print()
#     yn=input('Do you want to continue(Y/N)?: ')
#     if yn=='Y' or yn=='y':
#         x=True
#     elif yn=='N' or yn=='n':
#         print('Exiting the program')
#         x=False
#     else:
#         print('Invalid input, exiting the program')
#         break