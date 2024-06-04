def main():
    #Get user input
    message = input("Enter text message: ")

    #Call convert function
    result = convert(message)

    #Print the result
    print(result)

def convert(message):
    #Replace ":)" with "🙂" emoji
    message1 = message.replace(":)", "🙂")

    #Replace ":(" with "🙁" emoji
    message2 = message1.replace(":(","🙁")


    return message2


    print(message)


main()