# user_word = input("Введи слово: ")
# user_word = user_word.lower().replace(" ","")
# if user_word == user_word[::-1]:
#     print("Палиндром")
# else:
#     print("Не палиндром")


text = input("Введи текст: ")
vowels_count = 0
consonants_count = 0
vowels = 'eyuiojуеаоэяи'
for symbol in text:
    if symbol.isalpha():
        if symbol in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
print(vowels_count)
print(consonants_count)
