# * - unpacking operator
# args - arguments
def greet(*args):
    # print("Hello ", *args)
    print(sum(args))

greet(40, 30, 50)

# kwargs - key word arguments

def build_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

build_profile(name = "John ", age = 25, location = "Thika")