
# 4. Write a program to display only those number from a list that satisfy the following conditions:
# - the number must be divisible by 5.
# - if the number is gretter than 150, then skip it and move to the next number.
# - if the number is gretter than 500, then stop the loop

thislist = [1,2,8,9,10,110,120,1300,1400,1500,160,170,1800]

for i in thislist:

    if i > 500 : 
        break
    elif i > 150 :
        continue
    elif i % 5 == 0:
       print(i)

   
