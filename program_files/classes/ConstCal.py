from colorclass import Color


class ConstCal:
    def const_cal(self, matrix_a, matrix_q, line, column):
        mat, mat_1, mat_2 = ([] for i in range(3))

        for i in range(int(line)):
            for j in range(int(column)):
                if matrix_q[i][j] == 1:
                    mat_1.append(matrix_a[i][j])
                if matrix_q[i][j] == 2:
                    mat_2.append(matrix_a[i][j])

        with open('ConstCal.txt', 'w') as file:
            for i in mat_1:
                file.write(str(i) + ' ')
            file.write('\n')
            for i in mat_2:
                file.write(str(i) + ' ')

        print(Color('{green}Information was successfully written!{/green}\n'))