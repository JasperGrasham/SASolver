import numpy as np

def node_location(nodes): # The dictionary is called node_location!
    array = np.ones([nodes, ])
    iterations = len(array)
    desiredDict = {}
    for i in range(iterations):
        array[i] = (1 * i) + 1
        key = array[i]
        i += i+1
        valList = []
        print('Current node - ', key)
        valList.append(input("Input Coords (separated by comma)\n").split(','))
        desiredDict[key] = valList
    return desiredDict

def degrees_of_freedom(nodes):
    array = np.ones([nodes, ])
    iterations = len(array)
    desiredDict = {}
    for i in range(iterations):
        array[i] = (1 * i) + 1
        key = array[i]
        valList = [1+(6*i), 2+(6*i), 3+(6*i), 4+(6*i), 5+(6*i), 6+(6*i)]
        desiredDict[key] = valList
        i += i+1
    return desiredDict

def element_pairings(elements):
    array = np.ones([elements, ])
    iterations = len(array)
    desiredDict = {}
    for i in range(iterations):
        array[i] = (1 * i) + 1
        key = array[i]
        i += i + 1
        valList = []
        print('Current element - ', key)
        valList.append(input("Interconnecting nodes (separated by comma)- "))
        desiredDict[key] = valList
    return desiredDict

def forces(nodes):
    array = np.ones([nodes, ])
    iterations = len(array)
    desiredDict = {}
    for i in range(iterations):
        array[i] = (1 * i) + 1
        key = array[i]
        i += i + 1
        valList = []
        print('Current node - ', key)
        valList.append(input("Node force vector - \n"))
        desiredDict[key] = valList
    return desiredDict

def fixed_dofs():
    fixed_dofs = input("Nodes with fixed Dofs (separate with space only) - ", )
    return fixed_dofs

def element_info(elements):
    array = np.ones([elements, ])
    iterations = len(array)
    desiredDict = {}

    def elasticity():
        elast = []
        for i in range(iterations):
            array[i] = (1 * i) + 1
            key = array[i]
            i += i + 1
            print('Current element information:', key)
            elasticity = input("Input elasticity\n")
            elasticity = int(elasticity)
            elast.append(elasticity)
        desiredDict['Elasticity'] = elast
        return desiredDict

    def area():
        elast = []
        for i in range(iterations):
            array[i] = (1 * i) + 1
            key = array[i]
            i += i + 1
            print('Current element information:', key)
            elasticity = input("Input area\n")
            elasticity = int(elasticity)
            elast.append(elasticity)
        desiredDict['Area'] = elast
        return desiredDict

    def length():
        elast = []
        for i in range(iterations):
            array[i] = (1 * i) + 1
            key = array[i]
            i += i + 1
            print('Current element information:', key)
            elasticity = input("Input length\n")
            elasticity = int(elasticity)
            elast.append(elasticity)
        desiredDict['Length'] = elast
        return desiredDict

    def I_y():
        elast = []
        for i in range(iterations):
            array[i] = (1 * i) + 1
            key = array[i]
            i += i + 1
            print('Current element information:', key)
            elasticity = input("Input I_y\n")
            elasticity = int(elasticity)
            elast.append(elasticity)
        desiredDict['I_y'] = elast
        return desiredDict

    def I_z():
        elast = []
        for i in range(iterations):
            array[i] = (1 * i) + 1
            key = array[i]
            i += i + 1
            print('Current element information:', key)
            elasticity = input("Input I_z\n")
            elasticity = int(elasticity)
            elast.append(elasticity)
        desiredDict['I_z'] = elast
        return desiredDict

    def G():
        elast = []
        for i in range(iterations):
            array[i] = (1 * i) + 1
            key = array[i]
            i += i + 1
            print('Current element information:', key)
            elasticity = input("Input G\n")
            elasticity = int(elasticity)
            elast.append(elasticity)
        desiredDict['G'] = elast
        return desiredDict

    def I():
        elast = []
        for i in range(iterations):
            array[i] = (1 * i) + 1
            key = array[i]
            i += i + 1
            print('Current element information:', key)
            elasticity = input("Input I\n")
            elasticity = int(elasticity)
            elast.append(elasticity)
        desiredDict['I'] = elast
        return desiredDict

    """
    def v():
        for i in range(iterations):
            array[i] = (1 * i) + 1
            key = array[i]
            i += i + 1
            valList = []
            print('Current element information:', key)
            v = input("Input v of current element\n")
            v = int(v)
            valList.append(v)
            desiredDict[v] = valList
        return desiredDict
    """
    elasticity()
    area()
    length()
    I_y()
    I_z()
    G()
    I()

    return desiredDict

