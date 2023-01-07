import my_modules_a
my_modules_a.sayhi()
print('Версия', my_modules_a.__version__)

from my_modules_a import sayhi, __version__
sayhi()
print('Версия', __version__)
"""Два варианта импорта"""
