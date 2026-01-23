# # movies = []


# # movies.append(input("Enter your First Movie :"))
# # movies.append(input("Enter your second Movie :"))
# # movies.append(input("Enter your third Movie :"))

# # print(movies)


# #  prac = ["A","B", "C","A","A","B", "C","A", ]
# # prac.sort
# # print(prac 
# #       )

# # count = 1 
# # while count <= 10:
# #     print(3*count)
# #     count+=1
    

# # nums = [1, 4 , 9 ,16, 25, 36, 49, 64, 81, 100]
# # while nums<=5:
# #         print(nums)
# #         nums+=1
 
# # heros = ["ironman", "captain_america", "thor", "black_panther", "dr_strange", "spider_man"]

# # print all numbers
# # for num in nums:
# #     print(num)
# # nums = [1, 4 , 9 ,16, 25, 36, 49, 64, 81, 100]
# # x= 36
# # i = 0
# # if (nums [i]==x):
# #     print("Found at Idx")
# #     beack
# # else :
# #     print("finding..")
# #     i+=1

# # print("End Of Loop ")

# #     nums = [1 , 1, 1,1 1,1 ,1,1 1,1 1,1, 1]

# # a = 5
# # b = 6

# #bitwise and
# # print(a & b)
# # a = 101
# # b = 110

# # Bitwise or
# # print(a|b)

# # Bitwise XOR
# # print(a^b)

# # Left shift
# # print(a<<2)

# # Right shift
# # print(a>>1)

# # 
# # 

# # coditional statements

# # 1. simple if
# # age = int(input("enter your age"))
# # if age > 18:
# #     print("you are eligible to give vote")
    
# # 2. simple if - else
# # if age> 18:
# #     print("you are able to do job")
# # else:
# #     print("you are not able to do this job")
    
# # 3. elif conditional statement
# marks = int(input("enter your marks :"))
# if marks >=90 or marks<100:
#     print("Grade A+")
# elif marks >= 80 or marks < 90:
#     print("Grade : A ")
# else:
#     print("No placement")


#WAF to print thte length of a list(list is the parameter) 

# cities = ["jaipur","ajmer","uaipur","bikaner","pali"]
# heros = ["ironman","batman","thor","captain_america","black_panther"]

# def print_somthing(list):
#     print(len(list))
#     return list
    
# print_somthing(cities)
# print_somthing(heros)

#WAF to print the element of a list in a single line .(list is a parameter)

# a = "2"
# b = 4.25
# print(int(a) + b)


# day = input("enter weather condition :")
# is_dost_available = True
# if day == "sunny" or day == "cloudy":
#     if is_dost_available :
#         print("hum khel sakte hain.")
#     else:
#         print("dost hi nahin hain.")
# else:
#      print("din hi achha nahin hain.")

# eng = int(input("enter mark"))
# hin= int(input("enter mark"))
# math= int(input("enter mark"))

# avg = (eng + hin+ math)/3
# if avg >90:
#     print("exellent")
# elif avg<90 and avg >= 75:
#     print("good")
# elif avg < 75 and avg >= 60:
#     print("average")
# else:
#     print("fail")
        
# new start
# 
# 
# 
# 
# 



# operaters 
# a = 10 (operand)
# b = 20 (operand)

# operand = Value



  
#calculate value from user 

# a= int (input("enter first number :"))
# b = int(input("enter second number : "))
# sign = input("enter operator :")

# if sign == '+':
#     print("the sum :",a+b)
# elif sign == '-':
#     if a>b:
#         print(a-b)
#     else: 
#         print(b-a)    
# elif sign == '*':
#     print("the mlt :",a*b)
# elif sign=='/':
#     if (a==0) and (b==0):
#         print("plzz don't use zero")
#     else:    
#         print("the divison :",a/b)
# else: 
#     print("invalid operator")    
    
    
    
#income tax calculate question


# salary = int(input("enter your salary :"))

# if salary < 250000:
#     print("NO TAX") 
# elif (salary >= 250000) and (salary < 500000):
#     print(salary * 0.05 )  
# elif(salary >= 500000)  and (salary <1000000):
#     print(salary * 0.20)   
# elif(salary >1000000):
#     print(salary *0.30)    
# else:
#     print("error") 


# create food menu for customer

# print("     MENU        ")
# print(" 1. pizza Rs: 200")
# print(" 2. burger Rs: 150") 
# print(" 3. sandwish Rs: 100") 
    
 
# choice = int(input("enter food number: "))
# if choice== 1 :
#     item = "pizza"
#     cost = 200
    
# elif choice == 2 :
#     item = "burger"
#     cost = 150   
# elif choice == 3 :
#     item = "sandwish"
#     cost = 100 
# else : 
#     print("invalid food number") 
        
# print(f'selected food : {item}')
# print(f'total cost : {cost}')
# print("thansk you for your order")                


# LOOPS =  loops are the used to run the particular part of (block of the code )multiple times 

#start -> inclusive 
#end -> exclusive n-1
# range (start , end , step) -> range is a bultin function which is use to give a sequence of number in a range. 


# print 1 to 10 number with for loops 
# for i in range (1,11):
#     print(i)


# print A to Z by for loops
# for i in range (26):
#     print(chr(65+i), end = ' ')

# print every third number in a range 1 to 100 
# for i in range (0, 101 , 3):
#     print(i)
    
# print every second number in a range of 200 to 300
# for i in range (200, 301 , 2):
#     print(i)
    
 # print even number in a given range 200 , 400
# for i in range (200, 401):
#     if i % 2 ==0:
#         print(i) 


# WHILE LOOPS :- this loops runs on conditions (tille yhe conditions is True). we use the while loops when we don't know the number of iteration to be run by the loop .

# toffee = 10
# while toffee!=0:
#     print("over")
#     toffee = toffee -1



# n =  1 
# while n <5:
#     print(n)
#     n = n+1

# n = 1 
# sum = 0
# while n<=5:
#     sum = sum + n 
#     n = n +1
#     print(sum)

# print reverse natural number 
# n = 10
# while n>0:
#     print(n)
#     n= n-1

# print all the characters from A to Z
# i= 0
# while i < 26:
#     print(chr(65+i), end= ' ')
#     i = i+1

# sum of all odd number in a range 1 to 100

# n = 1
# sum = 0
# while n <= 100:
#     if n % 2 != 0:     
#         sum = sum + n
#     n = n + 1          
# print(sum)


# n = 123
# rev = 0 
# while n !=0:
#     digit = n %10
#     rev = rev *10+digit
#     n = n//10
# print(rev)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    greater = a
else:
    greater = b

while True:
    if greater % a == 0 and greater % b == 0:
        lcm = greater
        break
    greater += 1

print("LCM =", lcm)

        


    