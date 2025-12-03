mylist = ["apple", "banana", "fig", "date", "grape", "kiwi"]

if not mylist:
    print("Список пуст.")
else:
    min_len = min(len(w) for w in mylist)
    max_len = max(len(w) for w in mylist)

    shortest = [w for w in mylist if len(w) == min_len]
    longest  = [w for w in mylist if len(w) == max_len]

    print("Короткие слова (длина {}): {}".format(min_len, shortest))
    print("Длинные слова (длина {}): {}".format(max_len, longest))



