# Это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
print('Я должен сделать', len(shoplist), 'покупки.')
"""Переменная shoplist – это список покупок человека, идущего на рынок. В
shoplist мы храним только строки с названиями того, что нужно купить,
однако в список можно добавлять любые объекты, включая числа или даже
другие списки."""

print('Покупки:', end=' ')
for item in shoplist:
    print(item, end=' ')
"""Мы также использовали цикл for..in для итерации по элементам списка.
Вы уже, наверное, поняли, что список является также и последовательностью.
Использование ключевого аргумента end в функции
print, который показывает, что мы хотим закончить вывод пробелом вместо
обычного перевода строки."""

print('\nТакже нужно купить риса.')
shoplist.append('рис')
print('Теперь мой список покупок таков:', shoplist)
"""Далее мы добавляем элемент к списку при помощи append"""

print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)
"""Затем мы сортируем список, используя метод sort объекта списка"""

print('Первое, что мне нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил', olditem)
print('Теперь мой список покупок:', shoplist)
