first_number = int(input("Введи первое число: "))
user_actions = input("Какое действие сделать: ")
second_number = int(input("Введи второе число: "))
if user_actions == "-":
    print(first_number - second_number)
elif user_actions == "+":
    print(first_number + second_number)
elif user_actions == "*":
    print(first_number * second_number)
elif user_actions == "/":
    print(first_number / second_number)
elif user_actions == "%":
    print(first_number % second_number)
elif user_actions == "**":
    print(first_number ** second_number)
elif user_actions == "//":
    print(first_number // second_number)