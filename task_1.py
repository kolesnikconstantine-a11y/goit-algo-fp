from typing import Optional


class Node:
    """Node of a singly linked list."""

    def __init__(self, data=None):
        self.data = data
        self.next: Optional["Node"] = None


class LinkedList:
    """Singly linked list."""

    def __init__(self):
        self.head: Optional[Node] = None

    def insert_at_beginning(self, data) -> None:
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data) -> None:
        """Insert a new node at the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def print_list(self) -> None:
        """Print all elements of the list."""
        elements = []
        current = self.head

        while current is not None:
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements) if elements else "Empty list")


def reverse_linked_list(linked_list: LinkedList) -> None:
    """
    Reverse the linked list in-place by changing node pointers.
    """
    previous = None
    current = linked_list.head

    while current is not None:
        next_node = current.next

        # Reverse the current node's pointer
        current.next = previous

        # Move pointers one position forward
        previous = current
        current = next_node

    # Update the head to the new first node
    linked_list.head = previous


def split_list(head: Optional[Node]) -> tuple[Optional[Node], Optional[Node]]:
    """
    Split the linked list into two halves using
    the fast and slow pointer technique.
    """
    if head is None or head.next is None:
        return head, None

    slow = head
    fast = head.next

    # Move slow by one step and fast by two steps
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    middle = slow.next
    slow.next = None

    return head, middle


def merge_nodes(
    left: Optional[Node],
    right: Optional[Node]
) -> Optional[Node]:
    """
    Merge two sorted linked lists into one sorted list.
    """
    dummy = Node()
    tail = dummy

    while left is not None and right is not None:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next

        tail = tail.next

    # Attach the remaining nodes
    tail.next = left if left is not None else right

    return dummy.next


def merge_sort_nodes(head: Optional[Node]) -> Optional[Node]:
    """
    Recursively sort linked list nodes using Merge Sort.
    """
    if head is None or head.next is None:
        return head

    # Split the list into two halves
    left, right = split_list(head)

    # Recursively sort both halves
    left = merge_sort_nodes(left)
    right = merge_sort_nodes(right)

    # Merge the sorted halves
    return merge_nodes(left, right)


def sort_linked_list(linked_list: LinkedList) -> None:
    """Sort a LinkedList using the Merge Sort algorithm."""
    linked_list.head = merge_sort_nodes(linked_list.head)


def merge_two_sorted_lists(
    list1: LinkedList,
    list2: LinkedList
) -> LinkedList:
    """
    Merge two sorted linked lists into a new LinkedList.
    """
    merged_list = LinkedList()
    merged_list.head = merge_nodes(list1.head, list2.head)

    return merged_list


def create_list(values: list) -> LinkedList:
    """Create a linked list from a list of values."""
    linked_list = LinkedList()

    for value in values:
        linked_list.insert_at_end(value)

    return linked_list


if __name__ == "__main__":

    # 1. Reverse a linked list
    print("--- 1. Reversing ---")

    linked_list = create_list([10, 20, 30, 40, 50])

    print("Original list:")
    linked_list.print_list()

    reverse_linked_list(linked_list)

    print("Reversed list:")
    linked_list.print_list()

    # 2. Sort a linked list using Merge Sort
    print("\n--- 2. Sorting with Merge Sort ---")

    unsorted_list = create_list([4, 1, 5, 3, 2, 9, 6])

    print("Unsorted list:")
    unsorted_list.print_list()

    sort_linked_list(unsorted_list)

    print("Sorted list:")
    unsorted_list.print_list()

    # 3. Merge two sorted linked lists
    print("\n--- 3. Merging Two Sorted Lists ---")

    list_a = create_list([2, 3, 7, 9])
    list_b = create_list([1, 4, 5, 8, 10])

    print("List A:")
    list_a.print_list()

    print("List B:")
    list_b.print_list()

    merged = merge_two_sorted_lists(list_a, list_b)

    print("Merged sorted list:")
    merged.print_list()