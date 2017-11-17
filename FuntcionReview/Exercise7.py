def log(func):
    def func_wrapper(name):
        print("The Man, The Myth, The Legend")
        func(message)
    return func_wrapper

@log
def my_function(message):
    print(message)

message = input("Please input message here:")
my_function(message)
