# Создайте класс TodoList , который хранит ваши задачи.
# Реализуйте магические методы, которые позволят добиться следующего поведения:

# Реализуйте магический метод, который позволит складывать два списка задач (экземпляра класса TodoList )
# и получать новый список, содержащий задачи обеих складываемых списков:

# Дополните класс TodoList, чтобы выполнялось следующее поведение:

class TodoList:
    def __init__(self, tasks: list[str]) -> None:
        self.tasks = tasks

    def __repr__(self) -> str:
        return f'self.tasks = {self.tasks} == {__class__.__name__}'

    def __str__(self) -> str:
        return '\n'.join(self.tasks)

    def __add__(self, other: 'TodoList') -> 'TodoList':
        # return [*self.tasks, *other.tasks]
        return TodoList(self.tasks + other.tasks)

    def __len__(self) -> int:
        return len(self.tasks)


tasks = ['task1', 'task2']
list1 = TodoList(tasks)
print(repr(list1))
TodoList(list[str])
print(list1)
print('--------')
list2 = TodoList(['task3', 'task4'])
list3 = list1 + list2
print(list3)
print('--------')
print(len(list3))
