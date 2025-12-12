# def all_sublists(lst):
#     result = [[]]
#     n = len(lst)
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             result.append(lst[i:j])
#     return result

# def main():
#     a = [1, 2, 3]
#     subs = all_sublists(a)
#     print("Все подсписки:", subs)

# if __name__ == "__main__":
#     main()
# Xndir134


# numbers = []

# while True:
#     s = input("Введите число (или нажмите Enter для завершения): ")
#     if s.strip() == "":
#         break
#     try:
#         x = float(s)
#         numbers.append(x)
#     except ValueError:
#         print("Некорректный ввод. Введите число или просто Enter.")

# if not numbers:
#     print("Нет введённых чисел.")
# else:
#     avg = sum(numbers) / len(numbers)

#     print("Среднее значение введённого ряда чисел:", avg)

#     below = [x for x in numbers if x < avg]
#     equal = [x for x in numbers if x == avg]
#     above = [x for x in numbers if x > avg]

#     print("Числа ниже среднего:")
#     print(" ".join(str(x) for x in below))

#     print("Числа равные среднему:")
#     print(" ".join(str(x) for x in equal))

#     print("Числа выше среднего:")
#     print(" ".join(str(x) for x in above))
# Xndir 114


# def proper_divisors(n):

#     if n <= 1:
#         return []

#     divisors = [1]  
#     limit = int(n ** 0.5)

#     for i in range(2, limit + 1):
#         if n % i == 0:
#             comp = n // i
#             divisors.append(i)
#             if comp != i:
#                 divisors.append(comp)

#     divisors.sort()
#     return divisors


# if __name__ == "__main__":
#     try:
#         user_input = input("Введите число: ")
#         number = int(user_input)
#     except ValueError:
#         print("Некорректный ввод. Пожалуйста, введите целое число.")
#     else:
#         result = proper_divisors(number)
#         print("Собственные делители числа", number, ":", result)
# Xndir 115


import random

def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [f'{r}{s}' for s in suits for r in ranks]
    random.shuffle(deck)
    return deck

def card_value(card):
    rank = card[:-1]  
    if rank in ['J', 'Q', 'K']:
        return 10
    if rank == 'A':
        return 11  
    return int(rank)

def calculate_score(hand):
    score = sum(card_value(c) for c in hand)
    
    aces = sum(1 for c in hand if c[:-1] == 'A')
    
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
    return score

def print_hand(name, hand, hide_first_card=False):
    if hide_first_card:
        
        print(f"{name} hand: [hidden], " + ", ".join(hand[1:]))
    else:
        print(f"{name} hand: {', '.join(hand)}  ->  score: {calculate_score(hand)}")

def is_blackjack(hand):
    return calculate_score(hand) == 21 and len(hand) == 2

def play_round(balance=100):
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    print("\nНовая партия началась.")
    print_hand("Ваш", player_hand)
    print("Д dealer shows: " + dealer_hand[0])  

    if is_blackjack(player_hand):
        if is_blackjack(dealer_hand):
            print("Оба черные джекпоты! Ничья.")
            return 0
        else:
            print("У вас Blackjack! Вы выигрываете.")
            return 1  

    if is_blackjack(dealer_hand):
        print_hand("Дилер", dealer_hand)
        print("У дилера Blackjack. Вы проиграли.")
        return -1

    
    while True:
        move = input("Ваш ход: 'hit' (взять карту) или 'stand' (остановиться): ").strip().lower()
        if move == 'hit':
            new_card = deck.pop()
            player_hand.append(new_card)
            print_hand("Ваш", player_hand)
            if calculate_score(player_hand) > 21:
                print("Ваш счёт > 21. Перебор. Вы проиграли.")
                return -1
            if calculate_score(player_hand) == 21:
                print("21! Переберите ход? Обычно остаются.")
        elif move == 'stand':
            break
        else:
            print("Пожалуйста, введите 'hit' или 'stand'.")

    print_hand("Дилер", dealer_hand)
    while calculate_score(dealer_hand) < 17:
        new_card = deck.pop()
        dealer_hand.append(new_card)
        print("Дилер берет карту:", new_card)
        print_hand("Дилер", dealer_hand)

    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)

    print(f"Ваш итог: {player_score} | Итог дилера: {dealer_score}")

    if dealer_score > 21:
        print("Дилер перебрал. Вы выигрываете.")
        return 1
    if player_score > dealer_score:
        print("Вы выиграли!")
        return 1
    if player_score < dealer_score:
        print("Вы проиграли.")
        return -1
    print("Ничья.")
    return 0

def main():
    balance = 100
    print("Добро пожаловать в игру Blackjack!")
    while True:
        print(f"Ваш баланс: {balance}")
        bet = 0
        while True:
            try:
                bet = int(input("Укажите ставку за раунд (или введите 0, чтобы выйти): ").strip())
                if bet < 0:
                    print("Ставка не может быть отрицательной.")
                elif bet == 0:
                    print("Выход из игры.")
                    return
                elif bet > balance:
                    print("Ставка не может превышать ваш баланс.")
                else:
                    break
            except ValueError:
                print("Пожалуйста, введите число.")
        result = play_round(balance)
        if result == 1:
            balance += bet
        elif result == -1:
            balance -= bet
        
        if balance <= 0:
            print("У вас больше нет денег. Игра окончена.")
            break
        again = input("Хотите сыграть ещё раз? (да/нет): ").strip().lower()
        if again not in ('да', 'yes', 'y'):
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
# Black Jack