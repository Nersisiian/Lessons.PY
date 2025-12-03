# ----------------------------------------------------------------------------------------------------------

# BASE_FARE = 4.00           
# RATE_PER_140M = 0.25       

# import math

# def calculate_taxi_fare(distance_km):
  
#     distance_meters = distance_km * 1000    
#     segments = math.ceil(distance_meters / 140)
#     distance_fare = segments * RATE_PER_140M
#     total_fare = BASE_FARE + distance_fare
    
#     return total_fare

# def main():

#     try:
#         distance_km = float(input("Введите расстояние поездки в километрах: "))
#         fare = calculate_taxi_fare(distance_km)
#         print(f"Стоимость поездки длиной {distance_km} км составляет: ${fare:.2f}")
#     except ValueError:
#         print("Пожалуйста, введите корректное числовое значение для расстояния.")

# if __name__ == "__main__":
#     main()

# ----------------------------------------------------------------------------------------------------------

# def расчет_стоимости_доставки(количество_товаров):
#     цена_первого_товара = 10.95
#     цена_последующих = 2.95
    
#     if количество_товаров <= 0:
#         return 0  
    
#     if количество_товаров == 1:
#         return цена_первого_товара
#     else:
        
#         общая_стоимость = цена_первого_товара + (количество_товаров - 1) * цена_последующих
#         return общая_стоимость

# try:
#     количество = int(input("Введите количество товаров в заказе: "))
#     if количество < 0:
#         print("Количество товаров не может быть отрицательным.")
#     else:
#         сумма_доставки = расчет_стоимости_доставки(количество)
#         print(f"Общая стоимость доставки: ${сумма_доставки:.2f}")
# except ValueError:
#     print("Пожалуйста, введите корректное целое число.")

# ----------------------------------------------------------------------------------------------------------

# def is_prime(n):
    
#     if n <= 1:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     sqrt_n = int(n**0.5) + 1
#     for i in range(3, sqrt_n, 2):
#         if n % i == 0:
#             return False
#     return True

# if __name__ == "__main__":
#     try:
#         num = int(input("Введите целое число: "))
#         if is_prime(num):
#             print(f"{num} является простым числом.")
#         else:
#             print(f"{num} не является простым числом.")
#     except ValueError:
#         print("Пожалуйста, введите корректное целое число.")

# ----------------------------------------------------------------------------------------------------------

# def isPrime(num):
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def nextPrime(n):
#     candidate = n + 1
#     while not isPrime(candidate):
#         candidate += 1
#     return candidate

# def main():
#     n = int(input("Введите число: "))
#     result = nextPrime(n)
#     print("Следующее простое число большее за", n, "— это", result)

# if __name__ == "__main__":
#     main()

# ----------------------------------------------------------------------------------------------------------

# Предполагается, что функция is_prime из упражнения 98 уже реализована и импортирована.

# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def nextPrime(n):
#     candidate = n + 1
#     while True:
#         if is_prime(candidate):
#             return candidate
#         candidate += 1

# if __name__ == "__main__":
#     try:
#         n = int(input("Введите число: "))
#         print(f"Следующее простое число после {n} — {nextPrime(n)}")
#     except ValueError:
#         print("Пожалуйста, введите целое число.")

# ----------------------------------------------------------------------------------------------------------

