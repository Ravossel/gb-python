# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять
# из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def count_vowels(word):
    vowels = 'аеёиоуыэюя'
    return sum(1 for letter in word if letter in vowels)

def check_rhythm(pooh_poem):
    phrases = pooh_poem.split()
    previous_vowel_count = None

    for phrase in phrases:
        words = phrase.split('-')
        phrase_vowel_count = sum(count_vowels(word) for word in words)

        if previous_vowel_count is not None and phrase_vowel_count != previous_vowel_count:
            return "Пам парам"
        
        previous_vowel_count = phrase_vowel_count

    return "Парам пам-пам"

pooh_poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(pooh_poem)
print(result)
