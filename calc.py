num_1= int(input("Enter 1st Number: "))
num_2= int(input("Enter 2nd Number: "))
opreation = input("Select + or - or / or * or ** :")
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



print ("Result is:", result) 