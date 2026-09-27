class DoublyNode:
    def __init__(self, val = -1, next = None, prev = None, key = -1):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key #ned this for reverse lookup

class LRUCache:

    def __init__(self, capacity: int):

        self.fake_head = DoublyNode()
        self.fake_tail = DoublyNode()

        self.fake_head.next = self.fake_tail
        self.fake_tail.prev = self.fake_head

        self.map = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.map: return -1
        else:
            node = self.map[key]

            if self.fake_head.next is node: return node.val
            else:
                left = node.prev
                right = node.next
                old_front = self.fake_head.next
                self.fake_head.next = node
                node.prev = self.fake_head
                node.next = old_front
                old_front.prev = node
                left.next = right
                right.prev = left

                return node.val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.map:
            #create a new node and make it the front
            new_node = DoublyNode(value, key = key)

            old_front = self.fake_head.next

            self.fake_head.next = new_node
            new_node.prev = self.fake_head

            new_node.next = old_front
            old_front.prev = new_node

            self.map[key] = new_node

            if len(self.map) == (self.capacity + 1):
                old_tail = self.fake_tail.prev

                self.fake_tail.prev = old_tail.prev
                old_tail.prev.next = self.fake_tail

                del self.map[old_tail.key]

        else:
            #update it and move it to the front
            node = self.map[key]
            node.val = value

            if self.fake_head.next is node: return
            else:
                left = node.prev
                right = node.next

                old_front = self.fake_head.next
                self.fake_head.next = node
                node.prev = self.fake_head
                node.next = old_front
                old_front.prev = node
                left.next = right
                right.prev = left


        
