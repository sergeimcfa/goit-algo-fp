class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    # Реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортування вставками
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sorted_insert(self, head_ref, new_node):
        if head_ref is None or head_ref.data >= new_node.data:
            new_node.next = head_ref
            return new_node
        else:
            current = head_ref
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return head_ref

# Функція об'єднання двох відсортованих списків
def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy
    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Перевірка
if __name__ == "__main__":
    ll1 = LinkedList()
    [ll1.insert_at_end(x) for x in [3, 1, 5]]
    print("Список 1:")
    ll1.print_list()
    
    ll1.reverse()
    print("Реверс списку 1:")
    ll1.print_list()
    
    ll1.insertion_sort()
    print("Відсортований список 1:")
    ll1.print_list()

    ll2 = LinkedList()
    [ll2.insert_at_end(x) for x in [4, 2, 6]]
    ll2.insertion_sort()
    print("Відсортований список 2:")
    ll2.print_list()

    merged = merge_sorted_lists(ll1, ll2)
    print("Об'єднаний список:")
    merged.print_list()
