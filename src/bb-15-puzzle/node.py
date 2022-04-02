import numpy as np
from copy import copy

class node:
    def __init__(self, initializedNode = None):
        self.__matrix = np.array([ [0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 0],
                                   [0, 0, 0, 0]  ])

        self.__blankPos = { "row" : 0, 
                            "col" : 0 }
        self.__f_val = 0
        self.__g_val = 0
    
    @classmethod
    def move(cls, parentNode, moveDirection):
        childNode = copy(parentNode)
        childNode.__swapBlank(moveDirection)

        return cls(childNode)

    def __swapBlank(self, moveDirection):
        # Initializing variables
        blankRow = self.__blankPos["row"]
        blankCol = self.__blankPos["col"]
        rowToSwap = blankRow
        colToSwap = blankCol

        if (moveDirection == "RIGHT"):
            colToSwap += 1

        elif (moveDirection == "LEFT"):
            colToSwap -= 1

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