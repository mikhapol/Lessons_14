class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"MyClass({self.value!r})"
        # return f"MyClass({self.value!s})"
        # return f"MyClass({self.value})"

    def __str__(self):
        return str(self.value)

    def __len__(self):
        return len(self.value)

    def __add__(self, other):
        return str(self) + other


obj = MyClass("hello")
assert repr(obj) == "MyClass('hello')"
print(repr(obj))    # == MyClass('hello') #return f"MyClass({self.value!r})"
                    # == MyClass(hello)     #return f"MyClass({self.value!s})"
                    # == MyClass(hello)     #return f"MyClass({self.value})"
assert str(obj) == "hello"
assert len(obj) == 5
assert obj + " world" == "hello world"
