# alist = [-10,-5,0,4,9]

# for element in alist:
#     print(element)

# # time O(n); space O(1)


# index = 0
# for _ in alist:
#     print(index)
#     index += 1


# alist = [-10,-5,0,4,9]
# for element in alist:
#     if element >= 0:
#         print(element)

# time n; space 1


# alist = [-10,-5,0,4,9]
# positive_nums = []
# for element in alist:
#     if element >= 0:
#         positive_nums.append(element)
# print(positive_nums)

# time n; space n


# alist = [-10,-5,0,4,9]
# my_sum = 0
# count = 0
# for element in alist:
#     my_sum += element
#     count += 1
# print(my_sum / count)

# time n; space 1


# alist = [4,6,8,10]
# print(alist[-1])

# time 1; space 1


# def findMax(alist):
#     highest = 0
#     for element in alist:
#         if element > highest:
#             highest = element
#     print(highest)

# alist = [4,6,8,10]
# findMax(alist)

# time n; space 1


# alist = [-10,-5,0,4,9]
# index = -1
# for _ in alist:
#     print(alist[index])
#     index -= 1

# time n; space 1


# alist = [-10,-5,0,4,9]
# for i in range(len(alist) - 1, -1, -1):
#     num = alist[i]
#     if num < 0:
#         alist.pop(i)
# print(alist)

# time n; space 1


# password = ''
# while password != 'secret':
#     password = input('enter password')
# print('Password accepted!')

# can't say time or space


# def linearSearch(arr,key):
#     for element in arr:
#         if element == key:
#             return True
#     return False
    
# alist = [10,20,30,40,50,60,70,80,90]
# print(linearSearch(alist, 40))
# print(linearSearch(alist, 140))

# time n; space 1


# def search_key_index(alist,key):
#     i = 0
#     for element in alist:
#         if element == key:
#             return i
#         i += 1
#     return -1

# alist = [10,20,30,40,50,60,70,80,90]
# print(search_key_index(alist, 40))
# print(search_key_index(alist, 140))

# time n; space 1


alist = [10,10,20,20,20,30]
freq = {}
for element in alist:
    if element in freq:
        freq[element] += 1
    else:
        freq[element] = 1
print(freq)

# time n; space n
