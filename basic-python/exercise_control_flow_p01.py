# Control flow


# Exercise 2.1: Range
# Check output and type of range(5)

print("Output of range(5):", range(5))
print("Type of range(5):", type(range(5)))

for num in range(5):
    print(num)


# Exercise 2.2: For loops
# Use a for loop to:

# (a) Print the numbers 0 to 100
for num in range(101):
    print("The numbers 0 to 100:", num)

# (b) Print the numbers 0 to 100 that are divisible by 7
for num in range(101):
    if num % 7 == 0:
        print("The numbers 0 to 100 that are divisible by 7:", num)

# (c) Print the numbers 1 to 100 that are divisible by 5 but not by 3
for num in range(1, 101):
    if num % 5 == 0 and num % 3 != 0:
        print("The numbers 1 to 100 that are divisible by 5 but not by 3:", num)

# (d) Print for each of the numbers x = 2, . . . 20, all numbers that divide x, excluding 1 and x.
for num in range(2, 21):
    print("For", num, ":", end=" ")

    for divisor in range(2, num):
        if num % divisor == 0:
            print(divisor, end=" ")

    print()


# Exercise 2.3: Simple while loops
# Instead of using a for loop, use a while loop to:

# (a) Print the numbers 0 to 100
num = 0
while num <= 100:
    print("The numbers 0 to 100:", num)
    num += 1

# (b) Print the numbers 0 to 100 that are divisible by 7
num = 0
while num <= 100:
    if num % 7 == 0:
        print("The numbers 0 to 100 that are divisible by 7:", num)
    num += 1


# Exercise 2.4: Hangman update 1
# Update the code such that the computer guesses 'e' first, and 'a' second.

guess_list = ['e', 'a', 'i', 'o', 'u', 's', 't', 'r']

print("First guess:", guess_list[0])
print("Second guess:", guess_list[1])

for guess in guess_list:
    print("guessing letter:", guess)


# Exercise 2.5: While loops
# Use a while loop to find the first 20 numbers that are divisible by 5, 7 and 11, and print them

step_size = 5 * 7 * 11
numbers_found = 0
current_num = step_size

while numbers_found < 20:
    print("The first 20 numbers that are divisible by 5, 7 and 11:", current_num)
    numbers_found += 1
    current_num += step_size


# Exercise 2.6: More while loops
# The smallest number that is divisible by 2, 3 and 4 is 12. Find the smallest number that is divisible by all integers between 1 and 10.

num = 1
while True:
    is_valid = True
    for divisor in range(1, 11):
        if num % divisor != 0:
            is_valid = False
            break

    if is_valid:
        print("The smallest number that is divisible by all integers between 1 and 10:", num)
        break

    num += 1
# Exercise 2.7: Collatz sequence
# A Collatz sequence is formed as follows: We start with some number x0, and we find the next number in the sequence by
# xi+1 =
# (
# xi/2 if xi
# is even
# 3xi + 1 if xi is odd
# If xi = 1, we stop iterating and have found the full sequence.


x = 103
print(x)

while x != 1:
    if x % 2 == 0:
        x = x // 2
    else:
        x = 3 * x + 1
    print(x)



