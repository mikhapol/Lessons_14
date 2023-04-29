# Задача 1
# Создайте класс TodoList, который хранит ваши задачи.
# Реализуйте магические методы, которые позволят добиться следующего поведения:

# Задача 2
# Продолжение задачи 1
# Реализуйте магический метод, который позволит складывать два списка задач (экземпляра класса TodoList)
# и получать новый список, содержащий задачи обоих складываемых списков:

# Продолжение задачи 2
# Дополните класс TodoList, чтобы выполнялось следующее поведение:

class TodoList:
    def __init__(self, tasks):
        self.tasks = tasks

    def __repr__(self):
        return f'self.tasks = {self.tasks}'

    def __str__(self):
        return ' + '.join(self.tasks)

    def __add__(self, other):
        return TodoList(self.tasks + other.tasks)

    def __len__(self):
        return len(self.tasks)


tasks = ['task1', 'task2']
list1 = TodoList(tasks)
print(repr(list1))
TodoList(list[str])
print(list1)
# task1
# task2
print('~~~~~~~')
list2 = TodoList(['task3', 'task4'])
list3 = list1 + list2
print(list3)
# task1
# task2
# task3
# task4
print('~~~~~~~')
print(len(list3))
# 4