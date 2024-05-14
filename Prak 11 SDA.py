class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self.min_value_node(node.left)

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def tree(self, root, indent="", last='updown'):
        if root != None:
            print(indent, end='')
            if last == 'updown': 
                print('R----', end='')
                indent += "     "
            elif last == 'right':
                print('R----', end='')
                indent += "|    "
            else:
                print('L----', end='')
                indent += "     "
            print(root.key)
            self.tree(root.left, indent, 'left')
            self.tree(root.right, indent, 'right')

def main():
    print("Nama: Rangga Aditya Pradana")
    print("NIM: 064002300026")

    avl_tree = AVLTree()
    root = None

    initial_values = [16, 5, 22, 4, 64, 26]
    for value in initial_values:
        root = avl_tree.insert(root, value)

    print("\nAVL Tree saat ini:")
    avl_tree.tree(root)

    while True:
        print("\nOPERASI AVL TREE :")
        print("1. MASUKKAN NODE")
        print("2. HAPUS NODE")
        print("3. TUTUP")

        choice = input("Silahkan pilih: ")

        if choice == '1':
            key = int(input("Masukan nilai yang mau diinsert: "))
            root = avl_tree.insert(root, key)
        elif choice == '2':
            key = int(input("Masukan nilai yang ingin dihapus: "))
            root = avl_tree.delete(root, key)
        elif choice == '3':
            print("\nAVL Tree saat ini:")
            avl_tree.tree(root)
            break
        else:
            print("Pilihan salah, silahkan coba lagi")

        print("\nAVL Tree saat ini:")
        avl_tree.tree(root)

if __name__ == "__main__":
    main()
