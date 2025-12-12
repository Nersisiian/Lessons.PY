# ------------------------------------------------------------------------------------------------- No136


# def reverseLookup(dictionary, value):
#     keys = []
   
#     for key, val in dictionary.items():
        
#         if val == value:
#             keys.append(key)
    
#     return keys

# if __name__ == "__main__":
    
#     sample_dict = {
#         'a': 1,
#         'b': 2,
#         'c': 3,
#         'd': 2,
#         'e': 1
#     }
#     print("Поиск ключей для значения 2:", reverseLookup(sample_dict, 2))  
#     print("Поиск ключей для значения 1:", reverseLookup(sample_dict, 1)) 
#     print("Поиск ключей для значения 5:", reverseLookup(sample_dict, 5))  
#     test_dict = {
#         'key1': 'apple',
#         'key2': 'banana',
#         'key3': 'apple'
#     }
#     print("Поиск ключей для значения 'apple':", reverseLookup(test_dict, 'apple'))  


# ------------------------------------------------------------------------------------------------- No137

# import random

# def бросить_две_кости():
#     кость1 = random.randint(1, 6)
#     кость2 = random.randint(1, 6)
#     return кость1 + кость2

# def основная():
#     количество_бросков = 1000
#     результаты = {сумма: 0 for сумма in range(2, 13)}  

#     # Симуляция бросков
#     for _ in range(количество_бросков):
#         результат = бросить_две_кости()
#         результаты[результат] += 1

#     теоретические_проценты = {
#         2: 2.78,
#         3: 5.56,
#         4: 8.33,
#         5: 11.11,
#         6: 13.89,
#         7: 16.67,
#         8: 13.89,
#         9: 11.11,
#         10: 8.33,
#         11: 5.56,
#         12: 2.78
#     }

    
#     print(f"{'Исход':>4} | {'Процент симуляции':>18} | {'Ожидаемый процент':>18}")
#     print('-' * 50)
#     for сумма in range(2, 13):
#         частота = (результаты[сумма] / количество_бросков) * 100
#         ожидаемый = теоретические_проценты[сумма]
#         print(f"{сумма:>4} | {частота:>18.2f} | {ожидаемый:>18.2f}")

# if __name__ == "__main__":
#     основная()
    

# ------------------------------------------------------------------------------------------------- No138


# symbol_to_keypress = {
#     '1': '1',            
#     '.': '1',
#     ',': '11',
#     '?': '111',
#     '!': '1111',
#     ':': '11111',
#     'A': '2', 'B': '22', 'C': '222',
#     'D': '3', 'E': '33', 'F': '333',
#     'G': '4', 'H': '44', 'I': '444',
#     'J': '5', 'K': '55', 'L': '555',
#     'M': '6', 'N': '66', 'O': '666',
#     'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
#     'T': '8', 'U': '88', 'V': '888',
#     'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
#     ' ': '0'
# }

# for ch in list(symbol_to_keypress.keys()):
#     if ch.isalpha():
#         symbol_to_keypress[ch.lower()] = symbol_to_keypress[ch]
# text = input("Введите текст: ")
# result = ""

# for ch in text:
#     if ch in symbol_to_keypress:
#         result += symbol_to_keypress[ch]
#     elif ch.lower() in symbol_to_keypress:
#         result += symbol_to_keypress[ch.lower()]

# print(result)


# ------------------------------------------------------------------------------------------------- No143


# word1 = input("Введите первое слово: ").strip()
# word2 = input("Введите второе слово: ").strip()

# def are_anagrams(w1, w2):
    
#     w1_lower = w1.lower()
#     w2_lower = w2.lower()
    
#     if len(w1_lower) != len(w2_lower):
#         return False
   
#     return sorted(w1_lower) == sorted(w2_lower)

# if are_anagrams(word1, word2):
#     print("Это анаграммы.")
# else:
#     print("Это не анаграммы.")



# ------------------------------------------------------------------------------------------------- No144


# import string

# def normalize_phrase(phrase):
    
#     translator = str.maketrans('', '', string.punctuation)
#     cleaned = phrase.translate(translator)
#     cleaned = cleaned.lower()
#     cleaned = cleaned.replace(' ', '')
#     return cleaned

# def are_phrases_anagrams(phrase1, phrase2):
   
#     normalized1 = normalize_phrase(phrase1)
#     normalized2 = normalize_phrase(phrase2)

#     return sorted(normalized1) == sorted(normalized2)

# phrase1 = "William Shakespeare"
# phrase2 = "I am a weakish speller"

# if are_phrases_anagrams(phrase1, phrase2):
#     print("Фразы являются анаграммами.")
# else:
#     print("Фразы не являются анаграммами.")


# ------------------------------------------------------------------------------------------------- No145


# letter_scores = {
#     **dict.fromkeys(['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'], 1),
#     **dict.fromkeys(['D', 'G'], 2),
#     **dict.fromkeys(['B', 'C', 'M', 'P'], 3),
#     **dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4),
#     **dict.fromkeys(['K'], 5),
#     **dict.fromkeys(['J', 'X'], 8),
#     **dict.fromkeys(['Q', 'Z'], 10)
# }

# word = input("Введите слово: ").upper()

# total_points = 0
# for letter in word:
#     if letter in letter_scores:
#         total_points += letter_scores[letter]
#     else:
#         print(f"Обнаружен недопустимый символ: {letter}")

#         continue

# print(f"Количество очков за слово '{word}': {total_points}")


# --------------------------------------------------------------------------------------------------