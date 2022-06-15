N = int(input("На сколько элементов надо сдвинуть?: "))
spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = (len(spisok))
for i in range(N):
    temp = spisok[i]
    spisok[i] = spisok[a - N + i]
    spisok[a - N + i] = temp
for i in range(N, a - 1):
    for j in range(N, a - i - 1):
        if spisok[j] > spisok[j + 1]:
            temp = spisok[j]
            spisok[j] = spisok[j + 1]
            spisok[j + 1] = temp
print(spisok)