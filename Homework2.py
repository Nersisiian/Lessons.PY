# имя = input("Введите ваше имя: ")
# print(f"Привет, {имя}!")
# Xndir 2. 


# length = float(input("Введите длину комнаты в метрах: "))
# width = float(input("Введите ширину комнаты в метрах: "))
# area = length * width
# print(f"Площадь комнаты составляет {area:.2f} квадратных метров.")
# Xndir 3.  


# length_feet = float(input("Введите длину участка в футах: "))
# width_feet = float(input("Введите ширину участка в футах: "))
# area_sq_feet = length_feet * width_feet
# area_acres = area_sq_feet / 43560
# print(f"Площадь участка составляет примерно {area_acres:.4f} акров.")  
# Xndir 4


# small_bottles = int(input("Введите количество бутылок объемом 1 литр и меньше: "))
# large_bottles = int(input("Введите количество бутылок объемом больше 1 литра: "))
# cost_small = 0.10
# cost_large = 0.25
# total_amount = small_bottles * cost_small + large_bottles * cost_large
# print("Общая сумма: ${:.2f}".format(total_amount))
# Xndir5


# summa_order = float(input("Введите сумму заказа в ресторане: "))
# tax_rate = 0.10
# tax = summa_order * tax_rate
# tips = summa_order * 0.18
# total = summa_order + tax + tips
# print(f"Налог: {tax:.2f}")
# print(f"Чаевые: {tips:.2f}")
# print(f"Общий итог: {total:.2f}")
# Xndir 6


# coin_denominations = [200, 100, 25, 10, 5, 1]
# amount = int(input("Введите сумму сдачи в центах: "))
# coins_used = {}
# for coin in coin_denominations:
#     count = amount // coin  
#     amount = amount % coin  
#     coins_used[coin] = count
# print("Для выдачи сдачи потребуется:")
# for coin in coin_denominations:
#     count = coins_used[coin]
#     if count > 0:
#         if coin == 200:
#             print(f"{count} монет(ы) по 2 доллара (toonie)")
#         elif coin == 100:
#             print(f"{count} монет(ы) по 1 доллару (loonie)")
#         else:
#             print(f"{count} монет(ы) по {coin} центов")
# Xndir 13


# number = int(input("Введите четырёхзначное число: "))

# if number < 1000 or number > 9999:
#     print("Ошибка: введено не четырёхзначное число.")
# else:
  
#     digits_str = str(number)
    
#     sum_digits = 0
#     digits_list = []

#     for digit in digits_str:
#         d = int(digit)
#         digits_list.append(d)
#         sum_digits += d

#     result_str = " + ".join(str(d) for d in digits_list)
#     print(f"{result_str} = {sum_digits}")
# Xndir 32


# price_per_bread = 3.49  
# discount = 60  
# quantity = int(input("Введите количество приобретенных вчерашних буханок хлеба: "))
# discounted_price = price_per_bread * (1 - discount / 100)
# total_cost = discounted_price * quantity
# print(f"Обычная цена за буханку: {price_per_bread:10.2f}")
# print(f"Цена со скидкой: {discounted_price:10.2f}")
# print(f"Общая стоимость приобретенного хлеба: {total_cost:10.2f}")
# Xndir 34







