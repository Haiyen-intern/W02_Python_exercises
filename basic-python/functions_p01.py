# 3 Functions


# Exercise 3.1: Hello
# (a) Write a function hello_world that prints 'Hello, world!'
# (b) Write a function hello_name(name) that prints 'Hello, name!' where name is a string.

def hello_world():
    print("Hello, world!")


def hello_name(name):
    print(f"Hello, {name}!")


hello_world()
hello_name("Yen")


# Exercise 3.2: Polynomial
# Write a function that evaluates the polynomial 3x^2 - x + 2.

def polynomial(x):
    return 3 * x**2 - x + 2


value = 7
result = polynomial(value)
print("The result of the polynomial 3x^2 - x + 2 for x =", value, "is", result)


# Exercise 3.3: Maximum
# Write a function my_max(x, y) that returns the maximum of x and y. Do not use the max function, but
# use if instead in following two ways:
# (a) Use both if and else.
def my_max_1(x, y):
    if x > y:
        return x
    else:
        return y


# (b) Use if but not else (nor elif).
def my_max_2(x, y):
    if x >= y:
        return x
    if y > x:
        return y


print("The maximum is", my_max_1(5, 10))
print("The maximum is", my_max_2(5, 10))


# Exercise 3.4: Primes
# (a) Write a function is_prime(n) that returns True only if n is prime.

def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True


print("Is 9 prime?", is_prime(9))


# (b) Note that apart from 2 and 3, all primes are of the form 6k ± 1 (though not all numbers of the form 6k ± 1 are prime of course). Using this, we can improve the computation time by a factor 3.

def is_prime_optimized(n):
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    factor = 5
    while factor * factor <= n:
        if n % factor == 0:
            return False
        if n % (factor + 2) == 0:
            return False
        factor += 6

    return True


# Update your function to use this.
# (c) Write a function that returns all primes up to n.

def all_primes_up_to_n(n):
    primes = []
    for m in range(2, n + 1):
        if is_prime_optimized(m):
            primes.append(m)
    return primes


print("All primes up to 20:", all_primes_up_to_n(20))


# (d) Write a function that returns the first n primes.

def first_n_primes(n):
    primes_list = []
    candidate = 2
    while len(primes_list) < n:
        if is_prime_optimized(candidate):
            primes_list.append(candidate)
        candidate += 1
    return primes_list


print("First 10 primes:", first_n_primes(10))


# Exercise 3.5: Root finding
# Suppose f is a continuous function and f(a) < 0 and f(b) > 0 for some known a and b. For simplicity, assume a < b. Then, there must exist some c such that f(c) = 0.
# (a) Write a function root(f, a, b) that takes a function f and two floats a and b and returns the root c. 
# (b) Remove the assumption that a < b, and that f(a) < 0 and f(b) > 0, if your current code relies on them.
# (c) Add a check that prints 'function evals have same sign'
# if f(a) > 0 and f(b) > 0 or if f(a) < 0 and f(b) < 0.

def root(f, a, b):
    if (f(a) > 0 and f(b) > 0) or (f(a) < 0 and f(b) < 0):
        print("function evals have same sign")
        return None

    if a > b:
        a, b = b, a

    while (b - a) >= 0.01:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


def f(x):
    return x**2 - 4

print("Root (8, 4):", root(f, 8, 4))