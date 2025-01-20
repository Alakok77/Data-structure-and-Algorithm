"""stack"""
class Node():
    """stack"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack():
    """stack"""
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, data):
        """push"""
        pNew = Node(data)
        if not self.head:
            self.head = pNew
            return

        pointer = self.head
        while pointer.next:
            pointer = pointer.next
        pointer.next = pNew

    def pop(self):
        """pop"""
        if self.head is None:
            print("Underflow!!!")
            return None
        if not self.head.next:
            pointer = self.head
            self.head = None
            return pointer.data
        prev = None
        pointer = self.head
        while pointer.next:
            prev = pointer
            pointer = pointer.next
        prev.next = None
        return pointer.data

    def getStackTop(self):
        """return stack top"""
        if self.is_empty():
            print("Underflow!!!")

        pointer = self.head
        while pointer.next:
            pointer = pointer.next
        return pointer.data

    def is_empty(self):
        """boolean"""
        return not self.head

    def traverse(self):
        """traverse"""
        if self.is_empty():
            print("the stack is empty")
        else:
            pointer = self.head
            while pointer:
                print(pointer.data, end =" / ")
                pointer = pointer.next

def main():
    """main"""
    txt = ""
    stack = Stack()
    while True:
        txt = input()
        if txt == "end" or txt == "End":
            break
        meth, data = txt.split(":")
        match meth:
            case "push":
                stack.push(data)
            case "pop":
                stack.pop()
            case "top":
                print(stack.getStackTop())
    stack.traverse()

main()
