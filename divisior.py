#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
num = int(input('Enter the number: '))
for i in range(1, 9):
    result = num / i
    if num % i == 0:
        print(result)




