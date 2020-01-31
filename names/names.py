import time
import sys

class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next
  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    #New Next is current value, so previous is current, and next is current next
    self.next = ListNode(value, self, current_next)
    #If next exists, current Next's prev needs to links to value we're inserting
    if current_next:
        current_next.prev = self.next
  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
        current_prev.next = self.prev
  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    #If Previous, previous's next now points to this' next, skipping current
    if self.prev:
        self.prev.next = self.next
    #If Next, next's previous now points to this previous, skipping current
    if self.next:
        self.next.prev = self.prev
  """Our doubly-linked list class. It holds references to
  the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0
  def __len__(self):
    return self.length
  """Wraps the given value in a ListNode and inserts it 
  as the new head of the list. Don't forget to handle 
  the old head node's previous pointer accordingly."""
  def add_to_head(self, value):
    if self.head:
        current_head = self.head
        #insert value before current head, so currentHead is connected to new head
        current_head.insert_before(value)
        #make head equal to head's previous value
        self.head = current_head.prev
    else:
        self.head = ListNode(value)
        self.tail = self.head   
    self.length += 1
  """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""
  def remove_from_head(self):
    current_head = self.head
    if current_head is None:
        return None
    #Reassigning new head
    if current_head.next is not None:
        self.head = current_head.next
    else:
        #Only 1 item, so both are None
        self.head = None
        self.tail = None
    self.length -= 1
    return current_head.value
  """Wraps the given value in a ListNode and inserts it 
  as the new tail of the list. Don't forget to handle 
  the old tail node's next pointer accordingly."""
  def add_to_tail(self, value):
    #insert after tail
    if self.tail:
        current_tail = self.tail
        current_tail.insert_after(value)
        self.tail = current_tail.next
    else:
        self.tail = ListNode(value)
        self.head = self.tail
    self.length += 1
  """Removes the List's current tail node, making the 
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""
  def remove_from_tail(self):
    if self.tail:
        current_tail = self.tail
        current_tail.delete()
        self.length -= 1
        if current_tail == self.head:
            self.head = None
            self.tail = None
        else:    
            self.tail = current_tail.prev
        return current_tail.value
    else:
        return None
  def contains(self, node):
    #Check if node exists in linked list
    current_node = self.head
    while current_node:
        if current_node == node:
            return True
        current_node = current_node.next
    return False
  def contains_value(self, value):
    current_node = self.head
    while current_node:
        if current_node.value == value:
            return True
        current_node = current_node.next
    return False
  """Removes the input node from its current spot in the 
  List and inserts it as the new head node of the List."""
  def move_to_front(self, node):
    if self.contains(node):
        print(self.length)
        #Add node to front of list
        self.add_to_head(node.value)
        print(self.length)
        #Delete node
        self.delete(node)
        print(self.length)
  """Removes the input node from its current spot in the 
  List and inserts it as the new tail node of the List."""
  def move_to_end(self, node):
    if self.contains(node):
        #add to tail
        self.add_to_tail(node.value)
        #delete
        self.delete(node)
  """Removes a node from the list and handles cases where
  the node was the head or the tail"""
  def delete(self, node):
    if self.contains(node):
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            #Node.delete does not change the length, but the other two do
            node.delete()
            self.length -= 1
  """Returns the highest value currently in the list"""
  def get_max(self):
    max_val = self.head.value
    current = self.head
    while current is not None:
        max_val = max(current.value, max_val)
        current = current.next
    return max_val
  
class Queue:
  def __init__(self):
      # self.size = 0
      # Why is our DLL a good choice to store our elements?
      self.storage = DoublyLinkedList()
  def enqueue(self, value):
      self.storage.add_to_tail(value)
  def dequeue(self):
      return self.storage.remove_from_head()
  def len(self):
      return len(self.storage)

class BinarySearchTree:
  def __init__(self, value):
      self.value = value
      self.frequency = 1
      self.left = None
      self.right = None
  # Insert the given value into the tree
  def insert(self, value):
      queue = Queue()
      queue.enqueue(self)
      while queue.len() > 0:
        current_node = queue.dequeue()
        if value == current_node.value:
            current_node.frequency += 1
        elif value > current_node.value:
          if current_node.right is None:
            current_node.right = BinarySearchTree(value)
          else:
            queue.enqueue(current_node.right)
        elif value < current_node.value:
          if current_node.left is None:
            current_node.left = BinarySearchTree(value)
          else:
            queue.enqueue(current_node.left)
            
  def contains(self, target):
      current_node = self
      while current_node is not None:
        # We only care about the first duplicate in the tree
        if target == current_node.value and current_node.frequency == 1:
          current_node.frequency += 1
          return True
        elif target > current_node.value:
          current_node = current_node.right
        elif target < current_node.value:
          current_node = current_node.left 
      return False
          
start_time = time.time()
f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
duplicates = []

# initialize binary search tree with first value
tree = BinarySearchTree(names_1[0])
for name_1 in names_1[1:]:
    tree.insert(name_1)
for name_2 in names_2:
    if tree.contains(name_2):
        duplicates.append(name_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?