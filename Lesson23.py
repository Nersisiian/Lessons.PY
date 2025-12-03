# class Прямоугольный:
#     def __init__(self, длина, ширина):
#         self.длина = длина
#         self.ширина = ширина

#     def периметр(self):
#         return 2 * (self.длина + self.ширина)

#     def площадь(self):
#         return self.длина * self.ширина

#     def __str__(self):
#         return f"Прямоугольник: длина = {self.длина}, ширина = {self.ширина}"

# if __name__ == "__main__":
#     прямоугольник = Прямоугольный(5, 3)
#     print(прямоугольник)
#     print("Периметр:", прямоугольник.периметр())
#     print("Площадь:", прямоугольник.площадь())

# ------------------------------------------------------------------------------------

# class Change:
#     def __init__(self, usd_rate, eur_rate, rub_rate):
        
#         self.usd_rate = usd_rate
#         self.eur_rate = eur_rate
#         self.rub_rate = rub_rate

#     def dram_to_usd(self, dram):
#         return dram / self.usd_rate

#     def dram_to_eur(self, dram):
#         return dram / self.eur_rate

#     def dram_to_rub(self, dram):
#         return dram / self.rub_rate

#     def usd_to_dram(self, usd):
#         return usd * self.usd_rate

#     def eur_to_dram(self, eur):
#         return eur * self.eur_rate

#     def rub_to_dram(self, rub):
#         return rub * self.rub_rate

#     def show_rates(self):
#         print("\n📊 Текущие курсы валют:")
#         print(f"1 USD = {self.usd_rate} AMD")
#         print(f"1 EUR = {self.eur_rate} AMD")
#         print(f"1 RUB = {self.rub_rate} AMD\n")


# def main():
#     change = Change(usd_rate=390.0, eur_rate=420.0, rub_rate=4.2)
#     change.show_rates()

#     while True:
#         print("Выберите действие:")
#         print("1 — Перевести драмы в валюту")
#         print("2 — Перевести валюту в драмы")
#         print("3 — Показать курсы")
#         print("0 — Выход")

#         выбор = input("👉 Ваш выбор: ").strip()

#         if выбор == "0":
#             print("До свидания 👋")
#             break

#         elif выбор == "1":
#             try:
#                 сумма = float(input("Введите сумму в драмах: "))
#                 валюта = input("Введите валюту (USD / EUR / RUB): ").upper()

#                 if валюта == "USD":
#                     print(f"{сумма} драм = {change.dram_to_usd(сумма):.2f} $")
#                 elif валюта == "EUR":
#                     print(f"{сумма} драм = {change.dram_to_eur(сумма):.2f} €")
#                 elif валюта == "RUB":
#                     print(f"{сумма} драм = {change.dram_to_rub(сумма):.2f} ₽")
#                 else:
#                     print("⚠️ Неизвестная валюта.\n")

#             except ValueError:
#                 print("⚠️ Ошибка ввода. Введите число.\n")

#         elif выбор == "2":
#             try:
#                 валюта = input("Введите валюту (USD / EUR / RUB): ").upper()
#                 сумма = float(input(f"Введите сумму в {валюта}: "))

#                 if валюта == "USD":
#                     print(f"{сумма} $ = {change.usd_to_dram(сумма):.2f} драм")
#                 elif валюта == "EUR":
#                     print(f"{сумма} € = {change.eur_to_dram(сумма):.2f} драм")
#                 elif валюта == "RUB":
#                     print(f"{сумма} ₽ = {change.rub_to_dram(сумма):.2f} драм")
#                 else:
#                     print("⚠️ Неизвестная валюта.\n")

#             except ValueError:
#                 print("⚠️ Ошибка ввода. Введите число.\n")

#         elif выбор == "3":
#             change.show_rates()

#         else:
#             print("⚠️ Неверный выбор. Попробуйте снова.\n")


# if __name__ == "__main__":
#     main()


# ------------------------------------------------------------------------------------

# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.__account_number = account_number
#         self.__balance = balance
#         self.transactions = []

#     def deposit(self, amount):
#         if amount <= 0:
#             print("❌ Сумма должна быть положительной.")
#             return
#         self.__balance += amount
#         self.transactions.append(f"Deposit: +{amount}")
#         print(f"✅ Пополнено: {amount}. Баланс: {self.__balance}")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("❌ Сумма должна быть положительной.")
#             return
#         if amount > self.__balance:
#             print("⚠️ Недостаточно средств.")
#             return
#         self.__balance -= amount
#         self.transactions.append(f"Withdrawal: -{amount}")
#         print(f"💸 Снято: {amount}. Баланс: {self.__balance}")

#     def transfer(self, other_account, amount):
#         if amount <= 0:
#             print("❌ Сумма должна быть положительной.")
#             return
#         if amount > self.__balance:
#             print("⚠️ Недостаточно средств для перевода.")
#             return
#         self.__balance -= amount
#         other_account.__balance += amount
#         self.transactions.append(f"Transfer to {other_account.__account_number}: -{amount}")
#         other_account.transactions.append(f"Transfer from {self.__account_number}: +{amount}")
#         print(f"🏦 Переведено {amount} на счёт {other_account.__account_number}")

#     def generate_statement(self):
#         print(f"\n📄 Выписка по счёту {self.__account_number}")
#         if not self.transactions:
#             print("Нет транзакций.")
#         else:
#             for t in self.transactions:
#                 print("•", t)
#         print(f"💰 Баланс: {self.__balance}\n")

#     def get_balance(self):
#         print(f"💰 Баланс счёта {self.__account_number}: {self.__balance}")
#         return self.__balance

#     def clear_transactions(self):
#         self.transactions.clear()
#         print("🧾 История транзакций очищена.")

#     def get_number(self):
#         return self.__account_number


# def main():
#     print("🏦 Добро пожаловать в банковскую систему!\n")

#     accounts = {
#         "001": BankAccount("001", 1000),
#         "002": BankAccount("002", 500),
#     }

#     while True:
#         print("\nВыберите действие:")
#         print("1 — Пополнить счёт")
#         print("2 — Снять деньги")
#         print("3 — Перевести между счетами")
#         print("4 — Показать выписку по счёту")
#         print("5 — Показать баланс")
#         print("6 — Очистить историю")
#         print("7 — Создать новый счёт")
#         print("0 — Выход")

#         choice = input("👉 Ваш выбор: ").strip()

#         if choice == "0":
#             print("👋 До свидания!")
#             break

#         elif choice == "7":
#             acc_num = input("Введите номер нового счёта: ")
#             if acc_num in accounts:
#                 print("⚠️ Такой счёт уже существует.")
#             else:
#                 accounts[acc_num] = BankAccount(acc_num)
#                 print(f"✅ Счёт {acc_num} успешно создан!")

#         elif choice in {"1", "2", "3", "4", "5", "6"}:
#             acc_num = input("Введите номер счёта: ")
#             if acc_num not in accounts:
#                 print("⚠️ Счёт не найден.")
#                 continue
#             account = accounts[acc_num]

#             if choice == "1":
#                 amount = float(input("Введите сумму для пополнения: "))
#                 account.deposit(amount)

#             elif choice == "2":
#                 amount = float(input("Введите сумму для снятия: "))
#                 account.withdraw(amount)

#             elif choice == "3":
#                 other_num = input("Введите номер счёта получателя: ")
#                 if other_num not in accounts:
#                     print("⚠️ Счёт получателя не найден.")
#                 else:
#                     amount = float(input("Введите сумму перевода: "))
#                     account.transfer(accounts[other_num], amount)

#             elif choice == "4":
#                 account.generate_statement()

#             elif choice == "5":
#                 account.get_balance()

#             elif choice == "6":
#                 account.clear_transactions()

#         else:
#             print("⚠️ Неверный выбор, попробуйте снова.")


# if __name__ == "__main__":
#     main()

# ------------------------------------------------------------------------------------

class TriangleChecker:
   
    def __init__(self):
        
        pass

    def is_triangle(self, a, b, c):

        if not all(isinstance(x, (int, float)) for x in [a, b, c]):
            return "Нужно вводить только числа!"

        if a <= 0 or b <= 0 or c <= 0:
            return "С отрицательными числами ничего не выйдет!"

        if (a + b > c) and (a + c > b) and (b + c > a):
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."
        
if __name__ == "__main__":
    checker = TriangleChecker()

    print(f"Тест (3, 4, 5): {checker.is_triangle(3, 4, 5)}") 

    print(f"Тест (1, 2, 10): {checker.is_triangle(1, 2, 10)}")  

    print(f"Тест (3, 4, -5): {checker.is_triangle(3, 4, -5)}")  

    print(f"Тест ('a', 4, 5): {checker.is_triangle('a', 4, 5)}") 

    print(f"Тест (5, 5, 5): {checker.is_triangle(5, 5, 5)}")  

    print(f"Тест (1, 2, 3): {checker.is_triangle(1, 2, 3)}")  

