import psycopg2

# define the colors and their frequency
colors = {
    "green": 10,
    "yellow": 6,
    "brown": 6,
    "blue": 26,
    "pink": 5,
    "orange": 8,
    "cream": 2,
    "red": 9,
    "white": 12,
    "black": 1
}

# 1. Which color of shirt is the mean color?
mean_color = max(colors, key=colors.get)
print("The mean color is:", mean_color)

# 2. Which color is mostly worn throughout the week?
most_worn_color = max(colors, key=colors.get)
print("The most worn color is:", most_worn_color)

# 3. Which color is the median?
median_color = sorted(colors)[len(colors) // 2]
print("The median color is:", median_color)

# 4. BONUS Get the variance of the colors
mean_frequency = sum(colors.values()) / len(colors)
variance = sum((f - mean_frequency) ** 2 for f in colors.values()) / len(colors)
print("The variance of the colors is:", variance)

# 5. BONUS if a colour is chosen at random, what is the probability that the color is red?
total_frequency = sum(colors.values())
red_frequency = colors["red"]
red_probability = red_frequency / total_frequency
print("The probability of choosing red is:", red_probability)



# 7. BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
def recursive_search(number, numbers):
    if not numbers:
        return False
    if numbers[0] == number:
        return True
    return recursive_search(number, numbers[1:])

# example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = 7
found = recursive_search(number, numbers)
print(f"The number {number} is in the list:", found)

# 8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.
import random

binary_number = ""
for i in range(4):
    binary_number += str(random.randint(0,1))
print(f"random 4 digits number of 0s and 1s: {binary_number}")
decimal_number = int(binary_number, 2)
print(f"The binary number {binary_number} in decimal is:", decimal_number)


# 9. Write a program to sum the first 50 fibonacci sequence.
def fibonacci(n):
    if n < 0:
        raise ValueError("n must be positive")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci_sum = sum(fibonacci(n) for n in range(1, 51))
print("The sum of the first 50 fibonacci sequence is:", fibonacci_sum)

# 6. Save the colours and their frequencies in postgresql database
connection = psycopg2.connect(user="postgres",
                              password="postgres",
                              host="DESKTOP-0DE63L0",
                              port="5432",
                              database="postgres")
cursor = connection.cursor()
for color, frequency in colors.items():
    query = f"INSERT INTO colors (color, frequency) VALUES ('{color}', {frequency})"
    cursor.execute(query)
connection.commit()