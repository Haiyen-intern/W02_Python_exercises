# Python Debug Notes 


1. IndexError: list index out of range

Exercise: Exercise 4.4 
Error Message:IndexError: list index out of range

Cause: Attempting to access or assign a value at an index that does not exist in the list (e.g., trying to modify index = 6 on a list with only 5 elements).

Fix: Check if the index falls within the valid range before attempting to access or modify it.

# Bug code:
def set_value_to_zero(elements, index):
    elements[index] = 0  # Raises IndexError if index is out of bounds

# Fixed code:
def set_value_to_zero(elements, index):
    if -len(elements) <= index < len(elements):
        elements[index] = 0
    else:
        print(f"Error: Index {index} is out of bounds.")
2. ValueError: max() arg is an empty sequence
Exercise: Exercise 4.9 (Finding the longest word)

Error Message:ValueError: max() arg is an empty sequence
Cause: Calling the max() function on an empty list (words = []). This happens when the input string consists entirely of punctuation marks (e.g., text = "???"), leaving an empty list after punctuation is stripped.
Fix: Ensure the list contains data before passing it to max().
# Bug code:
words = cleaned_text.split()
return max(words, key=len)  # Raises ValueError if words is empty

# Fixed code:
words = cleaned_text.split()
if not words:
    return ""  # Safely return an empty string
return max(words, key=len)

3. TypeError: 'tuple' object does not support item assignment

Exercise: Exercise 5.1 (Swapping two values) / Exercise 5.3 (Distances)

Error Message:TypeError: 'tuple' object does not support item assignment

Cause: Attempting to mutate an element inside a tuple via item assignment (e.g., point[0] = 10). In Python, tuples are immutable and cannot be altered after creation.

Fix: Create a new tuple instead of modifying the existing one, or convert the tuple to a list if dynamic modification is required.

# Bug code:
point = (1.0, 2.0)
point[0] = 5.0  # Raises TypeError

# Fixed code (Option 1: Create a new tuple):
point = (5.0, point[1])

# Fixed code (Option 2: Convert to list):
point_list = list(point)
point_list[0] = 5.0