
# print("Угадай число: введи a, b или c (a=1, b=2, c=3)")

# guess = input("Ваш выбор: ").strip().lower()

# a = (guess == "a")
# b = (guess == "b")
# c = (guess == "c")

# win = (
#     (a and not b and not c) or
#     (b and not a and not c) or
#     (c and not a and not b)
# )

# if win:
#     print("Правильно! Вы победили.")
# else:
#     print("Неправильно. Попробуйте ещё раз.")



# years_input = input("Введите возраст собаки в годах: ")
# try:
#     years = float(years_input)
# except ValueError:
#     years = 0.0

# human_years = (years <= 2) * (years * 10.5) + (years > 2) * (21.0 + (years - 2) * 4.0)

# print("Эквивалентный возраст в человеческих годах:", human_years)
