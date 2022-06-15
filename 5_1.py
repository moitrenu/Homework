N = int(input("Введи число: "))
M = int(input("Введи число: "))
K = int(input("Введи число: "))
counter = 0
while counter < 5:
    if N % M == 0 and N / M > K:
        positive = N
        print(positive)
        counter += 1
        N += 1
    else:
        N += 1