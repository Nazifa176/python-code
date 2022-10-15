# user_input = (int(input('enter a number: ')))
# user_input = 5
# i = 0
# sum = 0
# while i <= user_input:
#     sum = sum + i
#     i = i + 1
#     print(i)

    
# print (sum)  



user_input = (int(input('enter a number: '))) 
result = 0
for i in range(1,user_input+1,1):
    if i <= user_input :
        result = result + i
      
        print(i)
        
print (result) 
