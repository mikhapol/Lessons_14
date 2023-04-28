import datetime


class Employee:  # Класс Работник
    raise_coef = 1.5

    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.__pay = pay

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.surname}, {self.pay})'

    def __str__(self):
        return f'{self.fullname} ({self.pay})'

    def __len__(self):
        return len(self.fullname)

    def __add__(self, other):
        return self.pay + other.pay

    def raise_pay(self):
        self.__pay *= self.raise_coef

    @property
    def email(self):
        return f'{self.name.lower()}.{self.surname.lower()}@pochta.ru'

    @property
    def pay(self):
        return self.__pay

    @property  # get
    def fullname(self):
        return f'{self.name.title()} {self.surname.title()}'

    @fullname.setter  # set
    def fullname(self, fio_string):
        name, surname = fio_string.split('/')
        self.name = name.title()
        self.surname = surname.title()


if __name__ == '__main__':
    emp1 = Employee('Иван', 'Иванов', 60000)
    emp2 = Employee('Михаил', 'Михайлов', 105000)
    emp3 = Employee('Анастасия', 'Анастасьева', 100000)
    print('---------')
    print(repr(emp1), repr(emp2), repr(emp3))
    print('---------')
    print(emp1, emp2, emp3)
    print('---------')
    print(len(emp1), len(emp2), len(emp3))
    print('---------')
    result = emp1 + emp2
    result = emp2 + emp3
    print(result)
