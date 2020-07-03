import os
from sys import platform
import pandas as pd
import numpy as np


def cls():
    if platform == "linux" or platform == "linux2":
        return os.system('clear')
    elif platform == "win32":
        return os.system('cls')


class Delete:
    def del_line(self, matrix_a, matrix_q, line, column):

        waiting = input('If you want to go to the main menu enter \'quit\'.\nIf you want co continue enter \'go\': ')
        if waiting == 'go':
            cls()
            if column != '0' and line != '0':
                print('Current count of lines is: ' + str(len(matrix_a)))
                k = int(input('Enter the number of line which you want to delete: '))

                while k <= 0 or k > int(line):
                    cls()
                    print('This number of line doesn\'t exist\n')
                    print('Current count of lines is: ' + str(line))
                    k = int(input('Enter the number of line which you want to delete: '))

                matrix_a.remove(matrix_a[k - 1])
                matrix_q.remove(matrix_q[k - 1])

                dataframe = pd.DataFrame(data=matrix_a)
                dataframe.to_csv('Aur.in', sep=' ', header=False, index=False)

                dataframe = pd.DataFrame(data=matrix_q)  # Reading information
                dataframe.to_csv('Calitate.in', sep=' ', header=False, index=False)  # Writing information in file

                f = open('Aur.in', 'r+')
                lines = f.readlines()  # read old content
                f.seek(0)  # go back to the beginning of the file
                del_line = int(len(matrix_a))
                column = int(len(matrix_a[0]))
                if del_line == 0:
                    column = 0
                f.write(str(del_line) + ' ')
                f.write(str(column) + '\n')  # write new content at the beginning
                for f_line in lines:  # write old content after new
                    f.write(f_line)

                cls()
            else:
                print('\n    File is empty!\n')
        else:
            pass

    def del_column(self, matrix_a, matrix_q, line, column):
        print(len(matrix_a[0]))
        waiting = input('If you want to go to the main menu enter \'quit\'.\nIf you want co continue enter \'go\': ')
        if waiting == 'go':
            cls()
            if column != '0' and line != '0':
                print('Current count of column is: ' + str(len(matrix_a[0])))
                k = int(input('Enter the number of line which you want to delete: '))

                while k <= 0 or k > int(len(matrix_a[0])):
                    cls()
                    print('This number of line doesn\'t exist\n')
                    print('Current count of column is: ' + str(len(matrix_a[0])))
                    k = int(input('Enter the number of line which you want to delete: '))

                matrix_a = np.delete(matrix_a, k - 1, axis=1)
                matrix_q = np.delete(matrix_q, k - 1, axis=1)

                dataframe = pd.DataFrame(data=matrix_a)
                dataframe.to_csv('Aur.in', sep=' ', header=False, index=False)

                dataframe = pd.DataFrame(data=matrix_q)  # Reading information
                dataframe.to_csv('Calitate.in', sep=' ', header=False, index=False)  # Writing information in file

                f = open('Aur.in', 'r+')
                lines = f.readlines()  # read old content
                f.seek(0)  # go back to the beginning of the file
                column = int(len(matrix_a[0]))
                line = int(len(matrix_a))
                print(line, column)
                if column == 0:
                    line = 0
                f.write(str(line) + ' ')
                f.write(str(column) + '\n')  # write new content at the beginning
                for f_line in lines:  # write old content after new
                    f.write(f_line)

                print(len(matrix_a[0]))
                cls()
            else:
                print('\n    File is empty!\n')
        else:
            pass
