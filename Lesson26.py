# ----------------------------------------------------------------------------------------------------------------------------

# import random

# class House:
#     def __init__(self):
#         self.money = 100
#         self.food = 50
#         self.cat_food = 30
#         self.dirt = 0

#     def __str__(self):
#         return (f"Дом: деньги={self.money}, еда={self.food}, "
#                 f"кошачья еда={self.cat_food}, грязь={self.dirt}")

# class Human:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
#         self.fullness = 30
#         self.happiness = 100
#         self.eaten_food = 0
#         self.fur_coats = 0

#     def eat(self):
#         portion = min(30, self.house.food)
#         if portion == 0:
#             print(f"{self.name}: нет еды!")
#             self.fullness -= 10
#             return

#         print(f"{self.name} ест {portion} еды.")
#         self.house.food -= portion
#         self.fullness += portion
#         self.eaten_food += portion

#     def pet_cat(self):
#         print(f"{self.name} гладит кота. +5 счастья")
#         self.happiness += 5
#         self.fullness -= 10

#     def check_death(self):
#         if self.fullness <= 0:
#             print(f"❌ {self.name} умер от голода.")
#             return True
#         if self.happiness < 10:
#             print(f"❌ {self.name} умер от депрессии.")
#             return True
#         return False

#     def dirt_penalty(self):
#         if self.house.dirt > 90:
#             self.happiness -= 10

#     def __str__(self):
#         return f"{self.name}: сытость={self.fullness}, счастье={self.happiness}"

# class Husband(Human):
#     earned_money = 0

#     def work(self):
#         print(f"{self.name} работает. +150 денег")
#         self.house.money += 150
#         Husband.earned_money += 150
#         self.fullness -= 10

#     def play_games(self):
#         print(f"{self.name} играет. +20 счастья")
#         self.happiness += 20
#         self.fullness -= 10

#     def act(self):
#         self.dirt_penalty()
#         if self.check_death():
#             return False

#         if self.fullness < 20:
#             self.eat()
#         elif self.happiness < 20:
#             self.play_games()
#         else:
#             random.choice([self.work, self.play_games, self.pet_cat])()

#         return True

# class Wife(Human):
#     bought_food = 0
#     bought_cat_food = 0
#     fur_coats_bought = 0

#     def buy_food(self):
#         if self.house.money >= 50:
#             print(f"{self.name} покупает еды людям и коту.")
#             self.house.money -= 50
#             self.house.food += 50
#             self.house.cat_food += 10
#             Wife.bought_food += 50
#             Wife.bought_cat_food += 10
#             self.fullness -= 10
#         else:
#             print(f"{self.name}: нет денег на еду.")
#             self.fullness -= 10

#     def buy_fur_coat(self):
#         if self.house.money >= 350:
#             print(f"{self.name} покупает шубу! +60 счастья")
#             self.house.money -= 350
#             self.happiness += 60
#             self.fur_coats += 1
#             Wife.fur_coats_bought += 1
#             self.fullness -= 10
#         else:
#             print(f"{self.name}: недостаточно денег на шубу.")
#             self.fullness -= 10

#     def clean_house(self):
#         print(f"{self.name} убирается в доме (-100 грязи)")
#         self.house.dirt = max(0, self.house.dirt - 100)
#         self.fullness -= 10

#     def act(self):
#         self.dirt_penalty()
#         if self.check_death():
#             return False

#         if self.fullness < 20:
#             self.eat()
#         elif self.house.food < 20:
#             self.buy_food()
#         elif self.house.dirt > 120:
#             self.clean_house()
#         else:
#             random.choice([self.buy_food, self.buy_fur_coat, self.clean_house, self.pet_cat])()

#         return True

#     def __str__(self):
#         return (f"{self.name}: сытость={self.fullness}, счастье={self.happiness}, "
#                 f"шуб={self.fur_coats}")

# class Cat:
#     eaten_food = 0

#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
#         self.fullness = 30

#     def eat(self):
#         portion = min(10, self.house.cat_food)
#         if portion == 0:
#             print(f"{self.name}: нет кошачьей еды!")
#             self.fullness -= 10
#             return
#         print(f"{self.name} ест {portion} кошачьей еды.")
#         self.house.cat_food -= portion
#         self.fullness += portion * 2
#         Cat.eaten_food += portion

#     def sleep(self):
#         print(f"{self.name} спит.")
#         self.fullness -= 10

#     def tear_wallpaper(self):
#         print(f"{self.name} дерёт обои! +5 грязи")
#         self.house.dirt += 5
#         self.fullness -= 10

#     def act(self):
#         if self.fullness < 20:
#             self.eat()
#         else:
#             random.choice([self.sleep, self.tear_wallpaper])()

#         if self.fullness <= 0:
#             print(f"❌ Кот {self.name} умер от голода.")
#             return False
#         return True

#     def __str__(self):
#         return f"{self.name}: сытость={self.fullness}"

# def simulate_year():
#     house = House()
#     husband = Husband("Муж", house)
#     wife = Wife("Жена", house)
#     cat = Cat("Барсик", house)

#     for day in range(1, 366):
#         print(f"\n======== День {day} ========")
#         house.dirt += 5

#         if not husband.act(): break
#         if not wife.act(): break
#         if not cat.act(): break

#         print(husband)
#         print(wife)
#         print(cat)
#         print(house)

#     print("\n====== Итоги года ======")
#     print(f"Заработано денег: {Husband.earned_money}")
#     print(f"Съедено еды людьми: {husband.eaten_food + wife.eaten_food}")
#     print(f"Съедено кошачьей еды: {Cat.eaten_food}")
#     print(f"Куплено шуб: {Wife.fur_coats_bought}")

# simulate_year()

# ----------------------------------------------------------------------------------------------------------------------------

