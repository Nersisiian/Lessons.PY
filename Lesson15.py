# ---------------------------------------------------------

# def roman_to_int(s):
#     values = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
    
#     result = 0
#     i = 0
#     while i < len(s):
        
#         current_value = values[s[i]]
        
#         if i + 1 < len(s):
#             next_value = values[s[i + 1]]
            
#             if next_value > current_value:
#                 result += (next_value - current_value)
#                 i += 2  
#             else:
#                 result += current_value
#                 i += 1
#         else:
            
#             result += current_value
#             i += 1
    
#     return result

# print(roman_to_int("III"))        
# print(roman_to_int("LVIII"))      
# print(roman_to_int("MCMXCIV"))    

# ---------------------------------------------------------

def int_to_roman(num):
    
    value_symbols = [
        (1000, 'Μ'),  
        (900, 'CM'),  
        (500, 'D'),  
        (400, 'CD'),
        (100, 'C'),   
        (90, 'XC'),
        (50, 'L'),    
        (40, 'XL'),
        (10, 'X'),    
        (9, 'IX'),
        (5, 'V'),    
        (4, 'IV'),
        (1, 'I')      
    ]
    
    result = ''
    for value, symbol in value_symbols:
        while num >= value:
            result += symbol
            num -= value
    return result

print(int_to_roman(3))       
print(int_to_roman(58))      
print(int_to_roman(1994))   
