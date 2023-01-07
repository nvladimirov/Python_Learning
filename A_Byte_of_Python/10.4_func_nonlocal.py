def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        nonlocal x
        x = 4

    func_inner()
    print('Локальное x сменилось на', x)


func_outer()
"""Когда мы находимся внутри func_inner, переменная x, определённая в первой строке func_outer находится ни в 
локальной области видимости (определение переменной не входит в блок func_inner), ни в глобальной области видимости (
она также и не в основном блоке программы). Мы объявляем, что хотим использовать именно эту переменную x, 
следующим образом: nonlocal x. Попробуйте заменить «nonlocal x» на «global x», а затем удалить это зарезервированное 
слово, и пронаблюдайте за разницей между этими двумя случаями. """