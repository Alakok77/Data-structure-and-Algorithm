"""queue"""
class Node():
    """node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    """queue"""
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, data):
        """enqueue"""
        new = Node(data)
        if self.is_empthy():
            self.front = new
            self.rear = new
            return

        self.rear.next = new
        self.rear = new

    def dequeue(self):
        """dequeue"""
        if self.is_empthy():
            print("The queue is empthy")
            return None

        first = self.front
        self.front = first.next
        return first.data

    def queuRear(self):
        """return queueRear"""
        if self.is_empthy():
            print("Underflow!!!")
            return None

        return self.rear.data

    def queueFront(self):
        """return queueFront"""
        if self.is_empthy():
            print("Underflow!!!")
            return None

        return self.front.data

    def is_empthy(self):
        """boolean"""
        return not self.front

    def show_queue(self):
        """show queue"""
        if self.is_empthy():
            print("The queue is empthy")
            return

        pointer = self.front
        while pointer:
            print(pointer.data, end = " ---> ")
            pointer = pointer.next

    def delete(self, data):
        """delete"""
        if self.is_empthy():
            print("The queue is empthy")
            return None

        prev = None
        pointer = self.front
        while pointer:
            if pointer.data == data:
                break
            prev = pointer
            pointer = pointer.next

        if not pointer:
            print(f"{data} is not exist in the queue")
            return None

        if pointer.data == self.front.data and pointer.data == self.rear.data:
            self.front = None
            self.rear = None
            return

        if pointer.data == self.front.data:
            self.front = self.front.next
            return

        if pointer.data == self.rear.data:
            prev.next = None
            self.rear = prev
            return

        prev.next = pointer.next


def main():
    """main"""
    txt = ""
    q = Queue()
    while True:
        txt = input()
        if txt == "end" or txt == "End":
            break
        meth, data = txt.split(":")
        match meth:
            case "e":
                q.enqueue(data)
            case "d":
                q.dequeue()
            case "r":
                print(q.queuRear())
            case "f":
                print(q.queueFront())
            case "de":
                q.delete(data)
    q.show_queue()

main()
