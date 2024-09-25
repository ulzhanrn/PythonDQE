#importing necessary libraries
import random

#task1: create list of 100 random numbers from 0 to 1000

#creating random list with the use of random module and sample function
random_list = random.sample(range(0, 1000), 100)
#printing the result
print(random_list)

#task2: sort list from min to max(without using sort())

#using nested loop for sorting numbers in a list
for i in range(0, len(random_list)):
    for j in range(i+1, len(random_list)):
        if random_list[i] >= random_list[j]:
            temp = random_list[i]
            random_list[i] = random_list[j]
            random_list[j] = temp
#printing the result
print("Sorted list:", random_list)

#task3: calculate average for even and odd numbers

even_numbers = []
odd_numbers = []
#using modulus to determine even and odd numbers in a list
for i in range(0, len(random_list)):
    if random_list[i] % 2 == 0:
        even_numbers.append(random_list[i])
    else:
        odd_numbers.append(random_list[i])
#calculating average
avg_even = sum(even_numbers)/len(even_numbers)
avg_odd = sum(odd_numbers)/len(odd_numbers)
#printing the result
print("The average for even numbers:", avg_even)
print("The average for odd numbers:", avg_odd)


