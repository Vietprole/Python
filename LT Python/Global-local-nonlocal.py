max = 100
def print_max():
    global max
    max = max + 1
print(max)
print_max()
print(max)

def outer():
    title = 'original title'
    def inner():
        nonlocal title
        title = 'another title'
        print('inner:', title)
    inner()
    print('outer:', title)
outer()