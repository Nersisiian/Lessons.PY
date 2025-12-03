def multiplication_table(n=10):
    for i in range(1, n + 1):
        line = []
        for j in range(1, n + 1):
            line.append(str(i * j).rjust(4))  
        print("".join(line))

def main():
    try:
        user_input = input("Enter table size (default 10): ").strip()
        if user_input:
            n = int(user_input)
        else:
            n = 10
    except ValueError:
        print("Invalid input. Using default size 10.")
        n = 10

    multiplication_table(n)

if __name__ == "__main__":
    main()