# ----------------------------------------------------------------------------------------------------

# import math

# class CovidTest:
#     def __init__(self, temperature):
#         self.temperature = temperature

#     def check(self):
#         result = math.ceil(self.temperature * math.pi)
#         if 120 <= result <= 128:
#             return "You Have coronavirus"
#         else:
#             return "Everything is ok"

# try:
#     temp = float(input("Enter your body temperature in Celsius: "))
#     test = CovidTest(temp)
#     print(test.check())
# except ValueError:
#     print("❌ Please enter a valid number (e.g. 36.6)")

# ----------------------------------------------------------------------------------------------------

# import math

# class NameNumber:
#     def __init__(self, name):
#         self.name = name.lower()

#     def get_number(self):
#         chart = {
#             1: "ajs", 2: "bkt", 3: "clu", 4: "dmv",
#             5: "enw", 6: "fox", 7: "gpy", 8: "hqz", 9: "ir"
#         }
#         total = 0
#         for ch in self.name:
#             for num, letters in chart.items():
#                 if ch in letters:
#                     total += num
#                     break
#         return total

#     def is_widespread(self):
#         number = self.get_number()
#         result = math.sqrt(number)
#         if result < 5:
#             return f"{number}, Yes"
#         else:
#             return f"{number}, No"

# name = input("Enter your name: ")
# test = NameNumber(name)
# print(test.is_widespread())

# ----------------------------------------------------------------------------------------------------

# import random

# class HarryPotter:
#     def __init__(self, w1, w2, w3):
#         self.harry_words = [w1, w2, w3]
#         self.magic_words = ["Avada Kedavra", "Crucio", "Imperio"]

#     def fight(self):

#         voldemort_words = [random.choice(self.magic_words) for _ in range(3)]

#         score = 0
#         for h, v in zip(self.harry_words, voldemort_words):
#             if h == v:
#                 score += 1
#             else:
#                 score -= 1

#         print(" ".join(voldemort_words))

#         if score >= 2 or self.harry_words.count("Avada Kedavra") + \
#            self.harry_words.count("Crucio") + \
#            self.harry_words.count("Imperio") >= 2 and score > 0:
#             print("You win")
#         elif score >= 0 and self.harry_words.count("Avada Kedavra") + \
#              self.harry_words.count("Crucio") + \
#              self.harry_words.count("Imperio") >= 2:
#             print("You win")
#         else:
#             print("You lose")

# w1 = input()
# w2 = input()
# w3 = input()

# game = HarryPotter(w1, w2, w3)
# game.fight()

# ----------------------------------------------------------------------------------------------------

