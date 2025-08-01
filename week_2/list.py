# Create an empty list called my_list.
# Append the following elements to my_list: 10, 20, 30, 40.
# Insert the value 15 at the second position in the list.
# Extend my_list with another list: [50, 60, 70].
# Remove the last element from my_list.
# Sort my_list in ascending order.
# Find and print the index of the value 30 in my_list.

my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

#.extend for adding a list to another
my_list.extend([50, 60,70])

#pop
my_list.pop()

#sort in ascending order
my_list.sort()

#index finds the index of first matched item
index_of_30 = my_list.index(30)
print(index_of_30)


print(my_list)
