# DICTIONARIES


## Exercise 6.1: Printing a dictionary ##

# Write a function that prints key-value pairs of a dictionary.

student_info = {"name": "Yen", "age": 22, "class": "IT"}


def student_dict(d):
    for key, value in d.items():
        print(key, ":", value)


student_dict(student_info)


## Exercise 6.2: Histogram ##

# Write a function that takes a list, and returns a dictionary with keys the elements
# of the list and as value the number of occurrences of that element in the list.

students_list = ["An", "Minh", "Ha"]


def histogram(elements):
    counts = {}

    for item in elements:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


result = histogram(students_list)

print(f"List: {students_list}")
print(f"Result Dict: {result}")


# After you are done, look up 'python collections counter' in Google.
# Could you use a counter instead?

from collections import Counter

result_counter = Counter(students_list)
print(result_counter)


## Exercise 6.3: Get method ##

# Dictionaries have a get method, which takes a key and a default value.
# If the key is in the dictionary, it returns the value,
# otherwise, it returns the default value.

test_result_list = ["Pass", "Fail", "Pass", "Pass", "Fail"]


def histogram_with_get(elements):
    counts = {}

    for item in elements:
        counts[item] = counts.get(item, 0) + 1

    return counts


test_result_count = histogram_with_get(test_result_list)

print(f"List: {test_result_list}")
print(f"Result Dict: {test_result_count}")


## Exercise 6.5: Vector functions ##

# (a) Write a function that adds two (dense) vectors

def add_dense(v1, v2):
    result = []
   
    for x, y in zip(v1, v2):
        result.append(x + y)
    return result

# (b) Write a function that multiplies (i.e. inner product) two (dense) vectors

def dot_dense(v1, v2):
    result = 0
    for x, y in zip(v1, v2):
        result += x * y
    return result



# (c) Write a function that adds two sparse vectors


def add_sparse(v1, v2):
    result = {}

    for index, value in v1.items():
        result[index] = value

    for index, value in v2.items():
        result[index] = result.get(index, 0) + value

        if result[index] == 0:
            del result[index]

    return result


# (d) Write a function that multiplies two sparse vectors


def dot_sparse(v1, v2):
    result = 0

    for index in v1:
        if index in v2:
            result += v1[index] * v2[index]

    return result


# (e) Write a function that adds a sparse vector and a dense vector


def add_sparse_dense(v_sparse, v_dense):
    result = list(v_dense)

    for index, value in v_sparse.items():
        result[index] += value

    return result


# (f) Write a function that multiplies a sparse vector and a dense vector


def dot_sparse_dense(v_sparse, v_dense):
    result = 0

    for index, value in v_sparse.items():
        result += value * v_dense[index]

    return result



dense_vector_1 = [1, 2, 3]
dense_vector_2 = [4, 5, 6]

sparse_vector_1 = {0: 1, 2: 3}
sparse_vector_2 = {1: 2, 2: 4}

print("Dense vector addition:", add_dense(dense_vector_1, dense_vector_2))
print("Dense vector dot product:", dot_dense(dense_vector_1, dense_vector_2))

print("Sparse vector addition:", add_sparse(sparse_vector_1, sparse_vector_2))
print("Sparse vector dot product:", dot_sparse(sparse_vector_1, sparse_vector_2))

print("Sparse + dense:",
      add_sparse_dense(sparse_vector_1, dense_vector_2))

print("Sparse * dense:",
      dot_sparse_dense(sparse_vector_1, dense_vector_2))


# Exercise 6.6: Reverse look-up

# Dictionaries are made to look up values by keys. Suppose however, we want to find the key that is associated with some value.
# Write a function that takes a dictionary and a value, and returns the key associated with this value.


def reverse_lookup(d, target_value):
    for key, value in d.items():
        if value == target_value:
            return key


lookup_dictionary = {
    "name": "Yen",
    "age": 22,
    "class": "IT"
}

print("Key for value 22:", reverse_lookup(lookup_dictionary, 22))
print("Key for value 'IT':", reverse_lookup(lookup_dictionary, "IT"))
