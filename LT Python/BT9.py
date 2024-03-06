class Matrix:
    def __init__(self, n, m, initial_value=0):
        self.rows = n
        self.cols = m
        self.matrix = [[initial_value for _ in range(m)] for _ in range(n)]

    def from_file(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            self.rows, self.cols = map(int, lines[0].split())
            self.matrix = [[int(x) for x in line.split()] for line in lines[1:]]

    def display(self):
        for row in self.matrix:
            print(row)

    def find_max_adjacent_value:
        