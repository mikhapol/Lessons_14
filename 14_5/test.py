def verbose_month(month_number):
    months = [
        'January - Январь',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December',
    ]

    if month_number < 1 or month_number > 12:
        raise ValueError("1 to 12 Expected")
    return months[month_number - 1]


print(verbose_month(1))
print(verbose_month(2))
print(verbose_month(3))
print(verbose_month(4))
print(verbose_month(5))
print(verbose_month(6))
