# morse_code = {
#     'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',   
#     'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---', 
#     'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',  
#     'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',    
#     'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--', 
#     'Z': '--..',
#     '1': '.----', '2': '..---', '3': '...--', '4': '....-',  '5': '.....', 
#     '6': '-....', '7': '--...', '8': '---..', '9': '----.',  '0': '-----'
# }

# def text_to_morse(text):
#     morse_message = []
#     for char in text:
#         upper_char = char.upper()
#         if upper_char in morse_code:
#             morse_message.append(morse_code[upper_char])
#     return ' '.join(morse_message)

# user_input = input("Введите строку для преобразования в азбуку Морзе: ")
# morse_output = text_to_morse(user_input)

# print("Азбука Морзе:", morse_output)
# Xndir 139



# unique_chars = set(input("Введите строку: "))
# print(f"В строке содержится {len(unique_chars)} уникальных символов.")
# Xndir 142
# Kam senc
# print(len(set(input("Введите строку: "))))

