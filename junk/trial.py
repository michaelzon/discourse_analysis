#!/usr/bin/python
from textblob import TextBlob
import itertools
import nltk
import os
import sys

# # hoe het uit het artikel komt
# list1 = ["zin", "in", "hebben"]
#
# # hoe het in mijn posLijst staat
# list2 = ["zin hebben in"]
#
# if("zin" in list1):
#     print("ja1")
# else:
#     print("nee1")
#
# if("zin" in list2):
#     print("ja2")
# else:
#     print("nee2")
#
# twee = 2
#
# print(list1[])
#
# def first_half(str):
#   length = len(str)
#   half = int(length / 2)
#   if length == 2 * half:
#     return str[:half]
#
# # print(first_half('WooHoo'))
#
# def without_end(str):
#   length = len(str)
#   if len(str) >= 2:
#     return str[1:length-1]
#
# # print(without_end('Hello'))
#
# def left2(str):
#     if len(str) >= 2:
#         return str[2:] + str[:2]
#
# # print(left2("Hello"))
# # print(left2("H"))
#
# def first_last6(nums):
#   if len(nums) >= 1:
#     if (nums[0] == 6) or (nums[-1] == 6):
#       return True
#     else:
#       return False
#
# # print(first_last6([1, 2, 6]))
# # print(first_last6([6, 1, 2, 3]))
# # print(first_last6([13, 6, 1, 2, 3]))
#
# def first_last6(nums):
#   if len(nums) >= 1:
#     return(nums[0] == 6) or (nums[-1] == 6)
#
# print(first_last6([1, 2, 6]))
# print(first_last6([6, 1, 2, 3]))
# print(first_last6([13, 6, 1, 2, 3]))
#
# def same_first_last(nums):
#   return (len(nums) >= 1 and (nums[0] == nums[-1])
#
#   if len(nums) == 2:
#     if nums[0] or nums[1] == 2:
#       return True
#     elif nums[0] or nums[1] == 3:
#       return True
#
# def has23(nums):
#     if len(nums) == 2:
#         if 2 or 3 in nums:
#             return True
#         if not (2 or 3 in nums):
#             return False
#     else:
#         return False
# print("hier", has23([4, 5]))
#
# def has23(nums):
#     if (2 in nums) or (3 in nums):
#         return True
#
# def has23(nums):
#     return 2 in nums or 3 in nums
#
# print("hier", has23([4, 5]))
#
#
# def date_fashion(you, date):
#   if (3 =< you =< 10) or (3 =< date =< 10):
#     return 2
#   if 2 =< you or 2 =< date:
#     return 0
#   else:
#     return 1
#
# print(date_fashion(5, 10))
# print(date_fashion(5, 2))
# print(date_fashion(5, 5))
#
#
# def count_hi(str):
#   greeting = "hi"
#   hiOnly = str[str.find(greeting) + len(greeting)]
#
# print(count_hi('abc hi ho'))
# print(count_hi('ABChi hi'))
# print(count_hi('hihi'))
#
#
# def cat_dog(str):
#     count = 0
#     for i in range(len(str)-1):
#         if str[i:i+3] == "cat":
#             count += 1
#     return count
#
# # print('catdog', cat_dog("catcatBakkercat"))
#
#
# def count_hi(str):
#   count = 0
#   for i in range(len(str)-1):
#     if str[i:i+2] == "hi":
#       count += 1
#   return count
#
# print('hi', count_hi('ABChi hi'))
# print('hi', count_hi("hihiBakkerhi"))
#
#
# def cat_dog(str):
#
#   for i in range(len(str)-1):
#     if str[i:i+3] == "cat" and str[i:i+3] == "dog":
#       return True
#     if str[i:i+3] == "dog" and str[i:i+3] == "cat":
#       return True
#
#   else:
#     return False
#
#
# def count_code(str):
#     codeCount = 0
#     for i in range(0, len(str) - 3, 1):
#         if str[i:i+2] == "co" and str[i+3] == "e":
#             codeCount += 1
#     return codeCount
#
# print(count_code(('AAcodeBBcoleCCccorfDD')))
#
# def count_code(str):
#     codeCount = 0
#     print('cozexxcope')
#     print("0123456789")
#     for i in range(0, len(str) - 3, 1):
#         # if str[i:i+2] == "co" and str[i+3] == "e":
#         #     codeCount += 1
#     return codeCount
#
# print(count_code(('cozexxcope')))
#
# string = "code"
#
# count = 0
# # for i in range(len(string)-1):
# for i in range(0, len(string) - 3, 1):
#     # print('itr', count)
#     print("i", i)
#     print('str', string[i:i+4])
#     count += 1
#
#
# def xyz_there(str):
#     for i in range(0, len(str)):
#         if str [i:i+4] != ".xyz":
#             return(str[i:i+3] == "xyz")
#
# print(xyz_there('abc.xyz'))
# print("True",xyz_there('abcxyz'))
#
#
# def xyz_there(str):
#     for i in range(0, len(str) - 3):
#         if (str[i+1] != "." and str[i:i+3] == "xyz"):
#             return True
#         else:
#             return False
#
# print(xyz_there('abc.xyz'))
# print("True",xyz_there('abcxyz'))
#
#
# def xyz_there(str):
#     for i in range(len(str)-3):
#         if ".xyz" in str:
#             return False
#         if "xyz" in str:
#             return True
#         else:
#             return False
#
# print("False",xyz_there('abc.xyz'))
# print("True",xyz_there('abcxyz'))
#
#
# def count_evens(nums):
#     count = 0
#     for i in range(len(nums):
#         if (nums[i] % 2 == 0):
#             count += 1
#         return count
#
# def centered_average(nums):
#
#     lowest = min(nums)
#     print("lowest", lowest)
#     highest = max(nums)
#     print("highest", highest)
#     total = 0
#     length = (len(nums))
#     print("length", length)
#     for i in range(length):
#         total += nums[i]
#         print('tot1', total)
#
#     total = (total - lowest - highest)
#     print('tot2', total)
#     avarage = (total / (length - 2))
#     print(int(avarage))
#     return int(avarage)
#
#
# print(centered_average([1, 1, 5, 5, 10, 8, 7]))
#
# def sum67(nums):
#     i = 0
#     tot = 0
#     if 6 and 7 in nums:
#         while i < len(nums):
#             if nums[i] == 6:
#                 indexSix = nums.index(6)
#                 indexSeven = nums.index(7)
#                 indexIncrement = indexSeven - indexSix
#                 i += indexIncrement + 1
#                 continue
#             tot += nums[i]
#             i += 1
#         return tot
#
# print(sum67([5,5,5,6,2,2,2,2,7,8,6,1,7,1, 1, 1]))
#
#
#
# nums = ([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])
#
#
# indexSix = nums.index(6)
# indexSeven = nums.index(7)
#
#
# print(nums.index(6))
# print(nums.index(7))
# for i in range(len(nums)):
#     print(nums[i])
#
# def sum67(nums):
#     go = True
#     total = 0
#
#     for i in range(len(nums)):
#         print(nums[i], i)
#         if go == True:
#             if nums[i] == 6:
#                 go = False
#             else:
#                 total += nums[i]
#         else:
#             if nums[i] == 7:
#                 go = True
#     return total
#
# print(sum67([5,5,5,6,2,2,2,2,7,8,6,1,7,1]))

def has22(nums):
    for i in range(0, len(nums), 1):

        if nums[i] == 2 and nums[i+1] == 2:
            return True
    else:
        return False

print(has22([3,3,2,2]))
