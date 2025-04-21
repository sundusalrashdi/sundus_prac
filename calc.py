num_1= int(input("Enter 1st Number: "))
num_2= int(input("Enter 2nd Number: "))
opreation = input("Select + or - or / or * or ** or ! or absolute or (OR) | or (AND) & :") 
result =0 


if opreation == "+":
    result = num_1 + num_2

elif opreation == "-":
    result = num_1 - num_2

elif opreation == "/":
    result = num_1 / num_2 

elif opreation == "*":
    result = num_1 * num_2

elif opreation == "**":
    result = num_1 ** num_2

elif opreation == "!":
     result =1 

     for i in range(1,num_1+1): 
         result=result*i 

elif opreation == "absolute":
     result = abs(num_1)  

elif opreation == "|":
     result = num_1 | num_2 

elif opreation == "&":
     result = num_1 & num_2 

print ("Result is:", result) 