class EvenRange:
    def __init__(self, max_num):
        self.__max_num = max_num
        self.__step = 2
        self.__start = 0

    def __iter__(self):
        self.__current_value = self.__start - self.__step
        return self

    def __next__(self):
        self.__current_value += 2

        if self.__current_value < self.__max_num:
            return self.__current_value

        raise StopIteration


it = iter(EvenRange(10))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print('--------')
# for i in EvenRange(10):
#     print(i)
# print('--------')
# for i in range(3):
#     print(i)
# print('--------')
# it = iter(range(4))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
