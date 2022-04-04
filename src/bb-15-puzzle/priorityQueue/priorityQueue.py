from node import node
import numpy as np

class nodePriorityQueue:
    def __init__(self):
        self.__heap = []
        self.__heapMaxIdx = -1

    def __parentIdx(self, i):
        return (i - 1 // 2)
    
    def __leftChildIdx(self, i):
        return (2 * i + 1)
    
    def __rightChildIdx(self, i):
        return (2 * i + 2)

    def popMinCostNode(self):
        popped = self.__heap[0]
        self.__heap[0] = self.__heap[self.__heapMaxIdx]
        self.__heap.pop(self.__heapMaxIdx)
        self.__heapMaxIdx -= 1
        
        self.__shiftDown(0)
        return popped

    def insertNode(self, node):
        self.__heapMaxIdx += 1
        self.__heap.append(node)

        self.__shiftUp()

    def __shiftUp(self):
        nodeIdx = self.__heapMaxIdx
        parentIdx = self.__parentIdx(nodeIdx)
        while(nodeIdx > 0 and self.__heap[parentIdx].getCost() > self.__heap[nodeIdx].getCost()):
            self.__swap(nodeIdx, parentIdx)
            nodeIdx = parentIdx
            parentIdx = self.__parentIdx(nodeIdx)

    def __shiftDown(self, currentIdx):
        minCostIdx = currentIdx
        leftChildIdx = self.__leftChildIdx(currentIdx)

        if (leftChildIdx <= self.__heapMaxIdx and 
            self.__heap[minCostIdx].getCost() > self.__heap[leftChildIdx].getCost()):
            minCostIdx = leftChildIdx

        rightChildIdx = self.__rightChildIdx(currentIdx)

        if (rightChildIdx <= self.__heapMaxIdx and 
            self.__heap[minCostIdx].getCost() > self.__heap[rightChildIdx].getCost()):
            minCostIdx = rightChildIdx

        if (currentIdx != minCostIdx):
            self.__swap(currentIdx, minCostIdx)

            self.__shiftDown(minCostIdx)

    def __swap(self, currentIdx, targetIdx):
        currentNode = self.__heap[currentIdx]
        self.__heap[currentIdx] = self.__heap[targetIdx]
        self.__heap[targetIdx] = currentNode