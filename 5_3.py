N = int(input("Введи число: "))
first_number = 2
end_count = 0
for first_number in range(2, N + 1):
    if first_number % 2 == 0:
        result = first_number
        print(f"Ваше четное число : {result}", end=". ")
        first_number += 1
        end_count += 1
        if end_count == 5:
            print("\n")
            end_count = 0
    else:
        first_number += 1