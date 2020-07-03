from terminaltables import SingleTable
from classes.File import File
from colorclass import Color


class LMM:
    lmm = []
    obj_file = File()
    matrix_a = obj_file.matrix_a

    def compare(self, x, y):
        Z = []
        # U - верх, RL, D - низ, С - середина
        UL = (x - 1, y - 1)
        UC = (x - 1, y)
        UR = (x - 1, y + 1)
        LC = (x, y - 1)
        RC = (x, y + 1)
        DL = (x + 1, y - 1)
        DC = (x + 1, y)
        DR = (x + 1, y + 1)
        Z_ = [UL, UC, UR, LC, RC, DL, DC, DR]
        for z in Z_:
            try:
                x_, y_ = z
                if x_ >= 0 and y_ >= 0:
                    Z.append(self.matrix_a[x_][y_])
            except IndexError:
                pass
        return Z

    def show_lmm(self, matrix_a):
        for n in range(len(matrix_a)):
            for m in range(len(matrix_a[0])):
                if matrix_a[n][m] < min(self.compare(n, m)):
                    self.lmm.append([matrix_a[n][m], n, m])

        self.lmm.insert(0, ['Local\nnumber', 'coordinate\nx', 'coordinate\ny'])
        table = SingleTable(self.lmm)
        table.inner_row_border = True
        for i in range(len(matrix_a)):
            table.justify_columns[i] = 'center'
        print(table.table)
