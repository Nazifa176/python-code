# 3. Write a program to print multiplication table of a given number.
# Expected output:
# Dhoren number input dise user 2 tahole output e ashbe
# 2
# 4
# 6
# 8
# 10
# 12
# 14 
# Jodi 3 input dey tahole ashbe 
# 3
# 6
# 9
# 12
# 15

user_input = int(input('enter a number: '))

multiplication_result = 0

for i in range(1,11):
    multiplication_result = (i*user_input)
    i = i + 1
    print (multiplication_result)
    