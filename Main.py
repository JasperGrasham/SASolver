#!/usr/bin/env python

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import SAS
import Input
import Image_view
import Stiffness_matrix

def Main():

    # Inputs
    nodes = input("input number of nodes:")
    nodes = int(nodes)

    elements = input("input number of elements:")
    elements = int(elements)
    node_locations = Input.node_location(nodes)
    degrees_of_freedom = Input.degrees_of_freedom(nodes)
    element_pairings = Input.element_pairings(elements)
    forces = Input.forces(nodes)
#    fixed_dofs = Input.fixed_dofs()
    element_info = Input.element_info(elements)

    # Assigning the nodes their plotted location:
    raw_data = [i[0] for i in node_locations.values()]
    x = [str(raw_data[i][0] + '') for i in range(len(node_locations))]
    y = [str(raw_data[i][1] + '') for i in range(len(node_locations))]
    z = [str(raw_data[i][2] + '') for i in range(len(node_locations))]
    for i in range(0, len(x)):
        x[i] = int(x[i])
        y[i] = int(y[i])
        z[i] = int(z[i])

    # Showing the dictionary containing all element information
#    print(element_info)

    # Arranging the dictionary
    E = [element_info['Elasticity'][i] for i in range(0,elements)]
    A = [element_info['Area'][i] for i in range(0,elements)]
    L = [element_info['Length'][i] for i in range(0, elements)]
    I_y = [element_info['I_y'][i] for i in range(0, elements)]
    I_z = [element_info['I_z'][i] for i in range(0, elements)]
    G = [element_info['G'][i] for i in range(0, elements)]
    I = [element_info['I'][i] for i in range(0, elements)]

    if elements == 1:
        E = E[0]
        A = A[0]
        L = L[0]
        I_y = I_y[0]
        I_z = I_z[0]
        G = G[0]
        I = I[0]

        Local_matrix = Stiffness_matrix.matrix_equations(E, A, L, I_y, I_z, G, I)
        global_matrix = Local_matrix
        Dofs = 6

        force_matrix = []
        for i in range(1, nodes + 1):
            force_vec_list = forces[i][0].split(",")
            force_matrix.append(force_vec_list)

        vec = np.concatenate(force_matrix).ravel()
        final_force_vec = np.array(vec, dtype=np.float32)

        inverse_k = np.linalg.pinv(global_matrix)

        known_forces = np.nonzero(final_force_vec)[0]

        dofs = np.zeros([nodes * Dofs, 1])

        for i in range(0, len(known_forces)):
            first = known_forces[i]
            dofs[first] += np.matmul(inverse_k[first], final_force_vec)

        restrained_dofs = Input.fixed_dofs().split()
        for i in range(0, len(restrained_dofs)):
            final_force_vec[i] += np.matmul(global_matrix[i], dofs)

        final_dofs = np.matmul(inverse_k, final_force_vec)

        x_deflec, y_deflec, z_deflec = ([], [], [])

        for i in range(0, nodes * Dofs - 1, 6):
            x_dofs = final_dofs[i]
            y_dofs = final_dofs[i + 2]
            z_dofs = final_dofs[i + 4]
            x_deflec.append(x_dofs)
            y_deflec.append(y_dofs)
            z_deflec.append(z_dofs)

        final_x = [x[i] + x_deflec[i] for i in range(len(x))]
        final_y = [y[i] + y_deflec[i] for i in range(len(y))]
        final_z = [z[i] + z_deflec[i] for i in range(len(z))]
        print(final_x, final_y, final_z)

        #   View of initial and deflected shape
        Image_view.image_view(x, y, z, final_x, final_y, final_z)

    elif elements > 1:
        E = [E[i] for i in range(elements)]
        A = [A[i] for i in range(elements)]
        L = [L[i] for i in range(elements)]
        I_y = [I_y[i] for i in range(elements)]
        I_z = [I_z[i] for i in range(elements)]
        G = [G[i] for i in range(elements)]
        I = [I[i] for i in range(elements)]

        # Creating a function that allows the local matrix to be retrieved.

        def local():
            local_matrix_list = []
            for i in range(1, len(E)+1):
                Local_matrix = Stiffness_matrix.matrix_equations(E[i-1:i][0], A[i-1:i][0], L[i-1:i][0],
                                                                 I_y[i-1:i][0], I_z[i-1:i][0], G[i-1:i][0],
                                                                 I[i-1:i][0])
                local_matrix_list.append(Local_matrix)
                i += i+1
            return local_matrix_list

        local_matricies = local()

        # Assigning locals to global:

        Dofs = 6
        global_matrix = np.zeros([Dofs * nodes, Dofs * nodes])

        top_left_list = []
        top_right_list = []
        bottom_left_list = []
        bottom_right_list = []

        for i in range(0, elements):
            top_left_local = local_matricies[i][0:6, 0:6]
            top_right_local = local_matricies[i][0:6, 6:12]
            bottom_left_local = local_matricies[i][6:12, 6:12]
            bottom_right_local = local_matricies[i][6:12, 0:6]
            top_left_list.append(top_left_local)
            top_right_list.append(top_right_local)
            bottom_left_list.append(bottom_left_local)
            bottom_right_list.append(bottom_right_local)
            i = i + 1

        for i in range(1, nodes):

            global_matrix[(int(i-1))*Dofs:i*Dofs, int((i-1))*Dofs:i*Dofs] += top_left_list[i-1]  # top lefts
#            global_matrix[i*Dofs:int(i+1)*Dofs, i*Dofs:int((i+1))*Dofs] += top_left_list[i]

            global_matrix[(int(i-1))*Dofs:i*Dofs, i*Dofs:int(i+1)*Dofs] += top_right_list[i-1]  # top rights
#           global_matrix[i*Dofs:int(i+1)*Dofs, int(i+1)*Dofs:int((i+2))*Dofs] += top_right_list[i-1]

            global_matrix[i*Dofs:int(i+1)*Dofs, i*Dofs:int(i+1)*Dofs] += bottom_left_list[i-1]  # bottom left list
#            global_matrix[int(i+1)*Dofs:int((i+2))*Dofs, int(i+1)*Dofs:int((i+2))*Dofs] += bottom_left_list[i-1]

            global_matrix[i*Dofs:int(i+1)*Dofs, (int(i-1))*Dofs:i*Dofs] += bottom_right_list[i-1]  # bottom right list
#            global_matrix[int(i+1)*Dofs:int((i+2))*Dofs, i*Dofs:int((i+1))*Dofs] += bottom_right_list[i-1]

        # Creating the force matrix (physical, temperature and reaction loads):
        force_matrix = []
        for i in range(1, nodes+1):
            force_vec_list = forces[i][0].split(",")
            force_matrix.append(force_vec_list)

        vec = np.concatenate(force_matrix).ravel()
        final_force_vec = np.array(vec, dtype=np.float32)

        inverse_k = np.linalg.pinv(global_matrix)

        known_forces = np.nonzero(final_force_vec)[0]

        dofs = np.zeros([nodes*Dofs,1])

        for i in range(0, len(known_forces)):
            first = known_forces[i]
            dofs[first] += np.matmul(inverse_k[first], final_force_vec)

        restrained_dofs = Input.fixed_dofs().split()
        for i in range(0, len(restrained_dofs)):
            final_force_vec[i] += np.matmul(global_matrix[i], dofs)

        final_dofs = np.matmul(inverse_k, final_force_vec)

        x_deflec, y_deflec, z_deflec = ([], [], [])

        for i in range(0, nodes * Dofs - 1, 6):
            x_dofs = final_dofs[i]
            y_dofs = final_dofs[i+2]
            z_dofs = final_dofs[i+4]
            x_deflec.append(x_dofs)
            y_deflec.append(y_dofs)
            z_deflec.append(z_dofs)

        final_x = [x[i] + x_deflec[i] for i in range(len(x))]
        final_y = [y[i] + y_deflec[i] for i in range(len(y))]
        final_z = [z[i] + z_deflec[i] for i in range(len(z))]

        element_pairing_list = []
        for i in range(1, elements+1):
            element_pairings_el1 = element_pairings[i][0].split(",")
            element_pairing_list.append(element_pairings_el1)

        final_element_pairing_list = np.concatenate(element_pairing_list).ravel()

        xa_connections = []
        ya_connections = []
        za_connections = []

        xa_connections_deflec = []
        ya_connections_deflec = []
        za_connections_deflec = []

        original_corrections = []
        deflected_connections = []
        for i in range(0,len(final_element_pairing_list), 2):
            first_node = final_element_pairing_list[i]
            first_node = int(first_node)
            i = i + 1
            second_node = final_element_pairing_list[i]
            second_node = int(second_node)

            # original coordinates
            x_loc_1 = x[first_node-1]
            y_loc_1 = y[first_node-1]
            z_loc_1 = z[first_node-1]
            x_loc_2 = x[second_node-1]
            y_loc_2 = y[second_node-1]
            z_loc_2 = z[second_node-1]

            # deflected coordinates
            x_loc_1_deflec = final_x[first_node - 1]
            y_loc_1_deflec = final_y[first_node - 1]
            z_loc_1_deflec = final_z[first_node - 1]
            x_loc_2_deflec = final_x[second_node - 1]
            y_loc_2_deflec = final_y[second_node - 1]
            z_loc_2_deflec = final_z[second_node - 1]

            x_list_used = [x_loc_1, x_loc_2]
            y_list_used = [y_loc_1, y_loc_2]
            z_list_used = [z_loc_1, z_loc_2]

            x_list_used_deflec = [x_loc_1_deflec, x_loc_2_deflec]
            y_list_used_deflec = [y_loc_1_deflec, y_loc_2_deflec]
            z_list_used_deflec = [z_loc_1_deflec, z_loc_2_deflec]

            xa_connections.append(x_list_used)
            ya_connections.append(y_list_used)
            za_connections.append(z_list_used)

            xa_connections_deflec.append(x_list_used_deflec)
            ya_connections_deflec.append(y_list_used_deflec)
            za_connections_deflec.append(z_list_used_deflec)

        #   View of initial and deflected shape
        Image_view.image_view(x, y, z, final_x, final_y, final_z, xa_connections, ya_connections, za_connections, xa_connections_deflec, ya_connections_deflec, za_connections_deflec)

    else:
        print('nothing')

if __name__ == '__main__':
    Main()
