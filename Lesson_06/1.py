class Queue:

    def __init__(self, queue_list):
        self.queue_list = [i for i in queue_list]

    def pop(self):
        if len(self.queue_list) > 0:
            a = self.queue_list[0]
            self.queue_list = self.queue_list[1:]
            return a
        else:
            raise IndexError

    def push(self, new_element):
        self.queue_list.append(new_element)

    def __str__(self) -> str:
        return str(self.queue_list)


test_queue = Queue(["a", "b", "c"])
print(test_queue)
print(test_queue.pop())
test_queue.push("f")
print(test_queue)

