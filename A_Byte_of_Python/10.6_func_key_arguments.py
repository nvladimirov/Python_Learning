def func(a, b=5, c=10):
    print('a равно', a, ', b равно', b, ', а c равно', c)


func(1)
func(3, 7)
func(25, c=24)
func(c=50, a=100)
"""Функция с именем func имеет один параметр без значения по умолчанию, за которым следуют два параметра со 
значениями по умолчанию. При первом вызове, func(3, 7), параметр a получает значение 3, параметр b получает значение 
7, а c получает своё значение по умолчанию, равное 10. При втором вызове func(25, c=24) переменная a получает 
значение 25 в силу позиции аргумента. После этого параметр c получает значение 24 по имени, т.е. как ключевой 
параметр. Переменная b получает значение по умолчанию, равное 5. При третьем обращении func(c=50, a=100) мы 
используем ключевые аргументы для всех указанных значений. Обратите внимание на то, что мы указываем значение для 
параметра c перед значением для a, даже несмотря на то, что в определении функции параметр a указан раньше c. """
