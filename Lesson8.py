# n = 10  
# print("\t", end="")  
# for c in range(1, n + 1):
#     print(c, end="\t")
# print() 
# for r in range(1, n + 1):
#     print(r, end="\t")  
#     for c in range(1, n + 1):
#         print(r * c, end="\t")  
    # print()  


# N = int(input("Введите число N: "))
# for i in range(1, N + 1):
#     for j in range(1, i + 1):
#         print(j, end='\t')
#     print()


# width = int(input("Введите ширину рамки: "))
# height = int(input("Введите высоту рамки: "))
# print('-' * width)
# for _ in range(height - 2):
#     print('|' + ' ' * (width - 2) + '|')
# if height > 1:
#     print('-' * width)



# width = int(input("Введите ширину рамки: "))
# height = int(input("Введите высоту рамки: "))

# for _ in range(width):
#     print('-', end='')
# print()

# for _ in range(height - 2):
#     print('|', end='')
#     for _ in range(width - 2):
#         print(' ', end='')
#     print('|')

# if height > 1:
#     for _ in range(width):
#         print('-', end='')
#     print()



# N = int(input("Введите размер квадрата: "))

# for i in range(N):
#     for j in range(N):
#         if i == j or i + j == N - 1:
#             print('^', end=' ')
#         else:
#             print(' ', end=' ')
#     print()


# def is_prime(n: int) -> bool:
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     w = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += w
#         w = 6 - w
#     return True

# def main():
#     n = int(input("Введите кол-во чисел: "))
#     count_primes = 0
#     for _ in range(n):
#         x = int(input("Введите число: "))
#         if is_prime(x):
#             count_primes += 1
#     print(f"Количество простых чисел в последовательности: {count_primes}")

# if __name__ == "__main__":
#     main()


# n = int(input("Введите число N: "))
# fact = 1
# total = 0
# for i in range(1, max(n, 0) + 1):
#     fact *= i
#     total += fact
# print(f"Сумма факториалов от 1 до {n} равна {total}.")


# def sum_digits(n):
#     return sum(int(ch) for ch in str(abs(n)) if ch.isdigit())

# def main():
#     try:
#         N = int(input("Введите количество чисел N: "))
#     except ValueError:
#         print("Неправильный ввод. Ожидалось целое число N.")
#         return

#     best_num = None
#     best_sum = -1

#     for _ in range(N):
#         try:
#             x = int(input("Введите число: "))
#         except ValueError:
#             print("Неправильный ввод. Ожидалось целое число.")
#             return

#         s = sum_digits(x)

#         if s > best_sum or (s == best_sum and (best_num is None or x > best_num)):
#             best_sum = s
#             best_num = x

#     if best_num is None:
#         print("Не введены действительные числа.")
#         return

#     print(f"Число с наибольшей суммой цифр: {best_num}")
#     print(f"Сумма цифр этого числа: {best_sum}")

# if __name__ == "__main__":
#     main()


# h = int(input("Введите высоту пирамиды: "))

# for i in range(1, h + 1):
#     print(' ' * (h - i) + '#' * (2 * i - 1))


# n = int(input("Введите количество уровней пирамиды: "))

# next_odd = 1
# for i in range(1, n + 1):
#     row = []
#     for _ in range(i):
#         row.append(str(next_odd))
#         next_odd += 2
#     print(" ".join(row))



def yaма(N):
    
    cur = 1
    total_rows = N
    lines = []

  
    left = []
    right = []

   
    for i in range(N):
        left.append(cur)
        cur += 1
        right.append(cur)
        cur += 1


    for i in range(N):
       
        lead = i
        if i == N - 1:
            
            s = " " * lead + str(left[i] if i < len(left) else "")  
            lines.append(s)
        else:
            
            inner = (N - 1 - i) * 2 - 1
            left_num = str(left[i])
            right_num = str(right[i])
            s = " " * lead + left_num
            s += " " * inner + right_num
            lines.append(s)

    
    for line in lines:
        print(line)

if __name__ == "__main__":
    try:
        s = input("Введите N: ")
        N = int(s)
        if N <= 0:
            print("N должно быть положительным целым числом.")
        else:
            yaма(N)
    except Exception as e:
        print("Ошибка ввода:", e)
