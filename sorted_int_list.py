class SortedIntList:
    def __init__(self):
        self.sList = []

    def listAdd(self, value):
        lowest = self.__listLowerBound(value)
        self.sList.insert(lowest, value)

    def listRemove(self, value):
        targ = self.__listLowerBound(value)
        if self.sList[targ] != value:
            return
        del self.sList[targ]

    def __listLowerBound(self, value):
        low, high = 0, len(self.sList)
        while low < high:
            mid = (low + high) // 2
            if self.sList[mid] <= value:
                low = mid + 1
            else:
                high = mid
        return low

    def listClear(self):
        self.sList = []

    def __str__(self):
        return str(self.sList)


array = SortedIntList()
array.listAdd(10)
array.listAdd(9)
array.listAdd(12)
array.listAdd(19)
array.listAdd(19)
array.listAdd(21)
print(array)
