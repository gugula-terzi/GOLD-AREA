from terminaltables import SingleTable
from colorclass import Color


class Average:
    mat_1 = []
    mat_2 = []
    mat_3 = []
    mat_4 = []

    def calculate_average(self, matrix_a, matrix_q):
        for i in range(len(matrix_a)):
            for j in range(len(matrix_a)):
                if matrix_q[i][j] == 1:
                    self.mat_1.append(matrix_a[i][j])
                if matrix_q[i][j] == 2:
                    self.mat_2.append(matrix_a[i][j])
                if matrix_q[i][j] == 3:
                    self.mat_3.append(matrix_a[i][j])
                if matrix_q[i][j] == 4:
                    self.mat_4.append(matrix_a[i][j])

    def show_average(self):
         quality = [['Quality №1', round(sum(self.mat_1) / len(self.mat_1), 2)],
                    ['Quality №2', round(sum(self.mat_2) / len(self.mat_2), 2)],
                    ['Quality №3', round(sum(self.mat_3) / len(self.mat_3), 2)],
                    ['Quality №4', round(sum(self.mat_4) / len(self.mat_4), 2)]]

         table = SingleTable(quality)
         table.title = Color('{blue}Average{/blue}')
         table.inner_row_border = True
         table.inner_heading_row_border = False
         print(table.table)
         print()
