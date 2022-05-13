sentence_user = str(input("Введите текст:"))
some_list = dict()
for char in set(sentence_user):
    some_list[char] = sentence_user.count(char)
print(some_list)