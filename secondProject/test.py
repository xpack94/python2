#from random import random as r
import os



import random
import math
'''
num1,operator, num2= input("enter numbers and an operator ").split()
num1=int(num1)
num2=int(num2)

if operator=='+':
    print('{} + {} ={}'.format(num1, num2, num1+num2))
elif operator =='-':
    print('{} - {} ={}'.format(num1, num2, num1-num2))
elif operator =='/':
    print('{} / {} ={}'.format(num1, num2, num1/num2))
elif operator =='*':
    print('{} * {} ={}'.format(num1, num2, num1*num2))

'''

# for i in range(11):
#     if i%2==0:
#         print('{} is an even number '.format(i))
#     else :
#         print('{} is an odd number  '.format(i))
#
#
#
# f =float(input("enter a float number "))
# print(" rounding the float to 2 decimals : {:.2f}".format(f))


# def is_even(k):
#   return k


# data =[1,5,2,3,4]
# for i in range(len(data)):
#     k=r.randrange(len(data))
#     print(is_even(data[k]))



# def tree():
#  rows=int(input("enter the number of rows "))
#  spaces =rows-1
#  hashes=1
#
#  for i in range(rows) :
#      for k in range(spaces):
#          print(" ",end="")
#      for k in range(hashes):
#          print("#", end="")
#
#      print("")
#
#
#      hashes+=2
#      spaces-=1


#
#
# tree()

# try :
#     number=int(input("enter a number "))
#     print(number)
# except ValueError:
#     print("you didn't enter a number ")

#
# message=input("enter a message in uppercase")
# secret_message=""
# new_string=""
#
# for i in range(0,len(message)):
#     secret_message+=str(ord(message[i]))
# for i in range(0,len(secret_message),2):
#     new_string+=str(chr(int(secret_message[i:i+2])+32))
#
#
#
#
#
#
# print("the secret message ", secret_message)
# print("the new word is ",new_string)




#
# string = str(input("enter a string to convert into an accronym"))
# index1,index2=0,string.find(" ")
# accronym=string[0]
# number_of_spaces=string.count(" ")
# for i in range(number_of_spaces):
#
#
#     try:
#         index2+=1
#         index1 = index2
#         index2=string.find(" ",index2)
#         accronym += string[index1]
#     except :
#         break
#
#     if string[i]==".":
#         break
#
#
#
# print(accronym.upper())





#
# def equation():
#     equation=str(input("enter an equation 1st degre to solve"))
#     equal = equation.find("=") + 1
#     if equation.find("+")!=-1:
#         number = equation.find("+") + 1
#         result=int(equation[equal])-int(equation[number])
#     elif equation.find("-")!=-1:
#         number = equation.find("-") + 1
#         result = int(equation[equal] )+ int(equation[number])
#
#     return result
#
#
# print(equation())




# muliList=[[0]*9 for i in range(9)]
# inc=1
# inc2=inc
# for i in range(9):
#     for j in range(9):
#        muliList[i][j]+=inc
#        inc+=inc2
#
#     inc=inc2+1
#     inc2=inc
#
#
# for i in range(9):
#     for j in range(9):
#         print(muliList[i][j], end=",")
#     print()


#
# custumer={}
# counter=0;
# while input("enter a custumer y/n ")=="y":
#     counter+=1
#     try:
#        custumer["cust"+str(counter)]=input("enter the name ")
#     except ValueError:
#         print("error")
#
#
#
# for i,k in custumer.items():
#     print(i,k)



# customer =[]
#
# response=input("wanna add a custumor? y/n")
#
# while response[0]=="y":
#     fName,lName=input("enter the first and last Name of the customer ").split()
#     customer.append({fName:lName})
#     response = input("wanna add a custumor? y/n")
#
#
# for i in customer:
#     print(fName,i[fName])


#
#
# def fib(number):
#     if number==0:
#         return 0
#     elif number==1:
#         return 1
#     else:
#         return fib(number-1)+fib(number-2)
#
#
#
#
# try:
#     number=int(input("enter the number of fibonacci that you wanna have "))
#     with open("/home/xpack/Desktop/testFile3.txt", mode="w", encoding="utf-8") as myFile:
#         for i in range(number):
#             myFile.write("fib {} = {} \n".format(i, fib(i)))
#
#     with open("/home/xpack/Desktop/testFile3.txt", encoding="utf-8") as myFile:
#         print(myFile.read())
# except ValueError:
#     print("you didn't enter a number")


print([4]+[3])






