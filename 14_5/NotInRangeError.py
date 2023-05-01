class NotInRangeError(Exception):
    def __init__(self, message=None):
        super().__init__(message)


def verbose_grade(grade_int):
    if grade_int == 2:
        return "Плохо"
    elif grade_int == 3:
        return "Плохо"
    elif grade_int == 4:
        return "Хорошо"
    elif grade_int == 5:
        return "Отлично"

    raise NotInRangeError("Value from 2 to 5 expected")


# И сразу же вызовем с неверными данными

try:
    verbose_grade(1)
except NotInRangeError:
    print("Значение вне диапазона разрешенных значений")

# Выведет

# Значение вне диапазона разрешенных значений