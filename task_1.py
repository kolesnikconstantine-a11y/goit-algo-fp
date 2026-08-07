class Node:
    """Вузол однозв'язного списку."""

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """Однозв'язний список."""

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Вставка елемента на початок списку."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Вставка елемента в кінець списку."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        """Вивід елементів списку."""
        elements = []
        cur = self.head
        while cur:
            elements.append(str(cur.data))
            cur = cur.next
        print(" -> ".join(elements) if elements else "Empty list")


def reverse_linked_list(linked_list: LinkedList) -> None:
    """Реверсує однозв'язний список in-place, змінюючи вказівники вузлів."""
    prev = None
    current = linked_list.head

    while current is not None:
        next_node = current.next  # Зберігаємо наступний вузол
        current.next = prev  # Змінюємо напрямок вказівника
        prev = current  # Зсуваємо prev на поточний вузол
        current = next_node  # Переходимо до наступного вузла

    linked_list.head = prev  # Оновлюємо голову списку


def _split_list(head: Node):
    """Допоміжна функція: розділяє список на дві половини за допомогою методу швидкого та повільного вказівників (Fast & Slow Pointers)."""
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None  # Розриваємо список на дві частини
    return head, middle


def _merge_nodes(left: Node, right: Node) -> Node:
    """Допоміжна функція: зливає два відсортовані списки вузлів у один."""
    dummy = Node()
    tail = dummy

    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left if left else right
    return dummy.next


def merge_sort_nodes(head: Node) -> Node:
    """Рекурсивна функція сортування злиттям для вузлів."""
    if head is None or head.next is None:
        return head

    left_half, right_half = _split_list(head)

    left_sorted = merge_sort_nodes(left_half)
    right_sorted = merge_sort_nodes(right_half)

    return _merge_nodes(left_sorted, right_sorted)


def sort_linked_list(linked_list: LinkedList) -> None:
    """Публічна функція для сортування LinkedList за допомогою Merge Sort."""
    linked_list.head = merge_sort_nodes(linked_list.head)


def merge_two_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    """Приймає два відсортовані списки і повертає новий відсортований LinkedList."""
    merged_list = LinkedList()
    merged_list.head = _merge_nodes(list1.head, list2.head)
    return merged_list


if __name__ == "__main__":
    print("--- 1. Реверсування ---")
    llist = LinkedList()
    for val in [10, 20, 30, 40, 50]:
        llist.insert_at_end(val)

    print("Початковий список:")
    llist.print_list()

    reverse_linked_list(llist)
    print("Реверсований список:")
    llist.print_list()

    print("\n--- 2. Сортування (Merge Sort) ---")
    unsorted_llist = LinkedList()
    for val in [4, 1, 5, 3, 2, 9, 6]:
        unsorted_llist.insert_at_end(val)

    print("Невідсортований список:")
    unsorted_llist.print_list()

    sort_linked_list(unsorted_llist)
    print("Відсортований список:")
    unsorted_llist.print_list()

    print("\n--- 3. Об'єднання двох відсортованих списків ---")
    list_a = LinkedList()
    for val in [2, 3, 7, 9]:
        list_a.insert_at_end(val)

    list_b = LinkedList()
    for val in [1, 4, 5, 8, 10]:
        list_b.insert_at_end(val)

    print("Список A:")
    list_a.print_list()
    print("Список B:")
    list_b.print_list()

    merged = merge_two_sorted_lists(list_a, list_b)
    print("Об'єднаний відсортований список:")
    merged.print_list()