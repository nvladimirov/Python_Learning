def total(a=5, *numbers, **phonebook):
    print('a', a)
    # проход по всем элементам кортежа
    for single_item in numbers:
        print('single_item', single_item)
    # проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
"""Когда мы объявляем параметр со звёздочкой (например, *param), все позиционные аргументы начиная с этой позиции и 
до конца будут собраны в кортеж под именем param. Аналогично, когда мы объявляем параметры с двумя звёздочками (
**param), все ключевые аргументы начиная с этой позиции и до конца будут собраны в словарь под именем param. """
