def decorator(func):
    def wrapper():
        print("Before a given task.")
        func()
        print("After a given task.")
    return wrapper

@decorator
def greet():
    print("Hello World!")

greet()


# decorators with parameters

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution.")
        results = func(*args, **kwargs)
        print("After execution.")
        return results
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(4,5))
