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
                print("%s -> " % pos.data.strip(), end = "")
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

    def delete(self, data):
        prev = None
        start = self.head
        if start is None:
            print("Cannot delete, %s does not exist." %data)
            return

        if self.head.data == data:
            self.head = start.next
            self.count -= 1
            return

        while start is not None:
            if start.data == data:
                prev.next = start.next
                self.count -= 1
                return
            prev = start
            start = start.next

        print("Cannot delete, %s does not exist." %data)
        
    def delete_node(self, node):
        if self.head is None or node is None:
            print("Cannot delete, node does not exist.")
            return

        if self.head == node:
            self.head = self.head.next
            self.count -= 1
            return

        prev = None
        start = self.head
        while start is not None and start != node:
            prev = start
            start = start.next

        if start is None:
            print("Cannot delete, node does not exist.")
        else:
            prev.next = start.next
            self.count -= 1

def main():
    mylist = SinglyLinkedList()
    result = SinglyLinkedList()
    num = int(input())

    for _ in range(num):
        mylist.insert_last(input())


    while mylist.count > 0:
        last = mylist.head

        if not mylist.count:
            break

        while last.next is not None:
            last = last.next

        result.insert_last(last.data)
        mylist.delete_node(last)

        if not mylist.count:
            break

        result.insert_last(mylist.head.data)
        mylist.delete_node(mylist.head)

        if not mylist.count:
            break

        result.insert_last(mylist.head.data)
        mylist.delete_node(mylist.head)

        if not mylist.count:
            break

        last = mylist.head

        while last.next is not None:
            last = last.next

        result.insert_last(last.data)
        mylist.delete_node(last)

    result.traverse()

main()
