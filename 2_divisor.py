#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
while True:
    try:
        num = int(input('Enter a number: '))
        if num < 0:
            print("Please enter a non-negative number.")
        else:
            print("Divisors of", num, "are:")
            for i in range(1, num + 1):
                if num % i == 0:
                    print(i)

        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using the program.")
            break
    except ValueError:
        print("Invalid input. Please enter a valid numerical value.")

