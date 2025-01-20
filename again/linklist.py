"""this is link list"""
class Node():
    """data node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList():
    """link list"""
    def __init__(self):
        self.count = 0
        self.head = None

    def insert_last(self, data):
        """insert data"""   
        pNew = Node(data)
        pointer = self.head
        if not pointer:
            self.head = pNew
            return

        while pointer.next:
            pointer = pointer.next

        pointer.next = pNew

    def insert_front(self, data):
        """insert front"""
        pNew = Node(data)
        if not self.head:
            self.head = pNew
            return

        pNew.next = self.head
        self.head = pNew

    def is_empty(self):
        """is empthy"""
        return not self.head

    def traverse(self):
        """traverse"""
        if self.is_empty():
            print("the link list is empthy")
        else:
            pointer = self.head
            while pointer:
                print(pointer.data, end=" || ")
                pointer = pointer.next

    def delete(self, data):
        """delete"""
        if self.is_empty():
            print(f"{data} not exist in the link list")
            return

        prev = None
        pointer = self.head
        if pointer.data == data:
            self.head = pointer.next
            return

        while pointer:
            if pointer.data == data:
                prev.next = pointer.next
            prev = pointer
            pointer = pointer.next

        if not pointer:
            print(f"{data} not exist in the link list")

def main():
    """main"""
    txt = ""
    link_list = LinkList()
    while True:
        txt = input()
        if txt == "end" or txt == "End":
            break
        meth, data = txt.split(":")
        match meth:
            case "l":
                link_list.insert_last(data)
            case "f":
                link_list.insert_front(data)
            case "d":
                link_list.delete(data)
    link_list.traverse()

main()
