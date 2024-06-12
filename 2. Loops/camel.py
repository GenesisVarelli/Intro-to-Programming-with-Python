def name(camelcase):

    snakecase = []

    for letter in camelcase:

        if letter.isupper():
            # Append an underscore and the lowercase version
            snakecase.append('_')
            snakecase.append(letter.lower())

        else:
            snakecase.append(letter)

    # Join the list into a string and return it
    return ''.join(snakecase)

# Prompt the user for a camelCase variable name
name_input = input("Enter name: ")


# Convert to snake_case and print the result
name_output = name(name_input)
print("Camel case: ",name_output)