# Iterable (List,dict,tuple)
# Iterator


# number: int = 6
# while number > 0:
#     name: str = 'John'
#     print(f'Hello  {name}')
#     number -= 1
from typing import List


# numbers: List = [2, 4, 6]
# for i in numbers:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# start, stop, step
# for i in range(24, 3, -2):
#     print(i)

# example for iterators
# numbers1: List = [1, 24, 35, 56]
# iterator: iter = iter(numbers1)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# yoki dunder method bn
# numbers1_iter = numbers1.__iter__()
# print(numbers1_iter.__iter__())
# print(numbers1_iter.__iter__())
# print(numbers1_iter.__iter__())
# print(numbers1_iter.__iter__())

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# xatolikni oldini olish uchun
# while True:
#     try:
#         print(next(iterator))
# except StopIteration as e:
#     break
#
# class Sequence:
#     def __init__(self, sequence: List):
#         self._sequence = sequence
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index >= len(self._sequence):
#             raise StopIteration
#         else:
#             result = self._sequence[self._index]
#             self._index += 1
#             return (result)
#
#
# arr: List = [12, 324, 545]
# sequences = Sequence(arr)
# #
# # print(next(sequences))
# # print(next(sequences))
# # print(next(sequences))
# while True:
#     try:
#         print(next(sequences))
#     except StopIteration:
#         break

# iterator orqali kavadratni topish
# class Square:
#     def __init__(self):
#         self._sequence = range(1, 10)
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         if self._index >= len(self._sequence):
#             raise StopIteration
#         else:
#             result = self._sequence[self._index] ** 2
#             self._index += 1
#             return (result)
#
#
# square = Square()
# print(square.__next__())
# print(square.__next__())
# print(square.__next__())
# print(square.__next__())
#
# class Range:
#     def __init__(self, start, stop, step):
#         self.current = start
#         self.stop = stop
#         self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.step < 0:
#             if self.current > self.stop:
#                 temp = self.current
#                 self.current += self.step
#                 return temp
#             else:
#                 raise StopIteration
#
#         elif self.step > 0:
#             if self.current < self.stop:
#                 temp = self.current
#                 self.current += self.step
#                 return temp
#
#             else:
#                 raise StopIteration
#
#
# my_range: Range = Range(4, 10, 2)
#
# # print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
# print(next(my_range))
#
# while True:
#     try:
#         print(next(my_range))
#     except StopIteration:
#         break