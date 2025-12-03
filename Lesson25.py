# import random

# class Warrior:
#     def __init__(self, name):
#         self.name = name
#         self.health = 100

#     def attack(self, other):
#         hit_chance = random.random()  
#         if hit_chance > 0.2:  
#             other.health -= 20
#             print(f"{self.name} попал по {other.name}! У {other.name} осталось {other.health} здоровья.")
#         else:
#             print(f"{self.name} промахнулся по {other.name}!")

#     def is_alive(self):
#         return self.health > 0

# warrior1 = Warrior("Алексей")
# warrior2 = Warrior("Борис")

# round_number = 1
# while warrior1.is_alive() and warrior2.is_alive():
#     print(f"\nРаунд {round_number}")
#     warrior1.attack(warrior2)
#     if warrior2.is_alive():
#         warrior2.attack(warrior1)
#     round_number += 1

# if warrior1.is_alive():
#     print(f"\nПобедил {warrior1.name}!")
# else:
#     print(f"\nПобедил {warrior2.name}!")


# -----------------------------------------------------------------------------------------------------------------------

# import math

# class Circle:
#     def __init__(self, x=0, y=0, r=1):
#         self.x = x
#         self.y = y
#         self.r = r

#     def area(self):
#         return math.pi * self.r ** 2

#     def perimeter(self):
#         return 2 * math.pi * self.r

#     def resize(self, k):
#         self.r *= k

#     def intersects(self, other):
        
#         distance_centers = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
#         return distance_centers <= (self.r + other.r)

# circle1 = Circle()
# circle2 = Circle(2, 2, 3)

# print("Площадь первого круга:", circle1.area())
# print("Периметр первого круга:", circle1.perimeter())

# circle1.resize(2)
# print("Увеличенный радиус первого круга:", circle1.r)

# print("Пересекаются ли круги:", circle1.intersects(circle2))

# -----------------------------------------------------------------------------------------------------------------------

# class Student:
#     def __init__(self, name, group_number, grades):
#         self.name = name
#         self.group_number = group_number
#         self.grades = grades

#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)


# students = [
#     Student("Alice", "Group 1", [85, 90, 78]),
#     Student("Bob", "Group 1", [82, 88, 91]),
#     Student("Charlie", "Group 2", [79, 84, 80]),
#     Student("David", "Group 2", [95, 92, 88]),
#     Student("Eva", "Group 1", [76, 80, 85]),
#     Student("Frank", "Group 2", [83, 87, 90]),
#     Student("Grace", "Group 1", [91, 92, 94]),
#     Student("Henry", "Group 2", [75, 78, 77]),
#     Student("Isla", "Group 1", [89, 88, 90]),
#     Student("Jack", "Group 2", [82, 81, 80])
# ]


# sorted_students = sorted(students, key=lambda s: s.average_grade(), reverse=True)

# print("Список студентов по среднему баллу:")
# for student in sorted_students:
#     print(f"Имя: {student.name}, Группа: {student.group_number}, Средний балл: {student.average_grade():.2f}")

# -----------------------------------------------------------------------------------------------------------------------

# import math

# class COVIDCheck:
#     def __init__(self, temperature):
#         self.temperature = temperature

#     def check_coronavirus(self):
        
#         result = (self.temperature * 2) + math.pi
        
#         rounded_result = round(result)
        
#         if 120 <= rounded_result <= 128:
#             return "Вы имеете коронавирус."
#         else:
#             return "У вас нет коронавируса."

# temperature_input = float(input("Введите вашу температуру в градусах Цельсия: "))
# covid_check = COVIDCheck(temperature_input)
# result = covid_check.check_coronavirus()
# print(result)

# -----------------------------------------------------------------------------------------------------------------------

# import math

# class NameNumber:
#     def __init__(self, name):
#         self.name = name.lower()  

#     def count_wide_letters(self):
        
#         wide_letters = "b, d, f, h, k, l, m, n, p, q, r, t"
#         count = sum(1 for char in self.name if char in wide_letters)
#         return count

#     def is_name_wide(self):
#         square_root_length = math.sqrt(len(self.name))
#         return square_root_length < 5

#     def check_name(self):
#         wide_count = self.count_wide_letters()
#         name_wide = self.is_name_wide()

#         if name_wide:
#             return f"Количество широких букв: {wide_count}, имя широко распространено."
#         else:
#             return f"Количество широких букв: {wide_count}, имя не широко распространено."

# name_input = input("Введите ваше имя: ")
# name_checker = NameNumber(name_input)
# result = name_checker.check_name()
# print(result)

# -----------------------------------------------------------------------------------------------------------------------
class NameAnalyzer:
    def __init__(self, name):
        self.name = name.lower() 

    def get_letter_numbers(self):
        
        letter_values = {
            'a': 1, 'j': 1, 'b': 2, 'k': 2, 'c': 3, 'l': 4,
            'd': 4, 'm': 5, 'e': 5, 'n': 6, 'f': 6, 'o': 7,
            'g': 7, 'p': 8, 'h': 8, 'q': 9, 'i': 9, 'r': 9,
            's': 1, 't': 2, 'u': 4, 'v': 5, 'w': 6, 'x': 7,
            'y': 8, 'z': 9
        }
        return [letter_values[char] for char in self.name if char in letter_values]

    def is_widespread(self):
        name_length = len(self.name)
        return name_length < 5
        
    def analyze_name(self):
        letter_numbers = self.get_letter_numbers()
        is_widespread = self.is_widespread()
        
        return {
            'letter_numbers': letter_numbers,
            'is_widespread': is_widespread
        }

name_input = input("Введите ваше имя: ")
name_analyzer = NameAnalyzer(name_input)
result = name_analyzer.analyze_name()

print(f"Числа, соответствующие буквам: {result['letter_numbers']}")
print("Имя широко распространено." if result['is_widespread'] else "Имя не широко распространено.")