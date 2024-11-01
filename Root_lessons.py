# x = ["apples", "mangoes", "cherries"]
# y = ["apples", "mangoes", "cherries"]
# z = x
from symtable import Function

# print(x is z)
# print(x is y)

# names = ["James", "Matthew", "Arnold"]
# names.append("Moses")
# print(names)

# list = ["moses", 32, "volvo", 2.9]
# print(list)

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# mylist = ("apple", "banana", "cherry")
# print(type(mylist))

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# list=["apple", "banana", "cherry", "dragon fruit"]
# print(list[-1])

# list = ["apple", "banana", "cherry", "dragon fruit"]
# print(list[1:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# list = ["apple", "banana", "cherry"]
# if "apple" in list:
#     print("Yes baby, you got an apple")

# Use a range of indexes to print the third, fourth, and fifth item in the list.
# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[2:5])

# To change the value of a specific item, refer to the index number:
# list = ["apple", "banana", "cherry"]
# list[1] = "black_currant"
# print(list)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
# list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# list[1] = "blackcurrant"
# list[2] = "watermelon"
# print(list)

# alternatively:
# list = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# list[1:3] = "blackcurrant", "watermelon"
# print(list)

# insert less items than you replace
# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# append
# list = ["apple", "banana", "cherry"]
# list.append("orange")
# print(list)

# insert
# list = ["apple", "banana", "cherry"]
# list.insert(2,"orange")
# print(list)

# # question
# mylist = ['apple', 'banana', 'cherry']
# mylist[0] = 'kiwi'
# print(mylist)

# # append
# list = ["apple", "banana", "cherry"]
# list.append("orange")
# print(list)

# # insert
# list = ["apple", "banana", "cherry"]
# list.insert(2, "orange")
# print(list)

# # To append elements from another list to the current list, use the extend() method.
# list = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# list.extend(tropical)
# print(list)

# # add any iterable object (tuples, sets, dictionaries etc.).
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# mylist = ['apple', 'banana', 'cherry']
# mylist.insert(0, 'orange')
# print(mylist[1])

# # remove banana in the list below
# list = ["apple", "banana", "cherry"]
# list.remove("banana")
# print(list)

# # remove banana in the list below
# list = ["apple", "banana", "cherry", "banana"]
# list.remove("banana")
# print(list)

# # The pop() method removes the specified index.
# list = ["apple", "banana", "cherry"]
# list.pop(1)
# print(list)
#
# languages = ["Python", "Swift", "C++"]
# print(languages[0])
#
# my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i']
# # print from index 2 to index 4
# print(my_list[2:5])
# # print from index 5 to the end
# print(my_list[5:])
# # print from beginning to end
# print(my_list[0:])

# # Loop through a list
# list = ["apple", "banana", "cherry"]
# for x in list:
#     print(x)

# list = ["apple", "banana", "cherry"]
# print(list)

# # Looping through a string
# for x in "banana":
#     print(x)

# # The break Statement
# # With the break statement we can stop the loop before it has looped through all the items
# fruit =["apple","pear","orange","banana", "melon"]
# for x in fruit:
#     print(x)
#     if x == "orange":
#         break

# fruits = ['apple', 'orange', 'pear']
# for x in fruits:
#     if x == 'orange':
#         break
#         print(x)

# fruits = ['apple', 'orange', 'pear']
# for x in fruits:
#     if x == "orange":
#         continue
#     print(x)

# # The range() Function
# for x in range(6):
#     print(x)
#

# for x in range(2,6):
#     print(x)

# for x in range(2,30, 3):
#     print(x)

# # Else in for loop
#
# for x in range(6):
#     print(x)
# else:
#     print("Completed my tasks")

# for x in range(8):
#     if x==5: break
#     print(x)
# else:
#     print("Yeah, Python is fun")

# list = ["cars", "lorries", "matatus", "horses", "donkeys", "planes"]
# print(list)
#
# list = ["cars", "lorries", "matatus", "horses", "donkeys", "planes"]
# for x in list:
#     print(x)
#
# list = ["cars", "lorries", "matatus", "horses", "donkeys", "planes"]
# for x in range(2,6):
#     print(x)

# # Loop Through the Index Numbers
# thislist = ["apple", "banana", "cherry"]
# for x in range(len(thislist)):
#   print(thislist[x])

# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i = i + 1

# # List Comprehension
# list = ["apple", "banana", "cherry", "dragon fruit"]
# newlist = []
#
# for x in list:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)
#

# tuple
# tuple= ("apple", "banana", "cherry", "apple")
# print(tuple)

# list = ["apple", "banana", "cherry", "apple"]
# print(list)

# To determine the length in a tuple
# tuple = ("apple", "banana", "cherry")
# print(len(tuple))

# x = ("apple","banana","cherry")
# # y = list(x)
# # y[1] = "kiwi"
# # x = tuple(y)
# #
# # print(x)

## to add an item in a tuple
# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("kiwi")
# x = tuple(y)
# print(x)

## remove an item in a tuple
# x = ('apple', 'banana', 'cherry', 'kiwi')
# y = list(x)
# y.remove("kiwi")
# x = tuple(y)
# print(x)



