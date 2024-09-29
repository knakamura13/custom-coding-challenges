def list_to_linkedlist(input_list):
    linked_list = LinkedList()

    for item in input_list:
        linked_list.append(item)

    return linked_list


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def to_list(self):
        result = []
        current_node = self.head

        while current_node:
            result.append(current_node.data)
            current_node = current_node.next

        return result
