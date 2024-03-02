import timeit
my_list = list(range(1000000))
execution_time = timeit.timeit(lambda: [x * 2 for x in my_list], number=10)
print(f"Execution time: {execution_time} seconds")
