def my_max(items):
    current_max = items[0]

    for index in range(1, len(items)):
        item = items[index]
        if item > current_max:
            current_max = item

    return current_max


the_max = my_max([99, 1, 0, -99, -1])
print(the_max)
