class SingleLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        nval = self.next and self.next.value or None
        return f"{self.value} -> {repr(nval)}"


class SingleLinkedList(object):
    def __init__(self):
        self.begin = None


    def store_first(self, value):
        new_node = SingleLinkedListNode(value)    # Create a new node
        new_node.next = self.begin                # Next for new node becomes the   current head
        self.begin = new_node                     # Head now points to the new node


    def store_last(self, value):
        new_node = SingleLinkedListNode(value)
        if self.begin is None:
            self.begin = new_node
            return
        last = self.begin
        while last.next:
            last = last.next
        last.next = new_node


    def pop_first(self):
        if self.begin is None:
            return "The List is empty"          # if the list is empty return string
        self.begin = self.begin.next            # Otherwise, remove the head by making the next node to new head


    def pop_last(self):
        if self.begin is None:
            return "The List is empty"
        if self.begin.next is None:
            self.begin = None                   # If there's only one node, remove the head by making it None
            return
        temp = self.begin
        while temp.next.next:                   # Otherwise, go to the second-last node
            temp = temp.next
        temp.next = None                        # Remove the last node by setting the next pointer of the second-last node to None


    def show_first(self):
        if self.begin is None:
            return "The List is empty"
        return self.begin.value

    def show_last(self):
        if self.begin is None:
            return "The List is empty"
        temp = self.begin
        while temp.next.next:
            temp = temp.next
        return temp.next.value

    def show_specific(self, target):
        current = self.begin
        while current is not None:
            if current.value == target:
                return True
            current = current.next
        return False

    def count(self):
        temp = self.begin
        count = 0
        while temp:
            temp = temp.next
            count += 1
        return f"Count: {count}"

    def remove(self, target):
        current = self.begin
        while current is not None:
            if current.value == target:
                current.value = None
                return True
            current = current.next
        return False

    def get_all(self):
        temp = self.begin
        while temp:
            print(temp.value, end="\n")
            temp = temp.next


    def unshift(self):
        if self.begin is not None:
            print(f"Unshifted List: {self.begin.value}")
            self.begin = self.begin.next
        else:
            return "The List is empty"