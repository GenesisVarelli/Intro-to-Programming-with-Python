#Main function - Acts as the point of Execution
def main():

    #Get user input for Dollars
    dollars = dollars_to_float(input("how much was the meal? "))

    #Get user input for percentage
    percent = percent_to_float(input("What percentage would you like to tip? "))

    #Tip Calculation = cost of meal x tip
    tip = dollars * percent

    #Print using the f' string literals method
    print(f"Leave ${tip:.2f}")

#2nd function converts a string to a float
def dollars_to_float(d):
    d = d.replace("$","")
    return float(d)

#3rd function converts a string to a float
def percent_to_float(p):
    p = p.replace("%","")
    return float(p) / 100.0


main()