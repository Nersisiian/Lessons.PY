# ------------------------------------------------------------------------------

# def prime_list(mylist):

#     if not mylist:
#         return []
    
#     first = mylist[0]
#     rest = prime_list(mylist[1:])
#     if first % 2 != 0:
#         return [first] + rest
#     else:
#         return rest

# print(prime_list([7, 4, 1, 2, 6, 5]))

# ------------------------------------------------------------------------------

# def flatten(data):

#     if not data:
#         return []

#     first_element = data[0]
#     rest = data[1:]

#     if isinstance(first_element, list):

#         l1 = flatten(first_element)
#         l2 = flatten(rest)
        
#         return l1 + l2
#     else:
        
#         l1 = [first_element]
#         l2 = flatten(rest)
        
#         return l1 + l2

# if __name__ == "__main__":
#     data1 = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
#     data2 = [1, 2, 3]
#     data3 = [[[[[1]]]]]
#     data4 = []

#     print(flatten(data1))
#     print(flatten(data2))
#     print(flatten(data3))
#     print(flatten(data4))

# ------------------------------------------------------------------------------

# def decode(mylist):
#     result = []
    
#     for i in range(0, len(mylist), 2):
#         char = mylist[i]
#         count = mylist[i + 1]
#         result.extend([char] * count)
#     return result

# print(decode(["A", 12, "B", 4, "A", 6, "B", 1]))

# ------------------------------------------------------------------------------

# def dec_to_binary(n):
#     if n == 0:
#         return "0"
#     binary = ""
#     while n > 0:
#         binary = str(n % 2) + binary
#         n //= 2
#     return binary

# print(dec_to_binary(18))

# ------------------------------------------------------------------------------

