# 2. Calculate the sum of all numbers from 1 to given number. 
# Expected output:
# Dhoren user input dise 5 tahole 1+2+3+4+5 hobe r sum hobe 15 sum tai output e dekhate hobe.



user_input = (int(input('enter a number: '))) 
result = 0
for i in range(1,user_input+1,1):
    if i <= user_input :
        result = result + i
        print(i)
        
print (result)   

    