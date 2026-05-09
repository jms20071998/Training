#check whether given number is even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num, "is even number")
# else:
#     print(num, "is odd number")

# pgm to check whether the number is positive or negative
# num = int(input("Enter a number: "))
# if num > 0:
#     print(num ," is positive")
# elif num < 0:
#     print(num ," is negative")
# else:
#     print(" given number is zero")

#ATM Prgm
# bal = 100
# print("press 1 to check balance\npress 2 to withdraw amount\npress 3 to deposit amount\npress 4 to exit")
# choice = int(input("Enter your choice: "))
# if choice == 1:
#     print("Current balance: ", bal)
# elif choice == 2:
#     wd = int(input("Enter the amount you want to withdraw: "))
#     bal -= wd
#     print(wd, "is successfully withdrawn")
#     print("Current balance: ", bal)
# elif choice == 3:
#     dp = int(input("Enter the amount you want to deposit: "))
#     bal += dp
#     print(dp, "is successfully deposited")
#     print("Current balance: ", bal)
# elif choice == 4:
#     print("Thank you for using our service")

#1.Remove duplicate in a string
# str1 = ""
# s = input("Enter a string: ")
# for char in s:
#     if char not in str1:
#         str1 += char
# print(str1)

# 2.Find the occurrences in a string
s1 = ""
c = 0
s = input("Enter a string: ")
for char in s:
    if char not in s1:
        c += 1
        s1 += char
    print(f"{char} : {c}")
# for char in s1:
#     print(f"{char} : {c}")

