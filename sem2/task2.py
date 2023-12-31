# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# две подсказки: сумма S и произведение P.
S = int(input("Введите сумму S: "))
P = int(input("Введите произведение P: "))

# переберем все возможные значения X и Y.
for X in range(1, 1001):  # Мы знаем, что X и Y ≤ 1000.
    Y = S - X  # Вычислим Y, зная X и S.

    # проверим, что X и Y - натуральные числа и их произведение равно P.
    if Y > 0 and X * Y == P:
        print("Петя загадал числа X и Y:")
        print("X =", X)
        print("Y =", Y)
        break
else:
    print("Кажется, я не могу найти подходящие числа X и Y.")
