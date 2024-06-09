def main():
    #prompt user for  time
    mealtime = input("What time is it? ").strip()

    time = convert(mealtime)

    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print('lunch time')
    elif 18 <= time <= 19:
        print('dinner time')
    else:
        pass

def convert(time):
     # Get hours and minutes
     hours, minutes = time.split(":")
     # Convert time into a float number
     minutes_new = float(minutes) / 60
    # Return the result to main function
     return float(hours) + minutes_new

if __name__ == "__main__":
    main()
