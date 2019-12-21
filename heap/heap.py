class BinHeap:
    def __init__(self):
        self.__heapList = []

    #@classmethod
    #def f(cls, filename):
    #    return cls(data)

    def get_heap(self):
        return self.__heapList

    def _percUp(self,i):
        # Percolate element i upwards following the tree

        # while there is a parent node of i
        while (i-1) // 2 >= 0:
            # if current element in i is smaller than its parent, swap
            if self.__heapList[i] < self.__heapList[(i-1)//2]:
                tmp = self.__heapList[(i-1) // 2]
                self.__heapList[(i-1) // 2] = self.__heapList[i]
                self.__heapList[i] = tmp
            # Now change to the parent index and repeat
            i = (i-1) // 2

    def insert(self,k):
        # Insert an element k to the binary heap
        self.__heapList.append(k)
        self._percUp(len(self.__heapList)-1)

    def _minChild(self,i):
        # given an index i smaller than len(self.heapList)-1, give 
        # the index of the smallest child
        if 2*i + 1 > len(self.__heapList)-1:
            return None
        elif 2*i + 2 < len(self.__heapList):
            if self.__heapList[i*2+1] < self.__heapList[i*2+2]:
                return i * 2 + 1
            else:
                return i * 2 + 2
        else:
            return 2*i +1

    def _percDown(self,i):
        # Percolate element i downwards following the three

        # while there is at least one son
        while (2*i + 1) <= len(self.__heapList)-1:
            mc = self._minChild(i)
            if self.__heapList[i] > self.__heapList[mc]:
                tmp = self.__heapList[i]
                self.__heapList[i] = self.__heapList[mc]
                self.__heapList[mc] = tmp
            i = mc

    def delMin(self):
        retval = self.__heapList[0]
        self.__heapList[0] = self.__heapList[len(self.__heapList)-1]
        self.__heapList.pop()
        self._percDown(0)
        return retval
            

    

if __name__ == '__main__':
    heap = BinHeap()

    l = [9,6,10,4,3,20,1]

    for elem in l:
        heap.insert(elem)


    print(heap.get_heap())


