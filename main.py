"""
Как создать класс:

class Имя_класса:
    ...

"""

# import time

#
# class Computer:
#
#     def __init__(self, name):  # Конструктор обьекта Computer
#         self.bot = lambda x: x + 1
#         self.start_time = time.time()
#         self.name = self._format_name(name)
#         self.ram = 0
#         print(f'{self.name} Запущен')
#
#     def __del__(self):  # Деструктор обьекта Computer
#         print(f'{self.name} Выключен')
#
#     def set_ram(self, gb_ram):
#         self.ram = gb_ram
#
#     def get_ram(self):
#         return self.ram
#
#     def _format_name(self, name):
#         return f'Имя: {name}'
#
#     def get_name(self):
#         return self.name
#
#     def get_run_time(self):
#         return time.time() - self.start_time
#
#
# computer = Computer('Это компьютер 1')
# print(computer.get_name())

"""
Задание #1: Создайте структуру с именем student, содержащую поля: фамилия и инициалы, номер группы, успеваемость (массив из пяти элементов). Создать массив из десяти элементов такого типа, упорядочить записи по возрастанию среднего балла. Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.
Задание #2: Создайте структуру с именем train, содержащую поля: название пункта назначения, номер поезда, время отправления. Ввести данные в массив из пяти элементов типа train, упорядочить элементы по номерам поездов. Добавить возможность вывода информации о поезде, номер которого введен пользователем. Добавить возможность сортировки массив по пункту назначения, причем поезда с одинаковыми пунктами назначения должны быть упорядочены по времени отправления.
Задание #3:
Создайте класс Грузовик
У которого есть параметры Марка, год производства, максимальная скорость и кол-во км сколько ему нужно проехать
Класс должен уметь:
 - получать марку, год производства грузовика
 - получать за какое время грузовик проедет заданное количество км
"""

# def running_time(func):
#     def wrapper(n):
#         start = time.time()
#         return_value = func(n)
#         print(f'{func} отработала за {time.time() - start}s')
#         return return_value
#     return wrapper
#
#
# @running_time
# def sum(n):
#     sum_value = 0
#     for i in range(1, n + 1):
#         sum_value += i
#     return sum_value
#
#
# @running_time
# def multiply(n):
#     sum_value = 1
#     for i in range(1, n + 1):
#         sum_value *= i
#     return sum_value
#
#
# print(type(sum))
# sum(10000000)
# multiply(1000)
#
# import time


"""
декоратор property используется в качестве setter и getter.

Пример:

class Student:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value.title()
        else:
            raise ValueError('Name это не строка')
"""


class Student:

    def __init__(self, name, mark, email):
        self.name = name
        self.mark = mark
        self.email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if isinstance(value, str) and value.find('@') != -1 and value.find('.') != -1:
            self._email = value
        else:
            raise ValueError('В почте нет символов "@" и "." или email это не строка')

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        if isinstance(value, int) and 1 <= value <= 12:
            self._mark = value
        else:
            raise ValueError('Mark должен быть от 1 до 12 и тип данных int')

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value.title()
        else:
            raise ValueError('Name это не строка')


student = Student('вася', 10, 'admin@admin.com')
print(student.email)
student.email = 'vasya@student.com'
student.name = 'петя'
print(student.name)
# student.email = 'vasyastudent.com'
# print(student.get_email())

"""
Нужно создать класс User
В котором будут следующие свойства:
 - name, нужно проверить, что передаваемый аргумент - строка и сделать имя с заглавной буквы
 - email, нужно проверить, что передаваемый аргумент - строка и в почте есть символ "@" и "."
 - password, нужно проверить, что передаваемый аргумент - строка, а так-же, что длина пароля больше 8 символов и в нем есть хотя бы одно число, большая и маленькая буква
 - confirm_password, нужно проверить, что передаваемый аргумент - строка, а так-же, что поле совпадает с свойством password
В случае, если хотя бы одно поле не соответствует валидации, то выбросить ошибку ValueError с описанием проблемы.
Все setter и getter свойств должны быть реализованы через @property

После создания класса, необходимо сделать простой интерфейс для просмотра, добавления, редактирования и удаления пользователей.
"""
