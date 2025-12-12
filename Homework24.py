# --------------------------------------------------------------------------------------------- Codewars 

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
    
# ---------------------------------------------------------------------------------------------

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time

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
#         print(f"1 USD = {self.usd_rate:.2f} AMD")
#         print(f"1 EUR = {self.eur_rate:.2f} AMD")
#         print(f"1 RUB = {self.rub_rate:.2f} AMD\n")

# def fetch_rates():
    
#     service = Service('/path/to/chromedriver')
#     driver = webdriver.Chrome(service=service)
#     try:
#         driver.get('https://rate.am/en/foreign-currency-rates/armenia/armenia-central-bank/?amount=1&from=USD&to=AMD')
#         time.sleep(2)  

#         usd_elem = driver.find_element(By.XPATH, '//td[contains(text(),"USD")]/following-sibling::td')
#         usd_rate = float(usd_elem.text.replace(',', '').strip())
        
#         driver.get('https://rate.am/en/foreign-currency-rates/armenia/armenia-central-bank/?amount=1&from=EUR&to=AMD')
#         time.sleep(2)
#         eur_elem = driver.find_element(By.XPATH, '//td[contains(text(),"EUR")]/following-sibling::td')
#         eur_rate = float(eur_elem.text.replace(',', '').strip())

#         driver.get('https://rate.am/en/foreign-currency-rates/armenia/armenia-central-bank/?amount=1&from=RUB&to=AMD')
#         time.sleep(2)
#         rub_elem = driver.find_element(By.XPATH, '//td[contains(text(),"RUB")]/following-sibling::td')
#         rub_rate = float(rub_elem.text.replace(',', '').strip())

#         return usd_rate, eur_rate, rub_rate
#     finally:
#         driver.quit()

# def main():
#     print("Загружаем курсы с rate.am …")
#     try:
#         usd_rate, eur_rate, rub_rate = fetch_rates()
#     except Exception as e:
#         print("Ошибка загрузки курсов:", e)
        
#         usd_rate, eur_rate, rub_rate = 390.0, 420.0, 4.2

#     change = Change(usd_rate=usd_rate, eur_rate=eur_rate, rub_rate=rub_rate)
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

# Download

# pip install selenium webdriver-manager

# ---------------------------------------------------------------------------------------------