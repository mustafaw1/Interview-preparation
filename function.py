def function1(a, b):
    print("hello you are in function1")

def function2(a, b):
    """This is a function that calculate average of two numbers"""
    average = (a+b/2)
    return average
print(function2.__doc__)

