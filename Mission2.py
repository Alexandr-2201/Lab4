# Простое рехэширование

import time

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def rehash(self, old_hash, step_size=1):
        return (old_hash + step_size) % self.size

    def put(self, key, data):
        hash_value = self.hash_function(key)

        if self.slots[hash_value] is None:
            self.slots[hash_value] = (key, data)
        else:
            next_slot = self.rehash(hash_value)
            while self.slots[next_slot] is not None and self.slots[next_slot][0] != key:
                next_slot = self.rehash(next_slot)

            if self.slots[next_slot] is None:
                self.slots[next_slot] = (key, data)
            else:
                print("Hash table is full")

    def get(self, key):
        start_slot = self.hash_function(key)

        data = 'Значение не найдено'
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position][0] == key:
                found = True
                data = self.slots[position][1]
            else:
                position = self.rehash(position)
                if position == start_slot:
                    stop = True

        return data


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
        print(h_table.slots)
    elif command == 'exit': # Завершение программы
        break
    else:
        print("Неверная команда. Попробуйте снова.")
