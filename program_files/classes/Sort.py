import random
from terminaltables import SingleTable
from colorclass import Color


def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        q = random.choice(a)
        l, r, m = ([] for i in range(3))
        for elem in a:
            if elem > q:
                l.append(elem)
            elif elem < q:
                r.append(elem)
            else:
                m.append(elem)
        return quick_sort(l) + m + quick_sort(r)


class Sort:
    mat = []

    def gold_sort(self, matrix_a, matrix_q):
        mat_1, mat_2, mat_3, mat_4 = ([] for i in range(4))

        for i in range(len(matrix_a)):
            for j in range(len(matrix_a)):
                if matrix_q[i][j] == 1:
                    mat_1.append(matrix_a[i][j])
                if matrix_q[i][j] == 2:
                    mat_2.append(matrix_a[i][j])
                if matrix_q[i][j] == 3:
                    mat_3.append(matrix_a[i][j])
                if matrix_q[i][j] == 4:
                    mat_4.append(matrix_a[i][j])

        self.mat = [[len(mat_1), sum(mat_1), 1],
               [len(mat_2), sum(mat_2), 2],
               [len(mat_3), sum(mat_3), 3],
               [len(mat_4), sum(mat_4), 4]]

        self.mat = quick_sort(self.mat)
        self.mat.insert(0, ['Number of zones', 'Gold amount', 'Quality'])
        for i in range(5):
            self.mat[i][0], self.mat[i][2] = self.mat[i][2], self.mat[i][0]

    def show_sorted_gold(self):
        table = SingleTable(self.mat)
        table.title = Color('{blue}Sorted gold{/blue}')
        table.inner_row_border = True
        table.inner_heading_row_border = False
        for i in range(5):
            table.justify_columns[i] = 'center'
        print(table.table)
        print()