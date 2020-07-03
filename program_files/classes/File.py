class File:
    column = 0
    line = 0
    matrix_a = []
    matrix_q = []

    def __init__(self):
        file = open('Aur.in', 'r')
        array = file.readline().split()
        list_number = [num for num in array]
        self.line = int(list_number[0])
        self.column = int(list_number[1])
        array = [list(map(int, row.split())) for row in file.readlines()]
        self.matrix_a = array

        file = open('Calitate.in', 'r')
        array2 = [list(map(int, row.split())) for row in file.readlines()]
        self.matrix_q = array2
