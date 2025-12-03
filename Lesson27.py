# --------------------------------------------------------------------

# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number    
#         self.__balance = balance  
#         self.__transactions = []  

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.__transactions.append(f"Deposit: {amount}")
#         else:
#             print("Deposit amount must be positive")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             self.__transactions.append(f"Withdrawal: {amount}")
#         else:
#             print("Insufficient balance or invalid withdrawal amount")

#     def transfer(self, amount, to_account):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             to_account.deposit(amount)
#             self.__transactions.append(f"Transfer to {to_account.account_number}: {amount}")
#         else:
#             print("Insufficient balance or invalid transfer amount")

#     def get_balance(self):
#         return self.__balance

#     def clear_transactions(self):
#         self.__transactions.clear()

#     def transaction_statement(self):
#         return self.__transactions

# if __name__ == "__main__":
#     account1 = BankAccount("123456789", 1000)
#     account2 = BankAccount("987654321", 500)

#     account1.deposit(200)
#     account1.withdraw(150)
#     account1.transfer(100, account2)

#     print(f"Account 1 Balance: {account1.get_balance()}")
#     print(f"Account 2 Balance: {account2.get_balance()}")
#     print("Transaction History:", account1.transaction_statement())

#     account1.clear_transactions()
#     print("Transaction History after clearing:", account1.transaction_statement())

# --------------------------------------------------------------------------------------------- Codewars Pagination Helper

# class PaginationHelper:
    
#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.items_per_page = items_per_page

#     def item_count(self):
#         return len(self.collection)

#     def page_count(self):
        
#         return (len(self.collection) + self.items_per_page - 1) // self.items_per_page

#     def page_item_count(self, page_index):
#         if page_index < 0 or page_index >= self.page_count():
#             return -1
        
#         if page_index == self.page_count() - 1:
#             return len(self.collection) % self.items_per_page or self.items_per_page
#         return self.items_per_page

#     def page_index(self, item_index):
#         if item_index < 0 or item_index >= len(self.collection):
#             return -1
#         return item_index // self.items_per_page

# --------------------------------------------------------------------------------------------- OOP Exercise 1

# class Soda:
#     def __init__(self, addition=None):
#         self.addition = addition

#     def show_my_drink(self):
#         if self.addition:
#             print(f"Газировка и {self.addition}")
#         else:
#             print("Обычная газировка")

# drink1 = Soda("лимон")
# drink2 = Soda()

# drink1.show_my_drink()  
# drink2.show_my_drink()   

# --------------------------------------------------------------------------------------------- OOP Exercise 2

# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.sides = (a, b, c)

#     def is_triangle(self):
#         a, b, c = self.sides

#         if not all(isinstance(x, (int, float)) for x in self.sides):
#             return "Нужно вводить только числа!"

#         if a <= 0 or b <= 0 or c <= 0:
#             return "С отрицательными числами ничего не выйдет!"

#         if a + b > c and a + c > b and b + c > a:
#             return "Ура, можно построить треугольник!"
#         else:
#             return "Жаль, но из этого треугольник не сделать."
        
# t1 = TriangleChecker(3, 4, 5)
# print(t1.is_triangle())  

# t2 = TriangleChecker(-1, 4, 5)
# print(t2.is_triangle())   

# t3 = TriangleChecker(1, "a", 3)
# print(t3.is_triangle()) 

# t4 = TriangleChecker(1, 2, 3)
# print(t4.is_triangle())

# --------------------------------------------------------------------------------------------- OOP Exercise 3

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg  

#     @property
#     def kg(self):
        
#         return self.__kg

#     @kg.setter
#     def kg(self, value):
        
#         if value < 0:
#             raise ValueError("Вес не может быть отрицательным!")
#         self.__kg = value

#     def to_pounds(self):
#         return self.__kg * 2.205
    
# obj = KgToPounds(10)

# print(obj.kg)           
# print(obj.to_pounds())  

# obj.kg = 15             
# print(obj.to_pounds())  

# --------------------------------------------------------------------------------------------- OOP Exercise 4

# class Nikola:

#     __slots__ = ("name", "age") 

#     def __init__(self, name, age):
#         if name == "Николай":
#             self.name = name
#         else:
#             self.name = f"Я не {name}, а Николай"
#         self.age = age

# class RealString:
  
#     def __init__(self, string):
#         self.string = string

#     def __len__(self):
#         return len(self.string)

#     def __gt__(self, other):
#         if isinstance(other, RealString):
#             return len(self) > len(other)
#         return len(self) > len(other)

#     def __lt__(self, other):
#         if isinstance(other, RealString):
#             return len(self) < len(other)
#         return len(self) < len(other)

#     def __eq__(self, other):
#         if isinstance(other, RealString):
#             return len(self) == len(other)
#         return len(self) == len(other)

# if __name__ == "__main__":

#     print("=== Тест Nikola ===")
#     n1 = Nikola("Николай", 30)
#     print(n1.name)              

#     n2 = Nikola("Максим", 25)
#     print(n2.name)              
    
#     try:
#         n1.отчество = "Иванович"
#     except AttributeError as e:
#         print("Ошибка:", e)


#     print("\n=== Тест RealString ===")
#     a = RealString("Привет")
#     b = RealString("Hi")

#     print(a > b)                 
#     print(a < "Python")          
#     print("Test" == b)        

# --------------------------------------------------------------------------------------------- Codewars Vector Class

# import math

# class Vector:
#     def __init__(self, components):
#         self.components = components

#     def _check_length(self, other):
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must be of same length")

#     def add(self, other):
#         self._check_length(other)
#         return Vector([a + b for a, b in zip(self.components, other.components)])

#     def subtract(self, other):
#         self._check_length(other)
#         return Vector([a - b for a, b in zip(self.components, other.components)])

#     def dot(self, other):
#         self._check_length(other)
#         return sum(a * b for a, b in zip(self.components, other.components))

#     def norm(self):
#         return math.sqrt(sum(x * x for x in self.components))

#     def equals(self, other):
#         return self.components == other.components

#     def __str__(self):
#         return "(" + ",".join(str(x) for x in self.components) + ")"

#     __repr__ = __str__

# a = Vector([1,2,3])
# b = Vector([3,4,5])
# print(a.add(b))

# ----------------------------------------------------------------------------------------------





    




