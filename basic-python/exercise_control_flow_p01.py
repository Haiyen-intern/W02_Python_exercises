#Control flow


# Exercise 2.1: Range
# Check output and type of range(5)

print ("Output of range(5):", range(5))
print ("Type of range(5):", type(range(5)))

for i in range(5):
    print(i)


#Exercise 2.2: For loops
# Use a for loop to:

#(a) Print the numbers 0 to 100
for i in range(101):
    print("The numbers 0 to 100:", i)

# (b) Print the numbers 0 to 100 that are divisible by 7
for i in range(101):
    if i%7 == 0:
        print("The numbers 0 to 100 that are divisible by 7:", i)
# (c) Print the numbers 1 to 100 that are divisible by 5 but not by 3
for i in range (1,101):
    if i%5 == 0 and i%3 !=0:
        print("The numbers 1 to 100 that are divisible by 5 but not by 3:", i)
# (d) Print for each of the numbers x = 2, . . . 20, all numbers that divide x, excluding 1 and x. Hence,
# for 18, it should print 2 3 6 9.
for x in range (2,21):
    for i in range (2,x):
        if x%i == 0:
          print ("The numbers that divide", x, "excluding 1 and", x, ":", i)



#Exercise 2.3: Simple while loops
# Instead of using a for loop, use a while loop to:
# (a) Print the numbers 0 to 100
i = 0 
while i<=100:
    print ("The numbers 0 to 100:" ,i)
    i+=1

# (b) Print the numbers 0 to 100 that are divisible by 7
i = 0
while i<=100:
    if i%7 == 0:
        print ("The numbers 0 to 100 that are divisible by 7:",i)
    i+=1


#Exercise 2.4: Hangman update 1
# Lets reconsider the hangman code we saw in class.1 We noted that the computer agent is not very good
# at guessing. Update the code such that the computer guesses 'e' first, and 'a' second.

guess_list = ['e', 'a', 'i', 'o', 'u', 's', 't', 'r']

print("First guess:", guess_list[0])
print("Second guess:", guess_list[1])

for guess in guess_list:
    print("guessing letter:", guess)


# Exercise 2.5: While loops
# Use a while loop to find the first 20 numbers that are divisible by 5, 7 and 11, and print them

numbers_found = 0
i = 11
while numbers_found <20:
    if i%5 ==0 and i%7 ==0 and i%11 ==0:
        print("The first 20 numbers that are divisible by 5, 7 and 11:", i)
        numbers_found +=1
        i+=1

#Exercise 2.6: More while loops
# The smallest number that is divisible by 2, 3 and 4 is 12. Find the smallest number that is divisible by all integers between 1 and 10.

i = 1
while True:
    divisible = True
    for j in range (1,11):
        if i%j !=0:
            divisible = False
            break
        if divisible == True:
            print("The smallest number that is divisible by all integers between 1 and 10:", i)
            break



# Exercise 2.7: Collatz sequence
# A Collatz sequence is formed as follows: We start with some number x0, and we find the next number in the sequence by
# xi+1 =
# (
# xi/2 if xi
# is even
# 3xi + 1 if xi is odd
# If xi = 1, we stop iterating and have found the full sequence.

x = 103
step = 0
while x!=1:
    if x%2 ==0:
        x = x//2
    else:
        x =3*x +1
    step +=1
print("The number of steps to reach 1 in the Collatz sequence starting from 103:", step)






