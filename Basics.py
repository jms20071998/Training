#https://meet.google.com/zxk-pzvp-ybu
# #1. Add, sub, mul and div
# a = 10
# b = 5
# c = a + b
# d = a - b
# e = a * b
# f = a / b
# print(c)
# print(d)
# print(e)
# print(f)
from itertools import count

#-----------------------------------------------------------------------
#2. Variables
# name = 'Keerti'
# age = 24
# cgpa = 8.2
# print("Name:", name , "Age: ", age , "CGPA: ", cgpa)

#3.
# num1 = float(input("Enter a number: "))
# num2 = float(input("Enter another number: "))
# sum = num1 + num2
# print("sum of num1 and num2 is: ", sum)
#-------------------------------------------------------------------------
#4. List
# List = [10, 60, 30, 110, 50]
# print(List)             #printing the list
# print(len(List))        #printing the length of list
# List.sort()             #sorting in ascending order
# print(List)

# num = [11,13,14,12]
# num.reverse()          #reversing the list in same order
# print(num)
# num.sort(reverse=True)      #reversing the list in descending order
# print(num)
# num.append(15)      #adding single to the list
# print(num)
# num.remove(13)      #removing single value from the list
# print(num)
# num.append([5,10,15])       #appending list
# print(num)

# L = [10, 60, 30, 110, 50]
# m = sorted(L)             #
# print(m)

# Fruits = ['apples','oranges', 'banana']
# Vegetables = ['Onion','Carrots']
# Fruits.insert(1, 'gauva')     #inserting value to the mentioned position
# print(Fruits)
# Fruits.extend(Vegetables)     #adding 2nd list to the tail of 1st list
# print(Fruits)

# num = [11,13,14,12, 12]
# print(min(num))         #min value of list
# print(max(num))         #max value of list
# print(num.count(12))      #count of mentioned value from list
# print(num.index(12))      #printing the index of mentioned value
# del num[1]               #deleting the value of mentioned index from list
# print(num)
# print(11 in num)          #to check whether value is present or not
# print(20 in num)
# num.clear()               #to make list empty
# print(num)

# list1 = [1,2,3,4,5]
# list2 = [1,2,3,5,4]
# print(list1 == list2)
# Fruits1 = ['apple', 'banana', 'orange']
# Fruits2 = ['apple', 'banana', 'orange']
# print(Fruits1 == Fruits2)

#--------------------------------------------------------------------------
#Set
#1.
# a = {1,2,3,4,5}
# print(len(a))       #to check len of set
# a.add(9)            #adding value to set
# print(a)
# a.update({6,7})     #adding new set to the existing one
# print(a)
# a.update([10,11])   #adding new list to the existing set
# print(a)
# a.remove(2)         #removing mentioned value from a set & if mentioned value is not there in set, it throws err
# print(a)
# a.discard(99)       #removing mentioned value from a set & if mentioned value is not there in set, it ll ignore & print the existing set
# print(a)
# a.pop()
# print(a)

# ele = {10,20,30,40}
# ele.copy()
# print(ele)
# ele.clear()
# print(ele)

# a = {1,2,3,4,5, 6,7}
# b = {1,2,3,4,5,8,9}
# print(a.intersection(b))
# print(a.union(b))
# print(a. (b)) #or print(a-b)
# print(a^b)      #print(a.symmetric_difference(b))
# print(a == b)
# print(a != b)
# print(4 in a)
# print(14 in a)

# x = 10.1
# print(set(x))             #cant convert integer or float to set
# str = 'hello'
# print(set(str))             #converting string to set
# y = [1,2,3]
# z = set(y)                 #converting list to set
# print(z)
# z.update('good')            #adding string to set
# print(z)
# z.update((4,5,6))           #converting tuple & adding to existing set
# print(z)

#-----------------------------------------------------------------------------------
#Dictionary
# a = {1: "java", 3: "python", 5: "c" , 4: "python"}
# print(a)
# print(a.get(1))
# print(a.keys())
# print(a.values())
# print(a.items())
# a.update({2: "js", 6: "c#"})
# print(a)
# b = a.copy()
# print(b)
# b.clear()
# print(b)
# print(a)
# a.pop(3)        #--->passing key in argument
# print(a)
# a.popitem()
# print(a)
# a[2] = "html"
# print(a)
# for i in a.items():
#     print(i)
#----------------------------------------------------------------------------
#Tuple
a = (10, 20, 30, 40, 50)
# print(len(a))
# print(a[0])
# print(a[1:])        #slice operator
# print(a[-3])
# print(a.index(40))
#print(a+5.0)       #throws err,because we can't add integer, float, str values to the tuple
#print(a+'python')
# print(a+(60,70,80,90))      #can able to add only tuples to tuple
# a[0] =100
# print(a)            #We can't replace the value in tuple because all the values are constant.
# print(min(a))
# print(max(a))
#----------------------------------------------------------------------------
#for, while, break, continue
# for loop: -> How many times we want to iterate, used to loop over a sequence( list, tuple, string, range)
# Fruits = ['Apple', 'Orange', 'Banana', 'Mango']
# for fruit in Fruits:
#     print(fruit)

# while:->  We don't know how many times the loop should run. It will run until a condition becomes false.
# Manually we have to update the variable i.e., to control it.
# count = 1
# while count < 5:
#     print(count)
#     count += 1

# # Using break to exit a loop
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# Use continue to skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue        # it will be used inside the loop for the current iteration. And it jumps to next iteration
    print(i)










