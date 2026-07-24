# 4 Lists

# Exercise 4.1: Short questions

numbers_list = [1, 2, 3, 4, 5]


# (a) Write a function that prints the elements of a list
def list_elements(elements):
    for element in elements:
        print(element)


list_elements(numbers_list)
print("Elements in list:", numbers_list)


# (b) Write a function that prints the elements of a list in reverse
def elements_in_reverse(elements):
    for element in reversed(elements):
        print(element)


print("Elements in reverse:")
elements_in_reverse(numbers_list)


# (c) Write your own implementation of the len function that returns the number of elements in a list.
def custom_len(elements):
    count = 0
    for element in elements:
        count += 1
    return count


print("Length of list:", custom_len(numbers_list))


# Exercise 4.2: Copying lists

# (a) Create a list a with some entries.
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("List a:", a)

# (b) Now set b = a
b = a
print("List b:", b)

# (c) Change b[1]
b[1] = 11

# (d) What happened to a?
print("List a after changing b[1]:", a)

# (e) Now set c = a[:]
c = a[:]
print("List c:", c)

# (f) Change c[2]
c[2] = 15

# (g) What happened to a?
print("List a after changing c[2]:", a)


# Now create a function set_first_elem_to_zero(l) that takes a list, sets its first entry to zero, and returns the list.
def set_first_elem_to_zero(elements):
    if elements:
        elements[0] = 0
    return elements


# What happens to the original list?
original_list = [1, 2, 3, 4, 5]
modified_list = set_first_elem_to_zero(original_list)
print("Original list:", original_list)


# Exercise 4.3: Lists of lists

# What is the difference between a and b:
# a = [[]] * 3
a = [[]] * 3
print("List a:", a)

# b = [[] for _ in xrange(3)]
b = [[] for _ in range(3)]
print("List b:", b)


# Exercise 4.4: Lists and functions

# Write a function that takes a list and an index, and sets the value of the list at the given index to 0.
numbers = [1, 2, 3, 4, 5]


def set_value_to_zero(elements, index):
    if -len(elements) <= index < len(elements):
        elements[index] = 0
    else:
        print("Index out of range")


set_value_to_zero(numbers, 2)
print("List after setting index 2 to 0:", numbers)
set_value_to_zero(numbers, 6)


# Exercise 4.5: Primes

# In Section 3 you wrote a function that prints all primes up to n, and a function that prints the first n primes.
# Update these functions such that they return lists instead.
def is_prime_optimized(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    factor = 5
    while factor * factor <= n:
        if n % factor == 0 or n % (factor + 2) == 0:
            return False
        factor += 6
    return True


# Returns a list of all primes up to n
def all_primes_up_to(n):
    primes = []
    for m in range(2, n + 1):
        if is_prime_optimized(m):
            primes.append(m)
    return primes


primes_up_to_30 = all_primes_up_to(30)
print("All primes up to 30:", primes_up_to_30)


# Returns a list of the first n primes
def first_n_primes(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime_optimized(candidate):
            primes.append(candidate)
        candidate += 1
    return primes


first_20_primes = first_n_primes(20)
print("First 20 primes:", first_20_primes)


# Exercise 4.6: List comprehensions

# Let i, j = 1, . . . , n
n = 5

# (a) Generate a list with elements [i,j].
pairs_all = [[i, j] for i in range(1, n + 1) for j in range(1, n + 1)]
print("All pairs [i,j]:", pairs_all)

# (b) Generate a list with elements [i,j] with i < j
pairs_less = [[i, j] for i in range(1, n + 1) for j in range(1, n + 1) if i < j]
print("Pairs[i,j] with i < j:", pairs_less)

# (c) Generate a list with elements i + j with both i and j prime and i > j.
primes_sum = [
    i + j
    for j in range(1, n + 1)
    for i in range(j + 1, n + 1)
    if is_prime_optimized(i) and is_prime_optimized(j)
]

print("Sum of primes i + j with i > j:", primes_sum)

# (d) Write a function that evaluates an arbitrary polynomial a0 + a1x + a2x2 + . . . + anxn using a list comprehension
def evaluate_polynomial(x, coefs):
    return sum(coef * (x**power) for power, coef in enumerate(coefs))


coefs = [1, 2, 3]
x = 2
print("Polynomial evaluation result:", evaluate_polynomial(x, coefs))


# Exercise 4.7: Filter

# Implement filter using list comprehensions. Name your functions myfilter so you can compare with Python’s standard filter.
def myfilter(func, iterable):
    return [item for item in iterable if func(item)]


numbers = [1, 2, 3, 4, 5]


def is_even(n):
    return n % 2 == 0


filtered_numbers = myfilter(is_even, numbers)
print("Filtered even numbers:", filtered_numbers)


# Exercise 4.8: Flatten a list of lists

# Write a function that takes such a list, and returns a list with as elements the elements of the sublists
def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


nested_list = [[1, 3], [3, 6]]
flattened = flatten_list(nested_list)
print("Flattened list:", flattened)


# Exercise 4.9: Finding the longest word

import string


def find_longest_word(text):
    cleaned_text = ""
    for char in text:
        if char not in string.punctuation:
            cleaned_text += char

    words = cleaned_text.split()
    if not words:
        return ""

    # Returns the first longest word
    longest_word = max(words, key=len)
    return longest_word


sentence = "Long time no see"
print("Longest word:", find_longest_word(sentence))


# Exercise 4.10: Collatz sequence, part 2

# (a) Write a function that for any n, returns its Collatz sequence as a list
def get_collatz_sequence(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


print("Collatz sequence for 36:", get_collatz_sequence(36))


# (b) Write a function that finds the integer x that leads to the longest Collatz sequence with x < n.
def find_longest_collatz(n):
    max_length = 0
    integer_x = 1

    for candidate in range(1, n):
        current_length = len(get_collatz_sequence(candidate))
        if current_length > max_length:
            max_length = current_length
            integer_x = candidate

    return integer_x, max_length


best_num, sequence_len = find_longest_collatz(300)
print("The longest Collatz sequence length:", sequence_len)


# Exercise 4.11: Pivots

def pivot_list(x, ys):
    smaller = [y for y in ys if y < x]
    larger_or_equal = [y for y in ys if y >= x]
    return smaller + [x] + larger_or_equal


sample_pivot = 5
numbers_list = [1, 2, 3, 4]
result = pivot_list(sample_pivot, numbers_list)
print("Pivot result:", result)


# Exercise 4.12: Prime challenge

is_prime = lambda num: num > 1 and all(
    num % divisor != 0 for divisor in range(2, int(num**0.5) + 1)
)

primes = lambda n: [m for m in range(2, n + 1) if is_prime(m)]

print("Primes up to 20:", primes(20))