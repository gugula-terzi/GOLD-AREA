import os
from sys import platform
from classes.Path import Path
from classes.File import File
from classes.Show import Show
from classes.Add import Add
from classes.Delete import Delete
from classes.Average import Average
from classes.ConstCal import ConstCal
from classes.Sort import Sort
from classes.LMM import LMM
from terminaltables import AsciiTable
from colorclass import Color


# ================================== [Functions] ================================
def cls():
    if platform == "linux" or platform == "linux2":
        os.system(['clear'][os.name == os.sys.platform])
    elif platform == "win32":
        os.system(['cls'][os.name == os.sys.platform])
# ===============================================================================


# ================================== [Variables] ================================
obj_file = File()
# ===============================================================================


while True:
    menu = [
        ['1', 'Show information about gold'],
        ['2', 'Show information about gold quality'],
        ['3', 'Add column'],
        ['4', 'Add line'],
        ['5', 'Delete line'],
        ['6', 'Delete column'],
        ['7', 'Find average for each quality'],
        ['8', 'Write to a new file all the gold that has quality 1 and 2'],
        ['9', 'Show information about gold'],
        ['10', 'Find the maximum amount of gold that the robot can mine'],
        ['11', 'Find local minimums in the matrix'],
        ['0', 'Close program']
    ]
    table = AsciiTable(menu)
    table.title = Color('{blue}Menu{/blue}')
    table.inner_row_border = True
    table.inner_heading_row_border = False
    print(table.table)

    answer = input('Your choice: ')
    print()

    if answer == '1':
        cls()
        obj_show = Show()
        show_aur = obj_show.show_aur(obj_file.matrix_a, obj_file.line, obj_file.column)

    elif answer == '2':
        cls()
        obj_show = Show()
        show_calitate = obj_show.show_calitate(obj_file.matrix_q)

    elif answer == '3':
        cls()
        obj_add_col = Add()
        obj_add_col.add_column(obj_file.matrix_a, obj_file.matrix_q, obj_file.line, obj_file.column)

    elif answer == '4':
        cls()
        obj_add_line = Add()
        obj_add_line.add_line(obj_file.matrix_a, obj_file.matrix_q, obj_file.line, obj_file.column)

    elif answer == '5':
        cls()
        obj_del = Delete()
        obj_del.del_line(obj_file.matrix_a, obj_file.matrix_q, obj_file.line, obj_file.column)

    elif answer == '6':
        cls()
        obj_del = Delete()
        obj_del.del_column(obj_file.matrix_a, obj_file.matrix_q, obj_file.line, obj_file.column)

    elif answer == '7':
        cls()
        obj_average = Average()
        average = obj_average.calculate_average(obj_file.matrix_a, obj_file.matrix_q)
        show_average = obj_average.show_average()

    elif answer == '8':
        cls()
        obj_cal = ConstCal()
        obj_cal.const_cal(obj_file.matrix_a, obj_file.matrix_q, obj_file.line, obj_file.column)

    elif answer == '9':
        cls()
        obj_sort = Sort()
        obj_sort.gold_sort(obj_file.matrix_a, obj_file.matrix_q)
        obj_sort.show_sorted_gold()

    elif answer == '10':
        cls()
        obj_path = Path()
        find_path = obj_path.calculate_path(obj_file.matrix_a, obj_file.line, obj_file.column)
        show_path = obj_path.show_result(obj_file.matrix_a, obj_file.line)
        print()

    elif answer == '11':
        cls()
        obj_lmm = LMM()
        obj_lmm.show_lmm(obj_file.matrix_a)

    elif answer == '0':
        break

    else:
        cls()
        print(Color('{red}Incorrect number{/red}\n'))
