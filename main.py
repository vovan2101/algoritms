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

# def sum_num(arr):
#     total = 0
#     for i in arr:
#         total += i
#     return total
# print(sum_num([1,2,3,4,5]))

# def sum_num(arr):
#     if arr == []:
#         return 0
#     return arr[0] + sum(arr[1:])
#
# print(sum_num([1,2,3,4,5,6,7]))

# def rec(s):
#     if len(s) == 1 or len(s) == 2:
#         return s
#     return s[0] +'('+ rec(s[1:-1])     + ')' + s[-1]
# s = input()
# print(rec(s))

# def rec(s):
#     if len(s) <= 1:
#         return s
#     return s[0] + '*' + rec(s[1:-1]) + '*' + s[-1]
# print(rec('asdhsahdjklasdlasldkasdasdag'))
#
# def power(x, n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 1/power(x, -n)
#     if n % 2 == 0:
#         return power(x,n // 2) * power(x,n // 2)
#     else:
#         return power(x, n -1) * x
# x = int(input())
# n = int(input())
# print(power(x,n))

# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#
#         greater = [i for i in array[1:] if i > pivot]
#
#         return quicksort(less) + [pivot] + quicksort(greater)
#
# print(quicksort([10, 5, 2, 3]))


# import collections
#
# card = collections.namedtuple('card', ['rank', 'suit'])
#
# class FrenchDeck:
#     ranks = [str(n) for n in range (2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#
#     def __init__(self):
#         self._cards = [card(rank, suit) for suit in self.suits
#                                         for rank in self.ranks]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, position):
#         return self._cards[position]
#
# suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
#
# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]

# book = dict()
# book['Apple'] = 0.82
# book['Milk'] = 1.25
# book['Avocado'] = 4.20
# print(book)
# print(book['Avocado'])

# voted = {}
#
# def check_voter(name):
#     if voted.get(name):
#         print('Fick him!!')
#     else:
#         voted[name] = True
#         print('Let him in')
#
# graph = {}
# graph['you'] = ['alice', 'bob', 'claire']
# print(graph)
#
# def person_is_seller(name):
#     return name == 'claire'
#
# from collections import deque
#
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if not person in searched:
#             if person_is_seller(person):
#                 print(person + 'is mango seller!')
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#         return False
#
#
# search('you')
# graph = {}
# graph['start'] = {}
# graph['start']['a'] = 6
# graph['start']['b'] = 2
# graph['a'] = {}
# graph['a']['fin'] = 1
# graph['b'] = {}
# graph['b']['a'] = 3
# graph['b']['fin'] = 5
# graph['fin'] = {}

# stations = {}
# stations['kone'] = set(['id', 'nv', 'ut'])
# stations['ktwo'] = set(['wa', 'id', 'mt'])

