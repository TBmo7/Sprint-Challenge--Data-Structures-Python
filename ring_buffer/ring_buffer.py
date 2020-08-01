class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []

    def append(self, item):
        
        if len(storage) is not self.capacity:
            self.storage.append(item)
        


    def get(self):
        return self.storage


newbuffer = RingBuffer(5)

newbuffer.append('a')

print(newbuffer.get())