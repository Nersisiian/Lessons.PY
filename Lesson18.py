# -------------------------------------------------------------------------

# def can_make_amount(remaining_amount, coins, attempts):

#     if remaining_amount == 0:
#         return True
    
#     if attempts == 0 or remaining_amount < 0:
#         return False

#     if not coins:
#         return False

#     if can_make_amount(remaining_amount - coins[0], coins, attempts - 1):
#         return True
    
    
#     return can_make_amount(remaining_amount, coins[1:], attempts)

# coins = [25, 10, 5, 1]
# attempts = 8
# amount = 67
# result = can_make_amount(amount, coins, attempts)
# print(result)  

# -------------------------------------------------------------------------

# def flatten(data):
    
#     if not data:
#         return []
    
#     result = []
#     first = data[0]
    
#     if isinstance(first, list):

#         result.extend(flatten(first)) 
#     else:
#         result.append(first)  
    
#     result.extend(flatten(data[1:]))
    
#     return result

# nested_list = [1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]
# flattened_list = flatten(nested_list)
# print(flattened_list) 

# -------------------------------------------------------------------------

def nato_alphabet():
    nato_dict = {
        'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
        'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
        'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
        'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }
    
    def encode_word(word):
        if not word: 
            return []
        
        first_char = word[0].upper()  
        if first_char in nato_dict:  
            return [nato_dict[first_char]] + encode_word(word[1:])
        else:  
            return encode_word(word[1:])
    
    user_input = input("Введите слово: ")
    encoded = encode_word(user_input)
    print(" ".join(encoded))

nato_alphabet()


  

