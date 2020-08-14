import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections as mc

def image_view(x, y, z, final_x, final_y, final_z, xa_connections, ya_connections, za_connections, xa_connections_deflec, ya_connections_deflec, za_connections_deflec):
    mpl.rcParams['legend.fontsize'] = 10

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.scatter(x, y, z, color='black', s=1)
    ax.scatter(final_x, final_y, final_z, color ='green', s=1)

    for i in range(0,len(xa_connections)):
        ax.plot(xa_connections[i], ya_connections[i], za_connections[i], color='black', linewidth='1', linestyle='dashed')
        ax.plot(xa_connections_deflec[i], ya_connections_deflec[i], za_connections_deflec[i], color='green', linewidth='2')

    ax.legend(['Original Structure', 'Deformed Structure'], loc='upper right')

    ax.view_init(20, 40) # top and side swivel
    fig

    x_lim = max(x) + 1000

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_xlim([0, x_lim])
    ax.set_ylim([0, x_lim])
    ax.set_zlim([0, x_lim])
    plt.show(block=True)
    plt.show()
