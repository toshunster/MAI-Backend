# Домашнее задание №1

## Завести репозиторий на github, установить Python (>=3.6) (2 балла)
## Создать виртуальное окружение для Python и установить Django (2.2.5) (1 балл)
## Описать зависимости в requirements.txt (1 балл)
## Создать правильный .gitignore файл и  оформить изменения в виде отдельных осмысленных коммитов (1 балл)
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
