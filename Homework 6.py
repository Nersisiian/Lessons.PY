# def main():
#     total = 0.0
#     count = 0
#     first_input = True

#     while True:
#         try:
#             s = input("Введите число (0 для завершения): ")
#             x = float(s)
#         except ValueError:
#             print("Ошибка: введено не число. Попробуйте снова.")
#             continue

#         if first_input and x == 0:
#             print("Ошибка: первое введённое значение равно нулю.")
#             return
#         first_input = False

#         if x == 0:
#             break

#         total += x
#         count += 1

#     if count == 0:
#         print("Нет чисел для вычисления среднего.")
#     else:
#         average = total / count
#         print(f"Среднее значение: {average:.2f}")

# if __name__ == "__main__":
#     main()
    
# Xndir 63



# amounts = [4.95, 9.95, 14.95, 19.95, 24.95]
# discount_rate = 0.60

# print(f"{'Original Price':>15}  {'Discount':>12}  {'New Price':>12}")
# print("-" * 45)

# for original in amounts:
#     discount = original * discount_rate
#     new_price = original * (1 - discount_rate)
#     print(f"${original:>13.2f}  ${discount:>11.2f}  ${new_price:>11.2f}")
    
# Xndir 64


# def main():
#     print(f"{'Celsius (°C)':>15}  {'Fahrenheit (°F)':>15}")
#     print("-" * 32)

#     for c in range(0, 101, 10):
#         f = c * 9 / 5 + 32
#         print(f"{c:>15.0f}  {f:>15.1f}")

# if __name__ == "__main__":
#     main()

# Xndir 65



# n = int(input("Введите целое число: "))
# result = ""
# q = n

# while q != 0:
    
#     r = q % 2
#     result = str(r) + result
#     q = q // 2

# if result == "":
#     result = "0"

# print("Двоичное представление:", result)

# Xndir 82


# import random

# N = 100
# numbers = [random.randint(1, 100) for _ in range(N)]

# max_value = numbers[0]
# updates = 0
# print(numbers[0])
# for x in numbers[1:]:
#     if x > max_value:
#         max_value = x
#         updates += 1
#         print(f"{x} <== Обновление")
#     else:
#         print(x)

# print()
# print(f"Максимальное значение в ряду: {max_value}")
# print(f"Количество смен максимального значения: {updates}")

# # Xndir 83


import random

def simulate_one():
    sequence = []
    count = 0
    last = None
    streak = 0

    while True:
        flip = random.randint(0, 1)  # 0 -> О, 1 -> Р
        symbol = 'О' if flip == 0 else 'Р'
        sequence.append(symbol)
        count += 1

        if symbol == last:
            streak += 1
        else:
            last = symbol
            streak = 1

        if streak == 3:
            break

    return sequence, count

def main():
    simulations = 10
    results = []
    counts = []

    for _ in range(simulations):
        seq, c = simulate_one()
        results.append(seq)
        counts.append(c)

    for seq, c in zip(results, counts):
        print(' '.join(seq) + f" (попыток: {c})")
    avg = sum(counts) / len(counts)
    avg_str = f"{avg:.1f}".replace('.', ',')
    print(f"Среднее количество попыток: {avg_str}")

if __name__ == "__main__":
    main()

# Xndir 84



