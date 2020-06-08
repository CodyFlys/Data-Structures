class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_Node = Node(value)
        # if there isnt a head set it to the current node.
        if not self.head:
            self.head = new_Node
        else:
            # set the current head to previous_head if there is one.
            previous_head = self.head
            # set the head to the new node.
            self.head = new_Node
            # set the previous head that was in position 0 to position 1 thus pushing it over after adding our new head.
            self.head.set_next(previous_head)

    def add_to_tail(self, value):
        new_Node = Node(value)
        if not self.head:
            self.head = new_Node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            self.tail = current
            current.set_next(new_Node)

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            # value is the current value or aka current node the get_value is currently on.
            value = self.head.get_value()
            # overwriting the self.head
            self.head = self.head.get_next()
            return value

    def remove_from_tail(self):
        # if there is no head, return nothing.
        if not self.head:
            return None
        else:
            # previous head & current head are self.head
            previous = self.head
            current = self.head
            # while the get_next is still not at the tail (aka end)
            while current.get_next() is not None:
                # set "previous" to current node
                previous = current
                current = current.get_next()
            # set the previous node to the new tail since the current tail was removed.
            self.tail = previous
            previous.set_next(None)
            return current.get_value()