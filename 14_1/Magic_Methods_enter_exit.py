class MyOpen:
    def __init__(self, filename, mode='r'):
        """
        Класс, который создает объект, который можно использовать
        вместо open(), чтобы автоматически закрывать файл.
        :param filename: имя файла
        :param mode: режим открытия файла (по умолчанию 'r')
        """
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        """
        Метод, который вызывается при входе в блок контекста.
        Он открывает файл и возвращает файловый дескриптор.
        :return: файловый дескриптор
        """
        self.fp = open(self.filename, self.mode)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Метод, который вызывается при выходе из блока контекста.
        Он закрывает файл.
        """
        self.fp.close()


with MyOpen('hello.txt', 'r') as fp:  # Открываем файл
    print(fp.read())  # Читаем файл
