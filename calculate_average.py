# Write a program to calculate the average of numbers entered by the user until they type "stop".



def calculate_average():
    total = 0
    count = 0

    while True:
        user_input = input("Enter a number (or type 'stop' to finish): ")

        if user_input.lower() == 'stop':
            break

        try:
            number = float(user_input)
            total += number
            count += 1
        except ValueError:
            print("Please enter a valid number or 'stop' to finish.")

    if count == 0:
        print("No numbers were entered.")
    else:
        average = total / count
        print(f"The average of the entered numbers is: {average}")

if __name__ == "__main__": ()