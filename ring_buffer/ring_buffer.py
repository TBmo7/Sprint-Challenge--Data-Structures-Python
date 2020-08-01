class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.length = 0


    def append(self, item):
        
        
        lengthverify = False
        
        

        if len(self.storage) is not self.capacity:
            self.storage.append(item)
            lengthverify = True
        else:
            #self.storage[lengthcounter].append(item)
            #self.storage.insert(self.length ,item)
            self.storage[self.length] = item
            lengthverify = True
        if lengthverify is True:
            self.length += 1
            if self.length == self.capacity:
                self.length = 0
        


    def get(self):
        return self.storage


newbuffer = RingBuffer(5)

newbuffer.append('a')
newbuffer.append('b')
newbuffer.append('c')
newbuffer.append('d')
newbuffer.append('e')

print("TEST = a,b,c,d,e should be the same below")

print(newbuffer.get())

print("break-------")
print("inserting new element")

newbuffer.append('1')
newbuffer.append('2')
newbuffer.append('3')
print(newbuffer.get())
