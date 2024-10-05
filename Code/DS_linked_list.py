
class ListNode:
    """creates ListNode for LinkedList"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def add_after(self, node):
        """adds node after self"""
        tmp = self.next
        self.next = node
        node.prev = self
        node.next = tmp
        if tmp:
            tmp.prev = node
class LinkedList:
    """Creates LinkedList to store line diagram data"""
    def __init__(self):
        self.__ListNode = ListNode
        self.__head = self.__ListNode("Head")
        self.__tail = self.__ListNode("Tail")
        self.__head.add_after(self.__tail)
        self.__list_size = 0

    def add_last(self, val):
        """adds node as last"""
        new_node = ListNode(val)
        self.__tail.prev.add_after(new_node)
        self.__list_size += 1

    def get_size(self):
        """returns size of LinkedList"""
        return self.__list_size

    def get_at_position(self, n):
        """gets node at position n"""
        node = self.__get_at(n)
        return node.value if node else None

    def __get_at(self, n):
        """finds the node at position n"""
        if n < 0 or n >= self.get_size():
            return None
        current_node = self.__head.next
        count = 0
        while current_node:
            if count == n:
                return current_node
            count += 1
            current_node = current_node.next


    def remove_position(self, n):
        """Remove the node at the n'th position."""
        node_at_n = self.__get_at(n)
        prev = node_at_n.prev
        if prev:
            prev.next = node_at_n.next
            if node_at_n.next:
                node_at_n.next.prev = prev
                self.__list_size -= 1

