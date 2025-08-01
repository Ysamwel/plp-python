# 🐍 Python List Operations Practice

This project demonstrates basic operations on Python lists such as appending, inserting, extending, removing, sorting, and searching elements.

## 🚀 Objective

To practice and understand how to manipulate lists in Python using built-in methods.

## 📋 Task Summary

1. Create an empty list called `my_list`.
2. Append the following elements to `my_list`: `10`, `20`, `30`, `40`.
3. Insert the value `15` at the second position (index 1).
4. Extend `my_list` with another list: `[50, 60, 70]`.
5. Remove the last element from `my_list`.
6. Sort `my_list` in ascending order.
7. Find and print the index of the value `30` in `my_list`.

## 🧪 Sample Code

```python
my_list = []

# Step 1–2: Append values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert value at position 2 (index 1)
my_list.insert(1, 15)

# Step 4: Extend with another list
my_list.extend([50, 60, 70])

# Step 5: Remove last element
my_list.pop()

# Step 6: Sort in ascending order
my_list.sort()

# Step 7: Find index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

