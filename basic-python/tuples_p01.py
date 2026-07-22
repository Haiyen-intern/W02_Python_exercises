# 5 Tuples



# Exercise 5.1: Swapping two values
# Suppose you have two variables: a and b. Now you want to set a equal to the value of b and at the same time set b equal to the value of a.
a = 48
b = 23

print(f"Before swap: a = {a}, b = {b}")

a, b = b, a

print(f"After swap: a = {a}, b = {b}")


# Exercise 5.2: Zip
# Suppose we have two lists, x and y that give the x and y coordinates of a set of points. Create a list with the coordinates (x,y) as a tuple. Hint: Find out about the zip function.
x = [1, 2, 3, 4]
y = [15, 25, 35, 45]
# Zip two lists
points = list(zip(x, y))
print ("Zipped list of tuples:", points)
# Unzip the list
unzipped_x, unzipped_y = zip(*points)
# Convert
x_restored = list(unzipped_x)
y_restored = list(unzipped_y)

print("Unzipped list x:", x_restored)
print("Unzipped list y:", y_restored)

# Exercise 5.3: Distances
# Suppose we have two vectors, x and y, stored as tuples with n elements. Implement functions that compute the l1 and l2 distances between x and y. Note that n is not explicitly given.

def l1_distance(x, y):
    return sum(abs(x_elem - y_elem) for x_elem, y_elem in zip(x, y))

def l2_distance(x, y):
    sum_squared_diff = sum((x_elem - y_elem) ** 2 for x_elem, y_elem in zip(x, y))
    return sum_squared_diff ** 0.5
vector1 = (1.0, 2.0, 5.0)
vector2 = (4.0, 6.0, 5.0)

print("L1 Distance (Manhattan):", l1_distance(vector1, vector2))
print("L2 Distance (Euclidean):", l2_distance(vector1, vector2))