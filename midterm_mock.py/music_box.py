"""music class"""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, item: "Node"):
        if self.head is None:
            self.head = item

        else:

            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next

            item.next = self.head
            pointer.next = item

    def pop(self):
        pointer = self.head
        prev = None
        if self.head is None:
            return

        while pointer.next is not None:
            prev = pointer
            pointer = pointer.next

        prev.next = None
        return pointer

#////////////////////////////////////////////////////////////////////////////////////////////////////////

class Song():
    def __init__(self, name = "", genre = "", duration = 0):
        self.name = name
        self.genre = genre
        self.durations = (int(duration)//60) + (int(duration)%60/100)
        self.next = None

    def show_info(self):
        """show info"""
        return f"{self.name} <|> {self.genre} <|> {self.durations:.2f}"

class Queue():
    """class"""
    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None
        self.remove = None
        self.s = Stack()

    def enqueue(self, item: "Song"):
        """enqueue"""
        if self.front is None:
            self.front = item
            self.rear = item
            self.s.push(item)
            return

        self.rear.next = item
        self.rear = item
        self.size += 1
        self.s.push(item)

    def dequeue(self):
        """dequeue"""
        if self.front is None:
            print("Underflow! Dequeue from an empty queue")
        else:
            pointer = self.front
            self.front = pointer.next
            self.size -= 1
            self.s.push(pointer)
            print(f"Dequeue item: {pointer.show_info()}")
            return pointer

    def peek(self):
        """peek"""
        if self.front is None:
            print("Underflow! peek from an empty queue")
            return
        print(f"Peek item: {self.front.show_info()}")
        return self.front

    def isEmpty(self):
        """isempty"""
        if self.front is None:
            return True
        return False

    def show_Queue(self):
        """show info"""
        if self.isEmpty():
            print("Queue is empty!")
        else:
            pointer = self.front
            i = 1
            while pointer is not None:
                print(f"Queue#{i} {pointer.show_info()}")
                pointer = pointer.next
                i += 1

    def lastSong(self, time):
        """last song"""
        if self.isEmpty():
            print("Nothing here! Please add some song")
        else:
            last = (int(time)//60) + (int(time)%60/100)
            total = 0
            pointer = self.front
            i = 1
            while total + pointer.durations < last:
                if pointer == self.rear:
                    pointer = self.front
                    i = 1
                total += pointer.durations
                pointer = pointer.next
                i += 1
            print(f"Queue#{i} {pointer.show_info()}")

    def removeSong(self, name):
        """remove song"""
        prev = None
        start = self.front
        if self.isEmpty():
            print(f"Can not Delete! {name} is not exist")
            return
        if start.name == name:
            self.front = start.next
            return

        while start.next is not None:
            if start.name == name:
                break
            prev = start
            start = start.next

        if start.next is None and start.name != name:
            print(f"Can not Delete! {name} is not exist")
            return
        prev.next = start.next

    def groupSong(self):
        """group up"""
        jpop = "JPOP: "
        kpop = "KPOP: "
        r_b = "R&B: "
        pointer = self.front

        if pointer is None:
            print("Nothing here! Please add some song")
            return

        while pointer is not None:
            if pointer.genre == "JPOP":
                jpop += f"{pointer.name} | "
            elif pointer.genre == "KPOP":
                kpop += f"{pointer.name} | "
            elif pointer.genre == "R&B":
                r_b += f"{pointer.name} | "
            pointer = pointer.next

        print(jpop.strip("| "))
        print(kpop.strip("| "))
        print(r_b.strip("| "))
        return

    def undo(self):
        print(f"{self.s.pop().data}---------------")

    def rev_queue(self):
        pass

def main():
    """this is main function"""
    q = Queue()
    while (choice := input()) != "End":
        command, data = choice.split(": ")
        match command:
            case "enqueue":
                q.enqueue(Song(*data.split("|")))
            case "dequeue":
                temp = q.dequeue()
                if temp:
                    temp.show_info()
            case "peek":
                temp = q.peek()
                if temp:
                    temp.show_info()
            case "isEmpty":
                print(q.isEmpty())
            case "showQueue":
                q.show_Queue()
            case "lastSong":
                q.lastSong(int(data))
            case "removeSong":
                q.removeSong(data)
            case "groupSong":
                q.groupSong()
            case "undo":
                q.undo()
            # case "rev":
            #     q.rev_queue()
    q.show_Queue()
main()
