import numpy as np
from copy import copy, deepcopy

class node(object):
    def __init__(self, initializedNode = None):
        if (initializedNode == None):
            self.__matrix = np.array([  [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0],
                                        [0, 0, 0, 0]    ])

            self.__blankPos = { "row" : 0, 
                                "col" : 0 }
            self.__f_val = 0
            self.__g_val = 0
        
        else:
            self.__matrix = copy(initializedNode.__matrix)
            self.__blankPos = copy(initializedNode.__blankPos)
            self.__f_val = initializedNode.__f_val
            self.__g_val = initializedNode.__g_val
    
    @classmethod
    def fromFile(cls, filePath):
        pass
    
    @classmethod
    def fromInput(cls):
        rootNode = node()
        for row in range (4):
            for col in range (4):
                rootNode.__matrix[row][col] = int(input())
                if (rootNode.__matrix[row][col] == 0):
                    rootNode.__blankPos["row"] = row
                    rootNode.__blankPos["col"] = col
            
        rootNode.__f_val = None
        rootNode.__g_val = None

        return cls(rootNode)

    @classmethod
    def move(cls, parentNode, moveDirection):
        childNode = deepcopy(parentNode)
        childNode.__swapBlank(moveDirection)

        return cls(childNode)

    def __swapBlank(self, moveDirection):
        # Initializing variables
        blankRow = self.__blankPos["row"]
        print(blankRow)
        blankCol = self.__blankPos["col"]
        print(blankCol)
        rowToSwap = blankRow
        colToSwap = blankCol

        if (moveDirection == "RIGHT"):
            if (blankCol == 3):
               rowToSwap = rowToSwap + (int)(colToSwap / 3)
               colToSwap = (colToSwap + 1) % 4

        elif (moveDirection == "LEFT"):
            if (blankCol == 0):
               rowToSwap = rowToSwap - (int)(colToSwap / 3)
               colToSwap = (colToSwap + 1) % 4

        elif (moveDirection == "DOWN"):
            rowToSwap += 1

        elif (moveDirection == "UP"):
            rowToSwap -= 1

        # Swapping blank-cell with cell-to-swap
        blankCellVal = self.__matrix[blankRow][blankCol]

        self.__matrix[blankRow][blankCol] = self.__matrix[rowToSwap][colToSwap]
        self.__matrix[rowToSwap][colToSwap] = blankCellVal

        self.__blankPos["row"] = rowToSwap
        self.__blankPos["col"] = colToSwap

    def set_f_value(self, val):
        self.__f_val = val
    
    def get_f_value(self):
        return self.__f_val

    def set_g_value(self, val):
        self.__g_val = val

    def get_g_value(self):
        return self.__g_val

    def printStatus(self):
        self.printNode()
        print()
        print(self.__blankPos)
        print(self.get_f_value)
        print(self.get_g_value)