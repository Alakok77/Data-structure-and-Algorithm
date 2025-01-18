"""Stack"""
class DataNode():
    """Node of stack"""
    def __init__(self, data):
        """Attribute"""
        self.data = data
        self.next = None

class Stack():
    """stack"""
    def __init__(self):
        """Atrribute"""
        self.size = 0
        self.head =None

    def push_stack(self, data):
        """add data to top of stack"""
        pNew = DataNode(data)
        if self.head is None:
            self.head = pNew
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = pNew
        self.size += 1

    def pop_stack(self):
        """delete and return pop stack"""
        if self.head is None:
            print("Underflow!!!")
            return

        if self.size == 1:
            pointer = self.head.next
            self.head = None
        else:
            prev = DataNode(None)
            pointer = self.head
            while pointer.next is not None:
                prev = pointer
                pointer = pointer.next
            prev.next = None
        self.size -= 1
        return pointer

    def top_stack(self):
        """return top of stack"""
        if self.head is None:
            print("Underflow!!!")
            return

        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next
        return pointer.data

    def is_empty(self):
        """return empty stack"""
        return self.head is None

    def traverse(self):
        """show data in stack"""
        pointer = self.head
        result = ""
        while pointer is not None:
            if pointer.data is not None:
                result += f"{pointer.data} -> "
            pointer = pointer.next
        print(result.strip(" ->"))

    def copy_stack(self):
        """copy stack"""
        copy = Stack()
        temp = Stack()
        while not self.is_empty():
            temp.push_stack(self.pop_stack())

        while not temp.is_empty():
            copy.push_stack(temp.top_stack())
            self.push_stack(temp.top_stack())
            temp.pop_stack()

        copy.traverse()


def main():
    """main function"""
    txt = ""
    stack = Stack()
    while True:
        txt = input()
        if txt == "End":
            break
        command, data = txt.split(": ")
        if command == "push":
            stack.push_stack(data)
        elif command == "pop":
            stack.pop_stack()
        elif command == "top":
            print(stack.top_stack())
        elif command == "empty":
            print(stack.is_empty())
        elif command == "copy":
            stack.copy_stack()
    if stack.is_empty():
        print("The stack is empty")
    else:
        stack.traverse()

main()
