import numpy as np
from copy import deepcopy

class node(object):
    BlankVal = 16
    TotalRow = 4
    TotalCol = 4

    def __init__(self, initializedNode = None):
        if (initializedNode == None):
            self.__parentNode = None
            self.__matrix = np.array([  [None, None, None, None],
                                        [None, None, None, None],
                                        [None, None, None, None],
                                        [None, None, None, None]])
            self.__blankPos = { "row" : None, 
                                "col" : None }
            self.__branchLevel = None
            self.__cost = None
        
        else:
            self.__parentNode = initializedNode.__parentNode
            self.__matrix = deepcopy(initializedNode.__matrix)
            self.__blankPos = deepcopy(initializedNode.__blankPos)
            self.__branchLevel = initializedNode.__branchLevel
            self.__cost = initializedNode.__cost

    @classmethod
    def create(cls, parentNode, matrix):
        initNode = node()
        initNode.__parentNode = parentNode
        initNode.__matrix = deepcopy(matrix)

        for row in range (node.TotalRow):
            for col in range (node.TotalCol):
                if (initNode.__matrix[row][col] == node.BlankVal):
                    initNode.__blankPos["row"] = row
                    initNode.__blankPos["col"] = col
                
        if (parentNode):
            initNode.__branchLevel = parentNode.__branchLevel + 1
        else:
            initNode.__branchLevel = 0

        initNode.__calcCost()

        return cls(initNode)

    @classmethod
    def move(cls, parentNode, moveDirection):
        # If valid, creates child node of parentNode with moved-blank-cell position based on moveDirection

        minRow = 0 
        minCol = 0
        maxRow = 3
        maxCol = 3
        if (moveDirection == "RIGHT" and parentNode.__blankPos["col"] != maxCol
            or 
            moveDirection == "LEFT" and parentNode.__blankPos["col"] != minCol
            or
            moveDirection == "UP" and parentNode.__blankPos["row"] != minRow
            or 
            moveDirection == "DOWN" and parentNode.__blankPos["row"] != maxRow):

            childNode = deepcopy(parentNode)
            childNode.__moveBlank(moveDirection)

            # check whether the moved-blank-cell returns the same matrix configuration as parent of parentNode (i.e., two predecessors of childNode)
            childNodeTwoPredecessors = parentNode.__parentNode
            if (not childNodeTwoPredecessors or not childNode.__isEqual(childNodeTwoPredecessors)):
                childNode.__parentNode = parentNode
                childNode.__branchLevel += 1
                childNode.__calcCost()
                return cls(childNode)

        return cls()

    def __moveBlank(self, moveDirection):
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

    def __isEqual(self, otherNode):
        for row in range (node.TotalRow):
            for col in range (node.TotalCol):
                if (self.__matrix[row][col] != otherNode.__matrix[row][col]):
                    return False
    
        return True

    def __calcCost(self):
        f_val = self.__branchLevel

        g_val = 0
        for row in range(node.TotalRow):
            for col in range(node.TotalCol):
                cellValGoal = 1 + col + node.TotalCol * row
                if (self.__matrix[row][col] != self.BlankVal and self.__matrix[row][col] != cellValGoal):
                    g_val += 1
        
        self.__cost = f_val + g_val

    def isGoal(self):
        # Return true if this node/puzzle configuration is the same as desired puzzle configuration
        if (self.__blankPos["row"] == 3 and self.__blankPos["col"] == 3):
            for row in range(self.TotalRow):
                for col in range(self.TotalCol):
                    cellValGoal = 1 + col + self.TotalCol * row
                    if (self.__matrix[row][col] != cellValGoal):
                        return False
            return True

        else:
            return False

    def at(self, row, col):
        return self.__matrix[row][col]

    def isValid(self):
        return self.__matrix.any()

    def getBlank(self, key):
        return self.__blankPos[key]
    
    def getCost(self):
        return self.__cost

    def getParentNode(self):
        return self.__parentNode

    def printNode(self):
        for row in self.__matrix:
            for elmt in row:
                if (elmt == 16):
                    elmt = ' '
                print("{:2}{:2}".format(elmt, ' '), end = '')
            print()
