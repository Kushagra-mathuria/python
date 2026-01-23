# 1. write a program to check whether a number is negative, positiveor zero.
# num = int(input("Enter any number :"))
# if num>0:
#     print("positive")
# elif num ==0:
#     print("zero")
# else :
#     print("negative")

# # 
# 2. write a program to check if a number is even or odd:
# num = int(input("Enter any number :"))
# if num %2==0:
#     print("even number")
# else:
#     print("odd number")    

# # 
# 3.write a program to check whether a person is eligible to vote (age=>18):
# age = int(input("enter your age"))
# if age>=18:
#     print("eligible to vote")
# else :
#     print("not eligible to vote")
    
# # 
# 4. write a program to find the largest of two numbers:
# num1=int(input("enter a number :"))
# num2=int(input("enter a number:"))
# if num1>num2:
#     print("num1 is greater")
# else:
#     print("")

# # 
# first_name = input("Enter first name : ").title
# last_name = input("enter last name : ").title
# age= 20

# full_name= first_name + last_name

# print(f"hello my name is {} . my age is {}".format(full_name,age))q9

# # 
# s = "abc123"
# countdigit= 0
# countalpha= 0
# for ch in s :
#     if ch.isdigit():
#         countdigit+=1
#     elif ch.isalpha():
#         countalpha +=1
#     else: 
#         pass
# print(countdigit)
# print(countalpha)    
        

# # 
# s=input("enter any character:")
# countvowel=0
# countconsonant=0
# countdigit=0
# countspecial=0
# vowel ="aeiouAEIOU"

#  for ch in s:
#     if ch.isalpha():
#         if ch in vowel:
#             countvowel+=1
#         else:
#             countconsonant+=1
#     elif ch.isdigit():
#         countdigit+=1
#     else:
#         countspecial+=1
        
#     print("no. of vowels",countvowel)
#     print("no. of consonant",countconsonant)
#     print("no of special character",countspecial)
#     print("no of digits",countdigit)         

# # 
# s = "a2b3c4"
# sum = 0

# for ch in s:
#     if ch.isdigit():
#         sum+=ch
#     else:
#         pass
# print(sum)  


# st ="abcd"
# st1= ' '
# for i in range(0, len(st)):
#     if i%2==0:
#         st1 = st1 +st(i).upper()
#     else:
#     st1 = st1 +st(i)

# #   
# sent = "this is a sentence"
# words = sent.split() 
# maxlen = 0
# for word in words:
#     if maxlen < len(word):
#         maxlen = len(word)

# for word in words:
#     if maxlen == len(word):
#         print(word)
#         break


# #  Q .. password validator
# # len = 8
# # it should contain = lowercase,uppercase,digit,symbol
# # if it contain all the thing = give it strong password
# # else weak password
# ans===

# password = input("Enter password: ")

# has_upper = False
# has_lower = False
# has_digit = False
# has_special = False

# special_chars = "@#$%&*?"

# if len(password) >= 8:
#     for ch in password:
#         if ch.isupper():
#             has_upper = True
#         elif ch.islower():
#             has_lower = True
#         elif ch.isdigit():
#             has_digit = True
#         elif ch in special_chars:
#             has_special = True

# if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
#     print("Password is Strong ")
# else:
#     print("Password is Weak ")
#     if not len(password):
#         print("password must be contain at least 8 characters" )
#     elif not has_upper:
#         print("password should have at least one uppercasw letter")
#     elif not has_lower:
#         print("password should have at least one lowercase letter")


cmd;


















































