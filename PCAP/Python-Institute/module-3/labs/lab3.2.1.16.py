class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
       self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if len(self.__queue) > 0:
            last_element = self.__queue[-1]
            del self.__queue[-1]
            return last_element
        else:
            raise QueueError


class SuperQueue(Queue):
    def __init__(self):
       Queue.__init__(self)
    # The constructor must be specified for the SuperClass, refer to the link below
    # Refer to https://edube.org/learn/pe-2/a-short-journey-from-procedural-to-object-approach-57

    def isempty(self):
        # if len(self.queue) > 0:
        #     empty = False
        # else:
        #     empty = True
        # return empty
        return len(self.__queue) == 0


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
