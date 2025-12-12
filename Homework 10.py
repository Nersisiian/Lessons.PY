# Exercise 1 ------------------------------------------------------------------------------------------------------------------------------------


# my_list = ["hello", 42, 3.14, True, None, [1, 2, 3]]
# print(my_list) 
# print([type(x) 
#        for x in my_list])


# Exercise 2 ------------------------------------------------------------------------------------------------------------------------------------


# my_list = ["Hp", "Asus", "Dell", "Mac", "Lenovo"]
# has_mac = any(item.lower() == "mac" for item in my_list)
# print(has_mac)  
# print("Mac" in my_list) 


# Exercise 3 ------------------------------------------------------------------------------------------------------------------------------------


# def is_strong(password: str) -> bool:
    
#     digits = sum(1 for c in password if c.isdigit())
#     specials = sum(1 for c in password if c in "!@#$%&*")
#     return len(password) > 8 and digits >= 2 and specials >= 2

# if __name__ == "__main__":
#     s = input().strip()
#     print("Strong" if is_strong(s) else "Weak")


# Exercise 4 ------------------------------------------------------------------------------------------------------------------------------------


# from urllib.parse import urlparse, parse_qs

# def extract_youtube_id(url: str) -> str:
#     parsed = urlparse(url)
#     qs = parse_qs(parsed.query)

#     if 'v' in qs and qs['v']:
#         return qs['v'][0]

#     path_parts = [p for p in parsed.path.split('/') if p]
#     if path_parts:
#         possible_id = path_parts[-1]
#         if possible_id:
#             return possible_id

#     return ""

# if __name__ == "__main__":
#     url = input("Enter YouTube URL: ").strip()
#     vid = extract_youtube_id(url)
#     if vid:
#         print(vid)
#     else:
#         print("Video ID not found.")


# Exercise 5 ------------------------------------------------------------------------------------------------------------------------------------


# s = input().strip()

# s_lower = s.lower()
# if s_lower == s_lower[::-1]:
#     print("Open")
# else:
#     print("Trash")


# Exercise 6 ------------------------------------------------------------------------------------------------------------------------------------


# def to_char_list(s):
#     return list(s)

# def to_split_list(s, sep=' '):
#     return s.split(sep)

# def to_int_list(s, sep=','):
#     return [int(x.strip()) for x in s.split(sep)]

# def main():
#     s = input("Enter a string: ")

#     print("Characters:", to_char_list(s))

#     sep = input("Enter a delimiter for splitting (default is space): ").strip() or ' '
#     print("Split by delimiter '{}': {}".format(sep, to_split_list(s, sep)))

#     nums = input("Enter comma-separated numbers (e.g., 1,2, 3): ")
#     if nums:
#         print("Int list from numbers: ", to_int_list(nums, ','))
#     else:
#         print("No numbers provided.")

# if __name__ == "__main__":
#     main()


# Exercise 7 ------------------------------------------------------------------------------------------------------------------------------------


# s = input("Enter a string of digits: ").strip()

# evens = [ch for ch in s if ch.isdigit() and int(ch) % 2 == 0]
# result = "".join(evens)

# print(result)


# Exercise 8 ------------------------------------------------------------------------------------------------------------------------------------


# numbers = [3, 7, 10, 4, 5, 6, -7, 8]

# odd_items = [n for n in numbers if isinstance(n, int) and n % 2 != 0]
# print("Odd items (new list):", odd_items)

# i = 0
# while i < len(numbers):
#     n = numbers[i]
#     if isinstance(n, int) and n % 2 == 0:
#         del numbers[i]
#     else:
#         i += 1
# print("Original list after removing evens (in place):", numbers)
  

# Exercise 9 ------------------------------------------------------------------------------------------------------------------------------------


# import random

# def secret_santa(participants):
#     if len(participants) < 2:
#         raise ValueError("Need at least 2 participants")

#     while True:
#         recipients = participants[:]
#         random.shuffle(recipients)

#         if all(giver != receiver for giver, receiver in zip(participants, recipients)):
#             return dict(zip(participants, recipients))

# if __name__ == "__main__":
#     participants = ["Alice", "Bob", "Charlie", "Diana", "Evan"]
#     assignments = secret_santa(participants)
#     for giver, receiver in assignments.items():
#         print(f"{giver} -> {receiver}")


# Exercise 10 ------------------------------------------------------------------------------------------------------------------------------------


# def remove_duplicates_preserve_order(lst):
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result

# my_list = [1, 2, 3, 2, 4, 1, 5]
# print(remove_duplicates_preserve_order(my_list))


