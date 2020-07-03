import os
from sys import platform
import pandas as pd
import random
from colorclass import Color


def cls():
    if platform == "linux" or platform == "linux2":
        return os.system('clear')
    elif platform == "win32":
        return os.system('cls')


class Add:

    def add_column(self, matrix_a, matrix_q, line, column):
        waiting = input('If you want to go to the main menu enter \'quit\'.\nIf you want co continue enter \'go\': ')
        if waiting == 'go':
            cls()
            if line == '0' and column == '0':
                print('Current count of columns is: ' + str(len(matrix_a)))
                new_line = int(input('Enter count of numbers for this column: '))
                cls()

                answer = input('Do you want to enter numbers manually?(y/n): ')
                if answer == 'n':
                    cls()
                    a = int(input('Enter the first border range: '))
                    b = int(input('Enter the second border range: '))
                    for i in range(new_line):
                        matrix_a.insert(i, str(random.randint(a, b)).split())
                    for i in range(new_line):
                        matrix_q.insert(i, str(random.randint(1, 4)).split())
                else:
                    cls()
                    print('Input numbers for this column: ')
                    c = 1
                    for i in range(new_line):
                        print('[' + str(c) + ']', end="")
                        matrix_a.insert(i, input('==> '))
                        c += 1
                    print('Enter gold quality(1 - 4): ')
                    c = 1
                    for i in range(new_line):
                        print('[' + str(c) + ']', end="")
                        matrix_q.insert(i, input('==> '))
                        c += 1

                dataframe = pd.DataFrame(data=matrix_a)  # Reading information
                dataframe.to_csv('Aur.in', sep=' ', header=False, index=False)  # Writing information in file

                dataframe = pd.DataFrame(data=matrix_q)  # Reading information
                dataframe.to_csv('Calitate.in', sep=' ', header=False, index=False)  # Writing information in file

                f = open('Aur.in', 'r+')
                lines = f.readlines()  # Read old content
                f.seek(0)  # Go back to the beginning of the file
                add_column = int(len(matrix_a[0]))
                f.write(str(new_line) + ' ')
                f.write(str(add_column) + '\n')  # Write new content at the beginning
                for f_line in lines:  # Write old content after new
                    f.write(f_line)

            else:
                print('Current count of columns is: ' + str(len(matrix_a[0])))
                k = int(input('Enter the position of the column where it will be placed: '))
                cls()

                answer = input('Do you want to enter numbers manually?(y/n): ')
                if answer == 'n':
                    cls()
                    a = int(input('Enter the first border range: '))
                    b = int(input('Enter the second border range: '))
                    for i in matrix_a:
                        i.insert(k - 1, random.randint(a, b))
                    for i in matrix_q:
                        i.insert(k - 1, random.randint(1, 4))
                else:
                    cls()
                    print('Input numbers for this column: ')
                    c = 1
                    for i in matrix_a:
                        print('[' + str(c) + ']', end = "")
                        i.insert(k - 1, input('==> '))
                        c += 1
                    print('\nEnter gold quality(1 - 4): ')
                    c = 1
                    for i in matrix_q:
                        print('[' + str(c) + ']', end = "")
                        i.insert(k - 1, input('==>'))
                        c += 1

                dataframe = pd.DataFrame(data=matrix_a)  # Reading information
                dataframe.to_csv('Aur.in', sep=' ', header=False, index=False)  # Writing information in file

                dataframe = pd.DataFrame(data=matrix_q)  # Reading information
                dataframe.to_csv('Calitate.in', sep=' ', header=False, index=False)  # Writing information in file

                f = open('Aur.in', 'r+')
                lines = f.readlines()  # Read old content
                f.seek(0)  # Go back to the beginning of the file
                print(len(matrix_a[0]))
                add_column = int(len(matrix_a[0]))
                f.write(str(len(matrix_a)) + ' ')
                f.write(str(add_column) + '\n')  # Write new content at the beginning
                for f_line in lines:  # Write old content after new
                    f.write(f_line)

            cls()
            print(Color('{green}Information successfully written!{/green}\n'))
        else:
            cls()
            pass

    def add_line(self, matrix_a, matrix_q, line, column):
        m = []
        m_q = []
        waiting = input('If you want to go to the main menu enter \'quit\'.\nIf you want co continue enter \'go\': ')
        if waiting == 'go':
            cls()
            if line == '0' and column == '0':
                print('Current count of lines is: ' + str(len(matrix_a[0])))
                new_column = int(input('Enter count of numbers for this column: '))
                cls()

                answer = input('Do you want to enter numbers manually?(y/n): ')
                if answer == 'n':
                    cls()
                    a = int(input('Enter the first border range: '))
                    b = int(input('Enter the second border range: '))
                    m = [random.randint(a, b) for i in range(int(new_column))]
                    m_q = [random.randint(1, 4) for i in range(int(new_column))]
                else:
                    cls()
                    print('Input numbers for this line: ')
                    for i in range(int(new_column)):
                        print('[' + str(i + 1) + ']', end='')
                        a = int(input('==> '))
                        m.append(a)
                    for i in range(int(new_column)):
                        print('[' + str(i + 1) + ']', end='')
                        a = int(input('==> '))
                        m_q.append(a)

                matrix_a.append(m)
                matrix_q.appent(m_q)

                dataframe = pd.DataFrame(data=matrix_a)
                dataframe.to_csv('Aur.in', sep=' ', header=False, index=False)

                dataframe = pd.DataFrame(data=matrix_q) # Reading information
                dataframe.to_csv('Calitate.in', sep=' ', header=False, index=False)  # Writing information in file

                f = open('Aur.in', 'r+')
                lines = f.readlines()  # read old content
                f.seek(0)  # go back to the beginning of the file
                add_line = int(len(matrix_a))
                f.write(str(add_line) + ' ')
                f.write(str(new_column) + '\n')  # write new content at the beginning
                for f_line in lines:  # write old content after new
                    f.write(f_line)

            else:
                print('Current count of lines is: ' + str(len(matrix_a)))
                k = int(input('Enter the position of the line where it will be placed: '))
                cls()

                answer = input('Do you want to enter numbers manually?(y/n): ')
                if answer == 'n':
                    cls()
                    a = int(input('Enter the first border range: '))
                    b = int(input('Enter the second border range: '))
                    m = [random.randint(a, b) for i in range(int(len(matrix_a[0])))]
                    m_q = [random.randint(1, 4) for i in range(int(len(matrix_a[0])))]
                else:
                    cls()
                    print('Input numbers for this line: ')
                    for i in range(int(len(matrix_a[0]))):
                        print('[' + str(i + 1) + ']', end='')
                        a = int(input('==> '))
                        m.append(a)
                    print('\nEnter gold quality(1 - 4): ')
                    for i in range(int(len(matrix_a[0]))):
                        print('[' + str(i + 1) + ']', end='')
                        a = int(input('==> '))
                        m_q.append(a)

                matrix_q.insert(k - 1, m_q)
                matrix_a.insert(k - 1, m)

                dataframe = pd.DataFrame(data=matrix_a)
                dataframe.to_csv('Aur.in', sep=' ', header=False, index=False)

                dataframe = pd.DataFrame(data=matrix_q)  # Reading information
                dataframe.to_csv('Calitate.in', sep=' ', header=False, index=False)  # Writing information in file

                f = open('Aur.in', 'r+')
                lines = f.readlines()  # read old content
                f.seek(0)  # go back to the beginning of the file
                add_line = int(len(matrix_a))
                f.write(str(add_line) + ' ')
                f.write(str(len(matrix_a[0])) + '\n')  # write new content at the beginning
                for f_line in lines:  # write old content after new
                    f.write(f_line)
            cls()
            print(Color('{green}Information successfully written!{/green}\n'))
        else:
            cls()
            pass
