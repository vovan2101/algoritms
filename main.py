# low = 0
# high = len(list) - 1
# mid = (low + high) / 2
# guess = list(mid)

# if guess < item:
#     low = mid + 1
#
# def binary_search(lst, item):
#     low = 0
#     high = len(lst) - 1
#
#     while low <= high:
#         mid = (low + high)
#         guess = lst[mid]
#         if guess == item:
#            return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
# my_list = [1, 3, 5, 7, 9]
# print(binary_search(my_list, 3))
# print(binary_search(my_list, -1))

# def find_smallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index

# def selection_sort(arr):
#     new_arr = []
#     for i in range(len(arr)):
#         smallest = min(arr[i])
#         new_arr.append(arr[i].pop(smallest))
#     return new_arr
# print(selection_sort([5, 3, 6, 2, 10]))

# def rec(x):
#     if x < 4:
#         print(x)
#         rec(x+1)
#         print(x)
#
# rec(1)

# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x - 1) * x
# print(fact(4))

# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# print(fib(5))

# def palindrom(s):
#     if len(s) <= 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return palindrom(s[1:-1])
# print(palindrom('шалаш'))
#
# def greet(name):
#     print('Hello, ' + name + '!')
#     greet2(name)
#     print('Getting ready to say bye...')
#     bye()
#
# def greet2(name):
#     print('How are you, ' + name + '?')
#
# def bye():
#     print('Ok, bye')
# greet('Vlad')