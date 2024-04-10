#Метод цепочек

import time


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Создаем список списков для хранения элементов

    def hash_function(self, key):
        return key % self.size  # Простая хеш-функция для вычисления индекса в таблице

    def put(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))  # Добавляем элемент в список

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Ищем элемент по ключу и возвращаем его значение, если найден
        return 'Значение не найдено'  # Если не найден


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
        #result = [(h_table.keys[i], h_table.values[i]) for i in range(Size)]
        print(h_table.table)
    elif command == 'exit': # Завершение программы
        break
    else:
        print("Неверная команда. Попробуйте снова.")
