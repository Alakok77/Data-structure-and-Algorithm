class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        pNew = BSTNode(data)
        if self.root is None:
            self.root = pNew
        else:
            pointer = self.root
            while True:
                if data < pointer.data:
                    if pointer.left is None:
                        pointer.left = pNew
                        break
                    pointer = pointer.left
                else:
                    if pointer.right is None:
                        pointer.right = pNew
                        break
                    pointer = pointer.right

    def is_empty(self):
        return self.root is None

    def preorder(self, start = None):
        if start == None:
            start = self.root

        if start.data != None:
            print("-> %s " % start.data, end = "")
            if start.left != None:
                self.preorder(start.left)

            if start.right != None:
                self.preorder(start.right)

        return

    def inorder(self, start = None):
        if start == None:
            start = self.root

        if start.data != None:
            if start.left != None:
                self.inorder(start.left)

            print("-> %s " % start.data, end = "")

            if start.right != None:
                self.inorder(start.right)

        return

    def postorder(self, start = None):
        if start == None:
            start = self.root

        if start.data != None:
            if start.left != None:
                self.postorder(start.left)

            if start.right != None:
                self.postorder(start.right)

            print("-> %s " % start.data, end = "")

        return

    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
        else:
            print("Preorder: ", end = "")
            self.preorder()
            print("")
            print("Inorder: ", end = "")
            self.inorder()
            print("")
            print("Postorder: ", end = "")
            self.postorder()
            print("")

    def find_min(self):
        start = self.root
        while start.left != None:
            start = start.left

        return start.data

    def find_max(self):
        start = self.root
        while start.right != None:
            start = start.right

        return start.data

    def delete(self, data):
        prev = None
        start = self.root
        while start != None and start.data != data:
            prev = start
            if data < start.data:
                start = start.left
            else:
                start = start.right

        if start is None:
            print("Delete Error, %s is not found in Binary Search Tree." %data)
            return None

        if start.left is None and start.right is None:
            if start == self.root:
                self.root = None
            elif start == prev.left:
                prev.left = None
            else:
                prev.right = None

        elif start.left != None and start.right is None:
            if start == self.root:
                self.root = start.left
            elif start == prev.left:
                prev.left = start.left
            else:
                prev.right = start.left

        elif start.left is None and start.right != None:
            if start == self.root:
                self.root = start.right
            elif start == prev.left:
                prev.left = start.right
            else:
                prev.right = start.right

        else:
            parent = start
            child = start.left

            while child.right != None:
                parent = child
                child = child.right

            start.data = child.data

            if parent.left == child:
                parent.left = child.left
            else:
                parent.right = child.left

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()
