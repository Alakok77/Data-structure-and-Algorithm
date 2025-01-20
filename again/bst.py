"""binary search tree"""
class Node():
    """node"""
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BST():
    """binary search tree"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        """insert"""
        node = Node(data)
        if self.is_empty():
            self.root = node
            return

        pointer = self.root
        while True:
            if data >= pointer.data:
                if not pointer.right:
                    pointer.right = node
                    return
                pointer = pointer.right
            else:
                if not pointer.left:
                    pointer.left = node
                    return
                pointer = pointer.left

    def find_min(self):
        """return min"""
        if self.is_empty():
            print("BST is empthy.")
            return None

        pointer = self.root
        while pointer.left:
            pointer = pointer.left

        return pointer.data

    def find_max(self, root = "start"):
        """return max"""
        if root == "start":
            root = self.root

        if self.is_empty():
            print("BST is empthy")
            return None

        while root.right:
            root = root.right

        return root.data

    def is_empty(self):
        """is empthy"""
        return not self.root

    def preorder(self, root = "start"):
        """preorder"""
        if root == "start":
            root = self.root

        if root:
            print(f" --> {root.data}", end = "")
            self.preorder(root.left)
            self.preorder(root.right)

        return

    def inorder(self, root = "start"):
        """inorder"""
        if root == "start":
            root = self.root


        if root:
            self.inorder(root.left)
            print(root.data, end = " --> ")
            self.inorder(root.right)

        return

    def postorder(self, root = "start"):
        """postorder"""
        if root == "start":
            root = self.root

        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end = " --> ")

        return

    def traverse(self):
        """traverse"""
        if self.is_empty():
            print("BST is empthy")
            return None

        print("Preorder: ", end = "")
        self.preorder()
        print()

        print("Inorder: ", end = "")
        self.inorder()
        print()
    
        print("Postorder: ", end = "")
        self.postorder()
        print()

    def show_info(self):
        """show info"""
        if self.is_empty():
            print("BST is empthy")
            return None

        print("MAX: ", end = "")
        print(self.find_max())
        print("MIN: ", end = "")
        print(self.find_min())

    def delete(self, data):
        """delete"""
        if self.is_empty():
            print("BST is empthy")
            return

        prev = None
        target = self.root

        while target:
            if target.data == data:
                break
            
            if data >= target.data:
                prev = target
                target = target.right
            else:
                prev = target
                target = target.left

        # no child
        if not target.left and not target.right:
            if self.root == target:
                self.root = None
            elif prev.left == target:
                prev.left = None
            elif prev.right == target:
                prev.right = None

        # left child
        elif target.left and not target.right:
            if self.root == target:
                self.root = target.left
            elif prev.left == target:
                prev.left = target.left
            elif prev.right == target:
                prev.right = target.left

        # right child
        elif not target.left and target.right:
            if self.root == target:
                self.root = target.right
            elif prev.left == target:
                prev.left = target.right
            elif prev.right == target:
                prev.right = target.right

        # have two child
        elif target.left and target.right:
            number = self.delete(self.find_max(target.left))
            target.data = number

        return data

def main():
    """main"""
    txt = ""
    bst = BST()
    while True:
        txt = input()
        if txt == "end" or txt == "End":
            break
        meth, data = txt.split(":")
        match meth:
            case "i":
                bst.insert(int(data))
            case "d":
                bst.delete(int(data))
    bst.traverse()
    bst.show_info()

main()
main()
