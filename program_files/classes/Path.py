from terminaltables import SingleTable
from colorclass import Color

class Path:
    x = []
    def calculate_path(self, matrix, line, column):
        i = 0
        j = 0
        end = matrix[-1][-1]

        while matrix[i][j] != end:
            if matrix[i][j] == matrix[-1][-1]:
                break
            if i == 0 and j == 0:
                self.x.append(matrix[i][j])
            if i >= line - 1:
                self.x.append(matrix[i][j + 1])
                matrix[i][j + 1] = Color('{green}⮞{/green}')
                j += 1
                continue
            if j >= column - 1:
                self.x.append(matrix[i + 1][j])
                matrix[i + 1][j] = Color('{green}⮟{/green}')
                i += 1
                continue
            if matrix[i + 1][j] > matrix[i][j + 1]:
                self.x.append(matrix[i + 1][j])
                matrix[i + 1][j] = Color('{green}⮟{/green}')
                i += 1
            elif matrix[i][j + 1] > matrix[i + 1][j]:
                self.x.append(matrix[i][j + 1])
                matrix[i][j + 1] = Color('{green}⮞{/green}')
                j += 1

    def show_result(self, matrix, line):
        matrix[0][0] = Color('{green}START{/green}')
        matrix[-1][-1] = Color('{red}FINISH{/red}')
        table = SingleTable(matrix)
        table.title = Color('{yellow}Path{/yellow}')
        table.inner_row_border = True
        table.inner_heading_row_border = False
        for i in range(line+1):
            table.justify_columns[i] = 'center'
        print(table.table)
        print('\nThe maximum amount of gold that the robot can mine =', sum(self.x))
