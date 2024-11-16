#Write a Python program that prints all even numbers between 1 and 20 using a
#for loop.

# Loop through the range from 1 to 20
for num in range(1, 21):
    # Check if the number is even
    if num % 2 == 0:
        print(num)
        
        
        


# Use a while loop to ask the user to input a number until they provide a
#number greater than 10.

while True:
    number = int(input("Please enter a number greater than 10: "))
    if number > 10:
        print(f"Thank you! You entered {number}.")
        break
    else:
        print("The number is not greater than 10. Please try again.")
        
        
        


#Write a program that prints the multiplication table (from 1 to 10) for numbers
#from 1 to 5 using nested for loops.

# Outer loop to iterate through numbers 1 to 5
for i in range(1, 6):
    print(f"Multiplication table for {i}:")
    
    # Inner loop to iterate through numbers 1 to 10
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    
    # Add a blank line for separation after each table
    print()






#Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a
#for loop to find the sum of all odd numbers and print the result.

numbers = [4, 7, 2, 9, 12, 15]
odd_sum = 0

# Loop through each number in the list
for num in numbers:
    if num % 2 != 0:  # Check if the number is odd
        odd_sum += num  # Add the odd number to the sum

print(f"The sum of all odd numbers is: {odd_sum}")
