#Рехэширование с помощью псевдослучайных чисел

import random
import time

class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def rehash(self, key):
        return (self.hash_function(key) + random.randint(1,Size)) % self.size

    def put(self, key, value):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return

            index = self.rehash(key)

        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]

            index = self.rehash(key)

        return 'Значение не найдено'



Size = int(input("Введите размер хэш таблицы: "))
h_table = HashTable(Size) # Создание таблицы
# Бесконечный цикл для обработки команд пользователя
while True:
    command = input("Введите команду (put/get/show/exit): ")

    if command == 'put': # Добавление элемента
        keyP = int(input("Введите ключ: "))
        dataP = input("Введите значение: ")
        h_table.put(keyP, dataP)
    elif command == 'get': # Поиск элемента
        keyG = int(input("Введите ключ для поиска: "))
        start_time = time.time()
        print(h_table.get(keyG))
        print("--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
    elif command == 'show': # Отображение хэш таблицы
        result = [(h_table.keys[i], h_table.values[i]) for i in range(Size)]
        print(result)
    elif command == 'exit': # Завершение программы
        break
    else:
        print("Неверная команда. Попробуйте снова.")