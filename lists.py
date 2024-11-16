# Create a list of 5 fruits and print each fruit on a new line using a for loop.


fruits = ["mango", "orange", "pineapple", "grape", "kiwi"]

# Loop through each fruit in the list and print it
for fruit in fruits:
    print(fruit)



# Write a function that takes a list of numbers and returns a new list with
#each number squared. Example: [1, 2, 3] should become [1, 4, 9].

def square_numbers(numbers):
    
# Create a new list with each number squared
    squared_numbers = [num ** 2 for num in numbers]
    return squared_numbers

numbers = [1, 2, 3]
squared = square_numbers(numbers)
print(squared)



#Write a Python program that takes two lists, list1 = [1, 2, 3] and
#list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2,5, 3, 6].


# Define the two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Initialize an empty list to store the combined result
combined = []

# Use a for loop to combine elements alternately from both lists
for i in range(len(list1)):
    combined.append(list1[i])  # Add element from list1
    combined.append(list2[i])  # Add element from list2

# Print the combined list
print(combined)



#Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find
#and print the two largest numbers in the list without using the max() function.


numbers = [3, 1, 4, 1, 5, 9, 2]

# Sort the list in descending order and take the first two elements
numbers.sort(reverse=True)

# The two largest numbers will now be the first two elements
largest = numbers[0]
second_largest = numbers[1]

# Print the result
print(f"The two largest numbers are: {largest} and {second_largest}")








