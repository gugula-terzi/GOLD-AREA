from terminaltables import SingleTable
from colorclass import Color


class Show:
    def show_aur(self, matrix_a, line, column):
        try:
            if line == '0' and column == '0':
                print(Color('{red}File is empty!{/red}\n'))
            elif matrix_a != []:
                table = SingleTable(matrix_a)
                table.title = Color('{autoyellow}GOLD-BEARING AREA{/autoyellow}')
                table.inner_row_border = True
                table.inner_heading_row_border = False
                print(table.table)
                print()

        except FileNotFoundError:
            print(Color('{red}File wasn\'t found{/red}\n'))

    def show_calitate(self, matrix_q):
        try:
            for i in matrix_q:
                if i == []:
                    print(Color('{red}File is empty!{/red}\n'))
                    break
                else:
                    table = SingleTable(matrix_q)
                    table.title = Color('{autoyellow}GOLD QUALITY{/autoyellow}')
                    table.inner_row_border = True
                    table.inner_heading_row_border = False
                    print(table.table)
                    print()
                    break

        except FileNotFoundError:
            print(Color('{red}File wasn\'t found{/red}\n'))
