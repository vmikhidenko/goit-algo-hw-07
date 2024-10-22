class Node:
    def __init__(self, value):
        # Ініціалізація вузла з заданим значенням
        self.value = value
        self.left = None   # Лівий дочірній вузол
        self.right = None  # Правий дочірній вузол

def sum_tree(node):
    # Функція для знаходження суми всіх значень у дереві
    if node is None:
        return 0
    # Рекурсивно додаємо значення поточного вузла та значення лівого і правого піддерева
    return node.value + sum_tree(node.left) + sum_tree(node.right)

# Створення дерева
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(5)
root.left.right = Node(12)
root.right.left = Node(18)
root.right.right = Node(25)

# Знаходження суми всіх значень
total_sum = sum_tree(root)
print("Сума всіх значень у дереві:", total_sum)
