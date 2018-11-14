class Array:

    def __new__(cls, numItems, spacing):
            cls.length = numItems
            cls.spacing = spacing
            cls.create(cls)
            return cls

    def create(cls):
        cls.list = [i for i in range(cls.spacing, cls.length*cls.spacing + 1, cls.spacing)]

    def toTwenty(cls):
        return Array(cls, 20, 1)

    def toForty(cls):
        return Array(cls, 20, 2)

    def toOneThousand(cls):
        return Array(cls, 100, 10)

    
class binarySearch:
    from binarySearch import Array

    def __init__(self, numItems, spacing):
        self.binarySearch = Array(numItems, spacing)
        self.length = self.binarySearch.length
        self.list = self.binarySearch.list

    def __getitem__(self, position):
        return self.list[position]

    def search(self, toFind):
        self.list.sort()
        min = 0
        max = len(self.list) - 1
        counter = 0
        ## loop through list dividing it into halves until index is returned
        while True:
            if max < min:
                self.count = counter
                self.index = -1
                return {"count": self.count, "index": self.index}
            m = (min + max) // 2 ##Find the value at the centre of list
            ## Conditional to choose side with most likelyhood of containing the number
            ##Increment counter with every loop through
            if self.list[m] < toFind:
                min = m + 1
            elif self.list[m] > toFind:
                max = m - 1
            else:
                self.count = counter
                self.index = m
                return {"count": self.count, "index": self.index}
            counter = counter + 1