from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
          self.storage.add_to_tail(item)
          self.current = self.storage.tail 
        else:
          if self.current.next is not None:
            # changing the next nodes's value to be the value we wish to add
            self.current.next.value = item 
            # set current to be the next node
            self.current = self.current.next
          else:
              #change head to value
              self.storage.head.value = item
              # set current to head
              self.current = self.storage.head


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.head
        while current_node is not None:
            if current_node.value is not None:
                list_buffer_contents.append(current_node.value)
            current_node = current_node.next
        return list_buffer_contents

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
