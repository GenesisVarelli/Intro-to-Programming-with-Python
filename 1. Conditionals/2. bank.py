#Get user input
greeting = input("Enter greeting: ").lower().strip()

#greeting is 'hello'
if "hello" in greeting:
            print("$0")

#greeting starts with a 'H'
elif 'h' == greeting[0]:
            print("$20")

#Otherwise, print $100
else:
    print("$100")