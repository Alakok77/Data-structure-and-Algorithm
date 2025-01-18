"""link list"""
class Node():
    """Node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkList():
    """link list"""
    def __init__(self):
        self.count = 0
        self.head = None

    def insert_last(self, data):
        """insert_last data"""
        self.count += 1
        pNew = Node(data)
        if self.head is None:
            self.head = pNew
            return

        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next

        pointer.next = pNew

    def insert_front(self, data):
        """insert front of link list"""
        self.count += 1
        pNew = Node(data)
        if self.head is None:
            self.head = pNew
            return

        pNew.next = self.head
        self.head = pNew

    def traverse(self):
        """show data"""
        if self.is_empty():
            print("Link list is empty")
        else:
            pointer = self.head
            result = ""
            while pointer is not None:
                result += f"{pointer.data} --> "
                pointer = pointer.next
            print(result.strip(" --> "))

    def is_empty(self):
        """is empty"""
        return self.head is None

    def delete(self, target):
        """delete"""
        if self.head is None:
            print(f"Don't have --{target}-- in link list")
            return

        if self.head.data == target:
            print(f"Delete: {self.head.data}")
            self.head = None
            return

        prev = None
        pointer = self.head
        while pointer is not None and pointer.data != target:
            prev = pointer
            pointer = pointer.next

        if pointer is None:
            print(f"Don't have --{target}-- in link list")
            return


        prev.next = pointer.next
        print(f"Delete: {pointer.data}")

def main():
    """main function"""
    link_list = LinkList()
    txt = ""
    while True:
        txt = input()
        if txt == "End":
            break
        command, data = txt.split(": ")
        if command == "L":
            link_list.insert_last(data)
        elif command == "F":
            link_list.insert_front(data)
        elif command == "D":
            link_list.delete(data)
    link_list.traverse()

main()
