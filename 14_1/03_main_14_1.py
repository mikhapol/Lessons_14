class MyOpen:
    def __init__(self, filename, mode, encoding='utf-8'):
        self.__filename = filename
        self.__mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.__fp = open(self.__filename, self.__mode, encoding=self.encoding)
        return self.__fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__fp.close()


with MyOpen('hello.txt', 'r', encoding='utf-8') as fp:
    print(fp.read())