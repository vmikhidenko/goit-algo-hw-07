class Node:
    def __init__(self, value):
        # Ініціалізація вузла з заданим значенням
        self.value = value
        self.left = None   # Лівий дочірній вузол
        self.right = None  # Правий дочірній вузол

def find_min(node):
    # Функція для знаходження найменшого значення у дереві
    current = node
    while current.left is not None:
        # Переходимо до лівого дочірнього вузла
        current = current.left
    return current.value

# Створення дерева
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(5)
root.left.right = Node(12)

# Знаходження найменшого значення
min_value = find_min(root)
print("Найменше значення у дереві:", min_value)
