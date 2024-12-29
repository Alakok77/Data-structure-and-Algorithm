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

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input().strip())
    mylist.traverse()

main()
