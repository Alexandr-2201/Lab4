import random
import time

# Генерация начального набора случайных данных
data = [random.randint(1, 20000) for _ in range(8000)]
#data.sort()
print("Начальный набор данных:", sorted(data))


# Функция для добавления элемента
def add_element(element):
    data.append(element)
    #data.sort()
    print(f"Элемент {element} добавлен. Новый набор данных:", sorted(data))


# Функция для удаления элемента
def remove_element(element):
    if element in data:
        data.remove(element)
        print(f"Элемент {element} удален. Новый набор данных:", sorted(data))
    else:
        print(f"Элемент {element} не найден в наборе данных.")

# Функция бинарного поиска
def binary_search(element):
    data1 = sorted(data)
    left, right = 0, len(data1) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if data1[mid] == element:
            return print(f"Элемент {element} найден в позиции {mid}.")
        elif data1[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return print(f"Элемент {element} не найден в массиве.")


# Функция поиска бинарного дерева
class BTree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return BTree(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def tree_search(root, key):
    if root is None or root.val == key:
        return root
    if root.val < key:
        return tree_search(root.right, key)
    return tree_search(root.left, key)

# Создание бинарного дерева поиска из массива data
def create_binary_search_tree():
    root = None
    for val in data:
        root = insert(root, val)
    return root

# Функция Фибоначчиевого поиска
def fibonacci_search(element):
    data1 = sorted(data)
    n = len(data1)
    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        if data1[i] < element:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif data1[i] > element:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return print(f"Элемент {element} найден в позиции {i}.")
    if fib1 and data1[offset + 1] == element:
        return offset + 1
    return print(f"Элемент {element} не найден в массиве.")


# Функция интерполяционного поиска
def interpolation_search(element):
    data1 = sorted(data)
    low = 0
    high = len(data1) - 1
    while low <= high and element >= data1[low] and element <= data1[high]:
        pos = low + ((element - data1[low]) * (high - low)) // (data1[high] - data1[low])
        if data1[pos] == element:
            return print(f"Элемент {element} найден в позиции {pos}.")
        elif data1[pos] < element:
            low = pos + 1
        else:
            high = pos - 1
    return print(f"Элемент {element} не найден в массиве.")



# Бесконечный цикл для обработки команд пользователя
while True:
    command = input("Введите команду (add/remove/find/exit): ")

    if command == 'add': # Добавление элемента
        element = int(input("Введите элемент для добавления: "))
        add_element(element)
    elif command == 'remove': # Удаление элемента
        element = int(input("Введите элемент для удаления: "))
        remove_element(element)
    elif command == 'find': # Поиск элемента
        command_find = input("Введите номер функции поиска (Бинарный поиск (1) /Бинарное дерево (2) /Фибоначчиев (3) /Интерполяционный (4) / Стандартный (5)): ")
        if command_find == '1':
            element = int(input("Введите элемент для поиска: "))
            start_time = time.time()
            binary_search(element)
            print("--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
        elif command_find == '2':
            element = int(input("Введите элемент для поиска: "))
            start_time = time.time()
            root = create_binary_search_tree() # Создание бинарного дерева
            result = tree_search(root, element)
            if result:
                print(f"Элемент {element} найден в бинарном дереве поиска.")
            else:
                print(f"Элемент {element} не найден в бинарном дереве поиска.")
            print("--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
        elif command_find == '3':
            element = int(input("Введите элемент для поиска: "))
            start_time = time.time()
            fibonacci_search(element)
            print("--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
        elif command_find == '4':
            element = int(input("Введите элемент для поиска: "))
            start_time = time.time()
            interpolation_search(element)
            print("--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
        elif command_find == '5':
            element = int(input("Введите элемент для поиска: "))
            start_time = time.time()
            if element in data:
                Index = sorted(data).index(element)
                print(f"Элемент {element} найден в позиции {Index}.")
            else:
                print(f"Элемент {element} не найден в массиве.")
            print("--- {0} ms ---".format(round((time.time() - start_time) * 1000)))
        else:
            print("Неверная функция поиска. Попробуйте снова.")

    elif command == 'exit': # Завершение программы
        break
    else:
        print("Неверная команда. Попробуйте снова.")

