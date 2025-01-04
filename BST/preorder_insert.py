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

def main():
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()

main()
