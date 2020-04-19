from random import randint, seed

# Code inspired by the post:
# https://runestone.academy/runestone/books/published/pythonds/Trees/BinaryHeapImplementation.html


# Retrieve top (min in case of MinHeap) --> O(1)
# Retrieve top + delete top --> O(logn)
# Insert element --> O(logn)
# Useful for priority queues, schedulers (where the earliest item is desired), etc

class BinHeap:
    '''Basic implementation of binary heap:
    Binary heap is a list ranging from indexes i=0 to i=len(l)-1 where l
    is the original list.
    Such a list has indexes that indicate the realtionship of father-son

    Given node i:
        Left son: 2i+1
        Right son: 2i+2
        Father: (i-1)//2

    first element index: 0
    last element index: len(l)-1
    larger element with sons: len(l)//2 -1

    This binary heap is programmed as MinHeap, index 0 is the minimum value
    and sons have larger values than the node at i.

    '''
    def __init__(self, heapList = []):
        self._Heapify(heapList)


    def _Heapify(self,l):

        # Larger elemen that has sons
        i = len(l) // 2 -1
        self.__heapList = l[:]
        while (i >= 0):
            # swap with child if child is smaller
            self._percDown(i)
            i = i - 1


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
            if self.__heapList[2*i+1] < self.__heapList[2*i+2]:
                return 2*i + 1
            else:
                return 2*i + 2
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

    # same seed not to change results
    seed(5)
    l = [randint(0,10) for _ in range(8)]

    print("The list to heapify is \n{}".format(l))

    # construct an empty binary heap 
    heap = BinHeap()
    # fill the binary heap element by element
    for elem in l:
        heap.insert(elem)

    print('\nThe binary heap results in the array \n{}'.format(heap.get_heap()))

    print("\nNow we do the same but instead of filling the heap little by litte we heapify the array")
    heap2 = BinHeap(l)
    print("The heapified array is \n{}".format(heap2.get_heap()))


