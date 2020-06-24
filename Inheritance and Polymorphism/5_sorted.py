class SortedList(list):
    def append(self, value):
        super().append(value)
        self.sort()
    

sorted = SortedList([3,5,2,9])
sorted.append(4)
print(sorted)