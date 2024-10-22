class Node:
    def __init__(self, value):
        # Ініціалізація вузла з заданим значенням
        self.value = value
        self.left = None   # Лівий дочірній вузол
        self.right = None  # Правий дочірній вузол

def find_max(node):
    # Функція для знаходження найбільшого значення у дереві
    current = node
    while current.right is not None:
        # Переходимо до правого дочірнього вузла
        current = current.right
    return current.value

# Створення дерева
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(18)
root.right.right = Node(25)

# Знаходження найбільшого значення
max_value = find_max(root)
print("Найбільше значення у дереві:", max_value)
