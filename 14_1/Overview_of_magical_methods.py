# Ниже представлен класс, в котором реализованы основные магические методы.
# Этот класс создан для примера.
# В реальной разработке сложно встретит класс, который бы включал в себя все эти магические методы.
class BigFuncClass:

    def __init__(self, attr1, attr2):
        """
        Магический метод для инициализации объекта из класса: bfc1 = BigFuncClass('1', '2')
        """
        self.attr1 = attr1
        self.attr2 = attr2

    def __repr__(self):
        """
        Магический метод для отображения информации об объекте класса в режиме отладки (для разработчиков):
        repr(bfc1)
        """
        return f'{self.__class__.__name__}({self.attr1}, {self.attr2})'

    def __str__(self):
        """
        Магический метод для отображения информации об объекте класса для пользователей, например для функций
        print, str: print(bfc1)
        """
        return f'{self.attr1} - {self.attr2}'

    def __len__(self):
        """
        Магический метод, который позволяет применять функцию len() к экземплярам класса: len(bfc1)
        """
        return len(f'{self.attr1}{self.attr2}')

    def __add__(self, other):
        """
        Магический метод, который позволяет прибавлять к экземпляру класса объект произвольного типа: bfc1 + bfc2
        """
        self.attr1 += other.attr1
        self.attr2 += other.attr2

    def __call__(self, *args, **kwargs):
        """
        Магический метод, который позволяет экземпляр класса сделать callable-объектом,
        т. е. вызвать как обычную функцию для выполнения заложенной функциональности: bfc1()
        """
        print(f'Был вызван объект {self}')

    def __iter__(self):
        """
        Магический метод, который возвращает сам итератор для перебора объекта: for i in bfc1:
        """
        self.current_value = -1
        return self

    def __next__(self):
        """
        Магический метод, который позволяет переходить к следующему значению и его считывать: bfc1.next()
        """
        if self.current_value + 1 < len(self):
            self.current_value += 1
            return str(self)[self.current_value]
        else:
            raise StopIteration

    def __enter__(self):
        """
        Магический метод, который определяет, что должен сделать менеджер контекста в начале блока,
        созданного инструкцией with: with BigFuncClass('file.txt', 'r'):
        """
        self.fp = open(self.attr1, self.attr2)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Магический метод, который определяет действия менеджера контекста после того,
        как блок будет выполнен или прерван во время работы; отрабатывает автоматически.
        """
        self.fp.close()


bfc1 = BigFuncClass('1', '2')
bfc2 = BigFuncClass('3', '4')
