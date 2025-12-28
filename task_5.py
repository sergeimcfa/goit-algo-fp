import collections

# Генеруємо градієнт кольорів (від темного до світлого)
def generate_color(index, total_steps):
    # Базовий колір (наприклад, відтінки синього/фіолетового)
    # Змінюємо інтенсивність RGB
    r = int(18 + (200 * index / total_steps)) 
    g = int(150 + (100 * index / total_steps))
    b = 240
    return f'#{r:02x}{g:02x}{b:02x}'

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

# Обхід у глибину (DFS) з використанням стека
def visualize_dfs(root):
    if not root:
        return
    
    total_nodes = count_nodes(root)
    stack = [root]
    visited_order = []
    
    while stack:
        node = stack.pop()
        visited_order.append(node)
        # Додаємо правий, потім лівий, щоб лівий був оброблений першим (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    # Присвоюємо кольори
    for i, node in enumerate(visited_order):
        node.color = generate_color(i, total_nodes)
        
    print("Візуалізація DFS:")
    draw_tree(root)

# Обхід у ширину (BFS) з використанням черги
def visualize_bfs(root):
    if not root:
        return
        
    total_nodes = count_nodes(root)
    queue = collections.deque([root])
    visited_order = []
    
    while queue:
        node = queue.popleft()
        visited_order.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    # Присвоюємо кольори (можна використати іншу палітру для різноманіття)
    for i, node in enumerate(visited_order):
        # Відтінки оранжевого
        r = 255
        g = int(100 + (155 * i / total_nodes))
        b = int(0 + (100 * i / total_nodes))
        node.color = f'#{r:02x}{g:02x}{b:02x}'

    print("Візуалізація BFS:")
    draw_tree(root)

# Побудова дерева для тесту
root_tree = Node(0)
root_tree.left = Node(4)
root_tree.left.left = Node(5)
root_tree.left.right = Node(10)
root_tree.right = Node(1)
root_tree.right.left = Node(3)

# Запуск візуалізації
# Примітка: кольори оновлюються "на місці", тому запускаємо по черзі
# Щоб скинути кольори, можна перестворити дерево, але тут ми просто перезапишемо їх
visualize_dfs(root_tree)
visualize_bfs(root_tree)
