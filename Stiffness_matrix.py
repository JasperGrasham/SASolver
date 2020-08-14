import numpy as np

elements = input("input number of elements:")
elements = int(elements)

def matrix_equations(E, A, L, I_y, I_z, G, I):
    def SM1(E, A, L):
        eqn1 = E * A / L
        return eqn1

    def SM2(E, I_z, L):
        eqn2 = 12 * E * I_z / (L ** 3)
        return eqn2

    def SM3(E, I_y, L):
        eqn3 = 12 * E * I_y / (L ** 3)
        return eqn3

    def SM4(G, I, L):
        eqn4 = G * I / L
        return eqn4

    def SM5(E, I_z, L):
        eqn5 = 6 * E * I_z / (L ** 2)
        return eqn5

    def SM6(E, I_y, L):
        eqn6 = 6 * E * I_y / (L ** 2)
        return eqn6

    def SM7(E, I_y, L):
        eqn7 = 2 * E * I_y / L
        return eqn7

    def SM8(E, I_z, L):
        eqn8 = 2 * E * I_z / L
        return eqn8

    def local():
        x_axis = 12
        y_axis = 12
        a, b = x_axis, y_axis

        X = np.zeros([x_axis, y_axis])

        for i in range(a):
            for j in range(b):
                # Grouped equation placements

                X[0][0] = SM1(E, A, L)
                X[6][6] = SM1(E, A, L)
                X[7][0] = -SM1(E, A, L)
                X[0][7] = -SM1(E, A, L)

                X[1][1] = SM2(E, I_z, L)
                X[7][7] = SM2(E, I_z, L)
                X[7][1] = -SM2(E, I_z, L)
                X[1][7] = -SM2(E, I_z, L)

                X[2][2] = SM3(E, I_y, L)
                X[8][8] = SM3(E, I_y, L)
                X[8][2] = -SM3(E, I_y, L)
                X[2][8] = -SM3(E, I_y, L)

                X[3][3] = SM4(G, I, L)
                X[9][9] = SM4(G, I, L)
                X[9][3] = -SM4(G, I, L)
                X[3][9] = -SM4(G, I, L)

                X[1][5] = SM5(E, I_z, L)
                X[1][11] = SM5(E, I_z, L)
                X[5][7] = -SM5(E, I_z, L)
                X[7][11] = -SM5(E, I_z, L)
                X[5][1] = SM5(E, I_z, L)
                X[11][1] = SM5(E, I_z, L)
                X[7][5] = -SM5(E, I_z, L)
                X[11][7] = -SM5(E, I_z, L)

                X[2][4] = -SM6(E, I_y, L)
                X[2][10] = -SM6(E, I_y, L)
                X[4][8] = SM6(E, I_y, L)
                X[8][10] = SM6(E, I_y, L)
                X[4][2] = -SM6(E, I_y, L)
                X[10][2] = -SM6(E, I_y, L)
                X[8][4] = SM6(E, I_y, L)
                X[10][8] = SM6(E, I_y, L)

                X[4][4] = 2 * SM7(E, I_y, L)
                X[4][10] = SM7(E, I_y, L)
                X[5][5] = 2 * SM7(E, I_y, L)
                X[10][10] = 2 * SM7(E, I_y, L)
                X[10][4] = SM7(E, I_y, L)

                X[5][11] = SM8(E, I_z, L)
                X[11][11] = SM8(E, I_z, L)
                X[11][5] = SM8(E, I_z, L)
        return X

    local_matrix = local()
    return local_matrix
