#Prompts the user for an arithmetic expression
a_expression = input("Enter Expression? ")

#Convert into variables
x, y, z = a_expression.split(" ")

#convert varibales to x and z to float
convert_x = float(x)
convert_z = float(z)

    #Calculate
if y == "+":
    result = convert_x + convert_z
if y == "-":
        result = convert_x - convert_z
if y == "*":
    result = convert_x * convert_z
if y == "/":
    result = convert_x / convert_z

#Outputs the result as a floating-point value formatted to one decimal place
print(round(result, 1))
