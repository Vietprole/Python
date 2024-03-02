def swap(a, b):
    return b, a
a = 2
b = 3
x, y = swap(a, b)
print(x, y)
z = swap(a, b)
print(z)
#find type of z
print(type(z))

def greeter(name,
    title = 'Dr',
    prompt = 'Welcome',
    message = 'Live Long and Prosper'):
    """
    This function takes defines 4 parameters;
    name, title, prompt and message
    """
    print(prompt, title, name, '-', message)
greeter("Quyen")
# arguments can be passed in any order
greeter(message = 'We like Python', name = 'Lisa')
greeter('Rossie', message = 'We like Python')