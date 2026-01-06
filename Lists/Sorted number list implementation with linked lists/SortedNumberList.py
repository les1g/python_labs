from Node import Node

class SortedNumberList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, number):
        new_node = Node(number)

        # Case 1: empty list
        if self.head is None:
            self.head = self.tail = new_node
            return

        current = self.head

        # Find first node >= number
        while current and current.get_data() < number:
            current = current.get_next()

        # Case 2: insert at beginning
        if current is self.head:
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node
            return

        # Case 3: insert at end
        if current is None:
            new_node.set_previous(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            return

        # Case 4: insert in middle
        prev = current.get_previous()
        prev.set_next(new_node)
        new_node.set_previous(prev)
        new_node.set_next(current)
        current.set_previous(new_node)

    def remove(self, number):
        current = self.head

        while current:
            if current.get_data() == number:

                # Case 1: removing head
                if current is self.head:
                    self.head = current.get_next()
                    if self.head:
                        self.head.set_previous(None)
                    else:
                        self.tail = None
                    return True

                # Case 2: removing tail
                if current is self.tail:
                    self.tail = current.get_previous()
                    self.tail.set_next(None)
                    return True

                # Case 3: removing middle
                prev = current.get_previous()
                nxt = current.get_next()
                prev.set_next(nxt)
                nxt.set_previous(prev)
                return True

            current = current.get_next()

        return False

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.get_data())
            current = current.get_next()
        return result

    def is_empty(self):
        return self.head is None