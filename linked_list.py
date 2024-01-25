# Node creation
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # inserts at beginning
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    #inserts at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)    

    #inserts a list of values at the end
    def insert_values(self, data_list):
        if self.head == None:
            for data in data_list:
                self.insert_at_end(data)

        itr = self.head
        while itr.next:
            itr = itr.next

        for data in data_list:
            self.insert_at_end(data)  

    #insert value at a given index
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")
          
        if index == 0:
            self.head = Node(data, None)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                # temp = itr.next
                # itr.next = Node(data, temp)
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    #inserts a value after a specified data
    def insert_after_value(self, data_after, data_to_insert):
        count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    #remove value from a given index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1    

    #remove specific value
    def remove_by_value(self, data):
        count = 0
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1 

    #prints linked list
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        
        print(llstr)

    #finds the length of the linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    
ll = LinkedList()
ll.insert_at_beginning(100)
ll.insert_at_beginning(89)
ll.insert_at_end(29)
ll.insert_values([92, 91, 89, 72, 55])
ll.remove_at(5)
ll.print()
ll.insert_at(5, 77)
ll.print()
ll.insert_after_value(92, 93)
ll.print()
ll.remove_by_value(91)
ll.print()
print("Length:", ll.get_length())

