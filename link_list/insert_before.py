class DataNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        pos = self.head
        if pos is None:
            print("This is an empty list.")
            return
        while pos is not None:
            if pos.next is None:
                print(pos.data)
            else:
                print("%s -> " % pos.data, end = "")
            pos = pos.next

    def insert_last(self, data):
        self.count += 1
        pNew = DataNode(data)
        pos = self.head
        if self.head is None:
            self.head = pNew
        else:
            while pos.next is not None:
                pos = pos.next
            pos.next = pNew

    def insert_front(self, data):
        self.count += 1
        pNew = DataNode(data)
        if self.head is None:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew

    def insert_before(self, node, data):
        pNew = DataNode(data)
        if self.head is None:
            print("Cannot insert, %s does not exist." % node)
            return

        if self.head.data == node:
            pNew.next = self.head
            self.head = pNew
            self.count += 1
            return

        prev = None
        start = self.head

        while start is not None and start.data != node:
            prev = start
            start = start.next

        if start is None:
            print("Cannot insert, %s does not exist." % node)
        else:
            prev.next = pNew
            pNew.next = start
            self.count += 1

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #     mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

main()
