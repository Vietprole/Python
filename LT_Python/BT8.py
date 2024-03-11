with open('E:/Viet/Python/LT Python/fin.txt', 'r') as file:
    line = file.readlines()
    N,K = line[0].split()
    for i in range(N):
        # Read a line of input
        readline = line[1]

        # Split the line into a list of strings
        numbers_as_strings = readline.split()

        # Convert the list of strings to a list of integers
        numbers = [int(number) for number in numbers_as_strings]

        print(numbers)

