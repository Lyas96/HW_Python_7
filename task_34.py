# Задача 34: Напишите программу.
# Ритм есть, если число гласных букв в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

#**Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
# **Вывод:** Парам пам-пам



def para_pa_pa(words):
  list_1 = []
  for i in words:
    sum = 0
    for j in i:
        if j in 'аеёиоуыэюя':
            sum += 1
    list_1.append(sum)
  return len(list_1) == list_1.count(list_1[0])

words = input('Введите слова стихотворения через пробел: ').split()

if para_pa_pa(words):
    print('Парам пам-пам')
else:
    print('Пам парам')

