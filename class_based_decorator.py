def add_logging(cls):
    """Decorator function to add logging to all methods of a class"""

    class LoggedClass(cls):
        def __getattribute__(self, name):
            attribute = super().__getattribute__(name)
            if callable(attribute):

                def logged_method(*args, **kwargs):
                    print(
                        f"Calling method '{name}' with args {args} and kwargs {kwargs}"
                    )
                    return attribute(*args, **kwargs)

                return logged_method
            else:
                return attribute

    return LoggedClass


# Applying the decorator to a class
@add_logging
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


# Creating an instance of the decorated class
calc = Calculator()

# Using the decorated methods
# result1 = calc.add(5, 3)
# result2 = calc.subtract(8, 2)

# print("Result of addition:", result1)
# print("Result of subtraction:", result2)


def d(func):
    def outer(*args, **kwargs):
        print("executing first")
        func(*args, **kwargs)

    return outer


@d
def test_func(x, y, z):
    print(f"x = {x}, y = {y}, z = {z}")


test_func(10, y=20, z=30)
