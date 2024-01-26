import uuid

from main import draw_tree


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
            # draw_tree(root)
        else:
            root.right = insert(root.right, key)
            # draw_tree(root)
    return root


def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root


def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current


def max_value_node(root):
    if root is None:
        return None
    if root.right is None:
        return root
    return max_value_node(root.right)


def sum_tree(root):
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)

if __name__ == "__main__":
    # Test
    root = Node(5)
    root = insert(root, 1)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
    root = insert(root, 9)
    print('Min value in tree: ', min_value_node(root).val)
    print('Max value in tree: ', max_value_node(root).val)
    print('Sum of tree: ', sum_tree(root))

    draw_tree(root)
    