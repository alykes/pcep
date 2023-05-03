class QueueError(IndexError):  # Choose base class for the new exception.
    pass


class Queue:
    def __init__(self):
       self.__lst = []

    def put(self, elem):
        self.__lst.insert(0, elem)

    def get(self):
        if len(self.__lst) > 0:
            last_element = self.__lst[-1]
            del self.__lst[-1]
            return last_element
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
