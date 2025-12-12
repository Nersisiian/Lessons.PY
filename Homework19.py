# # ------------------------------------------------------------------------------------------- No149

# # import sys
# # import os

# # def main():
    
# #     if len(sys.argv) != 2:
# #         print("Ошибка: необходимо указать имя файла в качестве аргумента.")
# #         print("Использование: python script.py имя_файла")
# #         return

# #     filename = sys.argv[1]

# #     if not os.path.isfile(filename):
# #         print(f"Ошибка: файл '{filename}' не существует.")
# #         return

# #     try:
# #         with open(filename, 'r', encoding='utf-8') as f:
# #             for i in range(10):
# #                 line = f.readline()
# #                 if not line:
# #                     break
# #                 print(line.rstrip('\n'))
# #     except Exception as e:
# #         print(f"Произошла ошибка при чтении файла: {e}")

# # if __name__ == "__main__":
# #     main()

# # try python script.py имя_файла -------------------------

# # ------------------------------------------------------------------------------------------- No150

# # import sys

# # def main():
# #     if len(sys.argv) != 2:
# #         print("Ошибка: укажите имя файла.")
# #         return
# #     filename = sys.argv[1]
# #     try:
# #         with open(filename, 'r', encoding='utf-8') as f:
# #             lines = f.readlines()
# #             for line in lines[-10:]:
# #                 print(line.rstrip())
# #     except FileNotFoundError:
# #         print(f"Ошибка: файл '{filename}' не найден.")
# # if __name__ == "__main__":
# #     main()

# # ------------------------------------------------------------------------------------------- No151

# # filename = input("Введите имя файла: ")
# # try:
# #     with open(filename, 'r', encoding='utf-8') as f:
# #         count = sum(1 for _ in f)
# #     print("Количество строк в файле:", count)
# # except FileNotFoundError:
# #     print("Файл не найден.")

# # ------------------------------------------------------------------------------------------- No152

# # filename = input("Введите имя файла: ")
# # try:
# #     with open(filename, 'r', encoding='utf-8') as f:
# #         for line in f:
# #             for word in line.split():
# #                 print(word)
# # except FileNotFoundError:
# #     print("Файл не найден.")

# # ------------------------------------------------------------------------------------------- No153

# filename = input("Введите имя файла: ")
# try:
#     with open(filename, 'r', encoding='utf-8') as f:
#         for i, line in enumerate(f, start=1):
#             print(f"{i:>4}: {line.rstrip()}")
# except FileNotFoundError:
#     print("Файл не найден.")


# filename = input("Введите имя файла: ")
# try:
#     with open(filename, 'r', encoding='utf-8') as f:
#         for line in f:
#             if not line.strip().startswith("#") and line.strip() != "":
#                 print(line.rstrip())
# except FileNotFoundError:
#     print("Файл не найден.")

# # ------------------------------------------------------------------------------------------- No154

# filename = input("Введите имя файла: ")
# try:
#     with open(filename, 'r', encoding='utf-8') as f:
#         for line in f:
#             if not line.strip().startswith("#") and line.strip() != "":
#                 print(line.rstrip())
# except FileNotFoundError:
#     print("Файл не найден.")

# # ------------------------------------------------------------------------------------------- No155

# filename = input("Введите имя файла: ")
# try:
#     with open(filename, 'r', encoding='utf-8') as f:
#         words = f.read().split()
#         if words:
#             longest = max(words, key=len)
#             print("Самое длинное слово:", longest)
# except FileNotFoundError:
#     print("Файл не найден.")

# # ------------------------------------------------------------------------------------------- No156

# file1 = input("Первый файл: ")
# file2 = input("Второй файл: ")
# output = input("Имя результирующего файла: ")

# try:
#     with open(output, 'w', encoding='utf-8') as out:
#         for name in [file1, file2]:
#             with open(name, 'r', encoding='utf-8') as f:
#                 out.write(f.read() + "\n")
#     print("Файлы объединены в", output)
# except FileNotFoundError:
#     print("Один из файлов не найден.")

# # ------------------------------------------------------------------------------------------- No157

# src = input("Исходный файл: ")
# dst = input("Результирующий файл: ")
# try:
#     with open(src, 'r', encoding='utf-8') as f, open(dst, 'w', encoding='utf-8') as out:
#         for line in f:
#             if line.strip():
#                 out.write(line)
#     print("Пустые строки удалены.")
# except FileNotFoundError:
#     print("Файл не найден.")

# # ------------------------------------------------------------------------------------------- No158

# file1 = input("Первый отсортированный файл: ")
# file2 = input("Второй отсортированный файл: ")
# output = input("Имя результирующего файла: ")

# try:
#     with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output, 'w', encoding='utf-8') as out:
#         list1 = [line.strip() for line in f1]
#         list2 = [line.strip() for line in f2]
#         merged = sorted(list1 + list2)
#         for item in merged:
#             out.write(item + "\n")
#     print("Файлы объединены и отсортированы в", output)
# except FileNotFoundError:
#     print("Файл не найден.")

# # ------------------------------------------------------------------------------------------- No159

# from collections import Counter

# filename = input("Введите имя файла: ")
# try:
#     with open(filename, 'r', encoding='utf-8') as f:
#         words = f.read().lower().split()
#         counts = Counter(words)
#     for word, freq in counts.most_common():
#         print(f"{word}: {freq}")
# except FileNotFoundError:
#     print("Файл не найден.")

# # ------------------------------------------------------------------------------------------- 


