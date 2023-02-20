# Домашнее задание №1

## Завести репозиторий на github, установить Python (>=3.6) (2 балла)
Шаблон имени:
* YYYY-MAI-Backend-N-LAST\_NAME
* YYYY — текущий год
* N — первая буква имени
* LAST\_NAME — фамилия
**Пример**: 2023-MAI-Backend-A-Kukhtichev

## Создать виртуальное окружение для Python и установить Django==X, где X >= 3 (1 балл)
## Описать зависимости в requirements.txt (1 балл)
## Создать правильный .gitignore файл и оформить изменения в виде отдельных осмысленных коммитов (1 балл)
Коммитить папку с виртуальным окружением (venv) не нужно!!!

## Написать реализацию LRU-cache на языке Python (5 баллов)
Класс должен содержать следующие методы
```python
class LRUCache:
    def __init__(self, capacity: int=10) -> None:
        pass

    def get(self, key: str) -> str:
        pass

    def set(self, key: str, value: str) -> None:
        pass

    def rem(self, key: str) -> None:
        pass
```
Все операции должны работать за O(1). Начиная с Python==3.6, объекты dict теперь сохраняют свои элементы в том же порядке, в котором они были представлены.

Проверяться работоспособность должна так:
```python
from cache import LRUCache

cache = LRUCache(100)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
cache.get('Jesse') # вернёт 'James'
cache.rem('Walter')
cache.get('Walter') # вернёт ''
```
