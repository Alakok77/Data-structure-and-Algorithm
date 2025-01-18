"""binary search tree"""
class Node():
    """data node"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    """Binary search tree"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        """insert node"""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        pointer = self.root
        while pointer:
            if data >= pointer.data:
                if pointer.right is None:
                    pointer.right = new_node
                    return
                pointer = pointer.right
            else:
                if pointer.left is None:
                    pointer.left = new_node
                    return
                pointer = pointer.left

    def preorder(self, root = "Start"):
        """preorder"""
        if root == "Start":
            root = self.root

        if root:
            print(f" --> {root.data}", end = "")
            self.preorder(root.left)
            self.preorder(root.right)

        return

    def inorder(self, root = "Start"):
        """inorder"""
        if root == "Start":
            root = self.root

        if root:
            self.inorder(root.left)
            print(f" --> {root.data}", end = "")
            self.inorder(root.right)

        return

    def postorder(self, root = "Start"):
        """postorder"""
        if root == "Start":
            root = self.root

        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(f" --> {root.data}", end = "")

        return

    def traverse(self):
        """traverse"""
        print("Preorder: ", end = "")
        self.preorder()
        print()
        print("Inorder: ", end = "")
        self.inorder()
        print()
        print("Postorder: ", end = "")
        self.postorder()
        print()

    def find_min(self):
        """minimum number"""
        if self.is_empty():
            return "Can't find min"

        pointer = self.root
        while pointer.left:
            pointer = pointer.left
        return pointer.data

    def find_max(self, pointer = "start"):
        """maximum numbrt"""
        if pointer == "start":
            pointer = self.root

        if self.is_empty():
            return "Can't find max"

        while pointer.right:
            pointer = pointer.right
        return pointer.data

    def is_empty(self):
        """is empty"""
        return self.root is None

    def delete(self, data):
        """delete"""
        prev = Node(None)
        pointer = self.root
        while pointer:
            if pointer.data == data:
                break

            if data >= pointer.data:
                prev = pointer
                pointer = pointer.right
            else:
                prev = pointer
                pointer = pointer.left

        if pointer:

            if not pointer.left and not pointer.right:
                if self.root == pointer:
                    self.root = None
                elif prev.left == pointer:
                    prev.left = None
                elif prev.right == pointer:
                    prev.right = None
            elif not pointer.left and pointer.right:
                if self.root == pointer:
                    self.root = pointer.right
                elif prev.left == pointer:
                    prev.left = pointer.right
                elif prev.right == pointer:
                    prev.right = pointer.left
            elif pointer.left and not pointer.right:
                if self.root == pointer:
                    self.root = pointer.left
                elif prev.left == pointer:
                    prev.left = pointer.left
                elif prev.right == pointer:
                    prev.right = pointer.left
            elif pointer.left and pointer.right:
                num = self.delete(self.find_max(pointer.left))
                pointer.data = num
            return pointer.data
        else:
            print(f"Can't delete --{data}-- in tree.")

def main():
    """main function"""
    txt = ""
    bst = BST()
    while True:
        txt = input()
        if txt == "End":
            break
        command, data = txt.split(": ")
        if command == "i":
            bst.insert(int(data))
        elif command == "d":
            bst.delete(int(data))

    bst.traverse()
    print(f"MAX: {bst.find_max()}")
    print(f"MIN: {bst.find_min()}")

main()
