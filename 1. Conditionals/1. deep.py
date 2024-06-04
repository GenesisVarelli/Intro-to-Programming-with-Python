#Prompt User input?
deep = input("What is the Answer to the Great Question of Life, the Universe, and Everything?" )

#Print 'Yes' if the user inputs 42 or (case-insensitively) forty-two or forty two
if deep.strip() == "42":
    print("Yes")
elif deep.lower().strip() == "forty-two" or "forty two":
     print("Yes")

#Otherwise output No.
else:
     print("No")