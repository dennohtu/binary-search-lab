class Array:

    def __new__(cls, numItems, spacing):
            cls.length = numItems
            cls.spacing = spacing
            cls.create(cls)
            return cls

    def create(cls):
        cls.list = [i for i in range(cls.spacing, cls.length*cls.spacing + 1, cls.spacing)]

    def search(cls, toFind):
        min = 0
        max = len(cls.list)
        counter = 0
        ## loop through list dividing it into halves until index is returned
        while True:
            if toFind > max-1:
                cls.count = counter
                cls.index = -1
                return cls
            m = (min + max) // 2 ##Find the value at the centre of list
            ## Conditional to choose side with most likelyhood of containing the number
            ##Increment counter with every loop through
            if cls.list[m] < toFind:
                min = m + 1
                counter = counter + 1
            elif cls.list[m] > toFind:
                max = m - 1
                counter = counter + 1
            else:
                cls.count = counter
                cls.index = m
                return cls

class binarySearch:
    from binarySearch import Array

    def __init__(self, numItems = None, spacing = None):
        self.obj = Array(numItems, spacing)
        self.list = self.obj.list
    
    ##toTwenty() returns [1, 2, 3 . . . 20]
    def toTwenty(self):
        return binarySearch(20, 1).list

    ##toForty() returns [2, 4, 6 . . . 40]
    def toForty(self):
        return binarySearch(20, 2).list

    ##toOneThousand() returns [10, 20, 30 . . . 1000]
    def toOneThousand(self):
        return binarySearch(100, 10).list

    ##Search
    def search(self, toFind):
        srch = self.obj.search(self, toFind)

a = binarySearch(20,1)
print(a.toOneThousand())