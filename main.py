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

# import time
#
#
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

# class Student:
#
#     def __init__(self, name, mark, email):
#         self.name = name
#         self.mark = mark
#         self.email = email
#
#     @property
#     def email(self):
#         return self._email
#
#     @email.setter
#     def email(self, value):
#         if isinstance(value, str) and value.find('@') != -1 and value.find('.') != -1:
#             self._email = value
#         else:
#             raise ValueError('В почте нет символов "@" и "." или email это не строка')
#
#     @property
#     def mark(self):
#         return self._mark
#
#     @mark.setter
#     def mark(self, value):
#         if isinstance(value, int) and 1 <= value <= 12:
#             self._mark = value
#         else:
#             raise ValueError('Mark должен быть от 1 до 12 и тип данных int')
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if isinstance(value, str):
#             self._name = value.title()
#         else:
#             raise ValueError('Name это не строка')
#
#
# student = Student('вася', 10, 'admin@admin.com')
# print(student.email)
# student.email = 'vasya@student.com'
# student.name = 'петя'
# print(student.name)
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

# class User:
#
#     def __init__(self, name, email, password, confirm_password):
#         self.name = name
#         self.email = email
#         self.password = password
#         self.confirm_password = confirm_password
#
#     @property
#     def email(self):
#         return self._email
#
#     @email.setter
#     def email(self, value):
#         if isinstance(value, str) and value.find('@') != -1 and value.find('.') != -1:
#             self._email = value
#         else:
#             raise ValueError('В почте нет символов "@" и "." или email это не строка')
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         if isinstance(value, str):
#             self._name = value.title()
#         else:
#             raise ValueError('Name это не строка')
#
#     def check_password(self, confirm_password):
#         if self.password == confirm_password:
#             return True
#         else:
#             return False
#
#     @property
#     def password(self):
#         return self._password
#
#     @password.setter
#     def password(self, value):
#         if isinstance(value, str):
#             has_len = len(value) > 8
#             has_digit = any([True for x in value if x.isdigit()])
#             has_upper = any([True for x in value if x.isupper()])
#             has_lower = any([True for x in value if x.islower()])
#             if all([has_len, has_lower, has_upper, has_digit]):
#                 self._password = value
#             else:
#                 raise ValueError(
#                     'Не соответствует длина пароля больше 8 символов и в нем есть хотя бы одно число, большая и маленькая буква')
#         else:
#             raise ValueError('Валидация пароля не пройдена!')
#
#     @property
#     def confirm_password(self):
#         return self._confirm_password
#
#     @confirm_password.setter
#     def confirm_password(self, value):
#         if isinstance(value, str) and value == self.password:
#             self._confirm_password = value
#         else:
#             raise ValueError('Валидация пароля не пройдена!')
#
#     def __str__(self):
#         return self.name
#
#
# class UserDatabase:
#
#     def __init__(self):
#         self.users = []
#
#     def add_user(self, name, email, password, confirm_password):
#         try:
#             user = User(name, email, password, confirm_password)
#         except ValueError as e:
#             print(e)
#             return False
#         self.users.append(user)
#         return True
#
#     def get_user(self, name):
#         for idx, user in enumerate(self.users):
#             if user.name == name:
#                 return idx
#         return None
#
#     def edit_user(self, find_name, name, email, password, confirm_password):
#         user_idx = self.get_user(find_name)
#         if user_idx is None:
#             print('User not found')
#             return False
#         user = self.users[user_idx]
#         user.name = name
#         user.email = email
#         user.password = password
#         user.confirm_password = confirm_password
#         return True
#
#     def get_users(self):
#         return '\n'.join([f'{x.name}\n' \
#                           f'{x.email}\n' \
#                           f'{x.password}\n' \
#                           f'{x.confirm_password}\n'
#                           for x in self.users])
#
#     def delete_user(self, name):
#         user_idx = self.get_user(name)
#         if user_idx is None:
#             print('User not found')
#             return False
#         self.users.pop(user_idx)
#         return True
#
#     def __len__(self):
#         return len(self.users)
#
#     def __eq__(self, other):
#         return len(self) == len(other)
#
#     def __ne__(self, other):
#         return len(self) != len(other)
#
#     def __lt__(self, other):
#         return len(self) < len(other)
#
#     def __gt__(self, other):
#         return len(self) > len(other)
#
#     def __ge__(self, other):
#         return len(self) >= len(other)
#
#     def __le__(self, other):
#         return len(self) <= len(other)
#
#     def __add__(self, other):
#         tmp_db = UserDatabase()
#         if isinstance(other, UserDatabase):
#             tmp_db.users = self.users + other.users
#         elif isinstance(other, User):
#             tmp_db.users = self.users
#             tmp_db.users.append(other)
#         return tmp_db
#
#     def __str__(self):
#         return str([str(x) for x in self.users])

#
# """
# Магические методы в Python:
#  - __len__(self) - возвращает длину
#  - __eq__(self, other) - Определяет поведения оператора сравнения ==
#  - __ne__(self, other) - Определяет поведения оператора не равно !=
#  - __lt__(self, other) - Определяет поведения оператора <
#  - __gt__(self, other) - Определяет поведения оператора >
#  - __ge__(self, other) - Определяет поведения оператора >=
#  - __le__(self, other) - Определяет поведения оператора <=
# """
#
# user_db_1 = UserDatabase()
# user_db_1.add_user('petya', 'admin@admin.com', 'PaS$13123', 'PaS$13123')
# user_db_1.add_user('petya1', 'admin@admin.com', 'PaS$13123', 'PaS$13123')
# user_db_1.add_user('petya2', 'admin@admin.com', 'PaS$13123', 'PaS$13123')
# user_db_1.add_user('petya3', 'admin@admin.com', 'PaS$13123', 'PaS$13123')
#
# user_db_2 = UserDatabase()
# user_db_2.add_user('petya4', 'admin@admin.com', 'PaS$13123', 'PaS$13123')
# user_db_2.add_user('petya15', 'admin@admin.com', 'PaS$13123', 'PaS$13123')
# user_db_2.add_user('petya26', 'admin@admin.com', 'PaS$13123', 'PaS$13123')
#
# new_db = user_db_1 + User('asd', 'asd@ad.com', 'PaS$13123', 'PaS$13123')
# print(new_db)


# class Car:
#
#     def get_color(self):
#         pass
#
#     def acceleration_to_100(self):
#         pass
#
#     def get_car_brand(self):
#         pass
#
#
# class M5(Car):
#     COLORS = ['Blue', 'Green', 'White', 'Black']
#
#     def __init__(self, color='Blue', max_speed=200, brand='BMW'):
#         self._brand = brand
#         self.color = color
#         self._max_speed = max_speed
#
#     def get_color(self):
#         return self._color
#
#     def acceleration_to_100(self):
#         return self._max_speed / 100
#
#     def get_car_brand(self):
#         return self._brand
#
#     @property
#     def color(self):
#         return self._color
#
#     @color.setter
#     def color(self, value):
#         if value in self.COLORS:
#             self._color = f'{self.get_car_brand()}: {value}'
#         else:
#             raise ValueError(f'{value} not in {self.COLORS}')
#
#     def __str__(self):
#         return f'<{self.color} | {self._brand} | {self._max_speed} | id: {id(self)}>'
#
#
# class M6(M5):
#     def __init__(self, color='Blue', max_speed=350, brand='BMW'):
#         super(M6, self).__init__(color, max_speed, brand)
#
#     def acceleration_to_100(self):
#         return self._max_speed / 200
#
#
# class Passat(Car):
#     def __init__(self, max_speed=250):
#         self._max_speed = max_speed
#
#     def get_color(self):
#         return 'Blue'
#
#     def acceleration_to_100(self):
#         return self._max_speed
#
#     def get_car_brand(self):
#         return 'VW'
#
#
# def print_car_max_speed(obj):
#     print(obj.acceleration_to_100())
#
#
# car_6 = M6(max_speed=500, color='Green')
# car_5 = M5()
# car_1 = Passat()
# print_car_max_speed(car_6)
# print_car_max_speed(car_5)
# print_car_max_speed(car_1)

"""
Интерфейс - это абстрактный класс, у которого не реализованы все методы.
Абстрактный класс - класс у которого не реализован один или больше методов.
Родитель - это класс от которого наследуются другие классы
Дочерний класс - это класс который наследуется от родителя
Принципы ООП:
 1) Абстракция - выделение значемых свойств обьекта, исключает при этом незначемые. Простыми словами - обобщаем свойства обьекта.
 2) Наследование - это свойство системы, позволяющее описать новый класс на основе уже существующего с
  частичной или полностью заимствующейся функциональностью.
 3) Инкапсуляция - это свойство системы, которое позволяет обьеденить данные и методы,
  работающие с ними, в классе и скрыть детали реализации от пользователя.
 4) Полиморфизм - это свойство системы использовать обьекты с одинаковым
  интерфейсом без информации о типе и внутренней структуре обьекта.
"""


# Интерфейс машины
class Car:

    def get_color(self):
        pass

    def get_price(self):
        pass

    def brand(self):
        pass


# Абстрактный класс марки машины
class BMW(Car):

    def brand(self):
        return 'BMW'

    def has_spoiler(self):
        pass


class Porshe(Car):

    def is_sportcar(self):
        pass

    def brand(self):
        return 'Porshe'


class Lada(Car):

    def brand(self):
        return 'Lada'


class Vesta(Lada):

    def __init__(self, color, price_usd):
        self._color = color
        self.price = price_usd

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value * 28

    def get_color(self):
        return self._color

    def get_price(self):
        return self.price


class Cayenee(Porshe):

    def __init__(self, color, price_usd, max_speed=None):
        self._color = color
        self.price = price_usd
        self._max_speed = max_speed

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value * 28

    def get_color(self):
        return self._color

    def get_price(self):
        return self.price

    def is_sportcar(self):
        return True if self._max_speed > 500 else False


class X5(BMW):

    def __init__(self, color, price_usd):
        self._color = color
        self.price = price_usd

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value * 28

    def get_color(self):
        return self._color

    def get_price(self):
        return self.price

    def has_spoiler(self):
        return True if self.price > 500000 else False


def get_car_info():
    color = input('Введите цвет: ')
    price = int(input('Введите цену: '))
    return color, price


def sum_car_price(cars):
    sum_price = 0
    for car in cars:
        sum_price += car.get_price()
    return sum_price


if __name__ == '__main__':
    cars = []
    menu = 'Выберите марку:\n' \
           '1 - BMW\n' \
           '2 - Porshe\n' \
           '3 - Lada\n -> '
    for i in range(10):
        choice = int(input(menu))
        color, price = get_car_info()
        if choice == 1:
            cars.append(X5(color=color, price_usd=price))
        elif choice == 2:
            cars.append(Cayenee(color=color, price_usd=price))
        elif choice == 3:
            cars.append(Vesta(color=color, price_usd=price))
        else:
            exit()
