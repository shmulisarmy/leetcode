class Linked_list:
    removed_indexs = []
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, value):
        node = self
        while node.next:
            node = node.next

        node.next = Linked_list(value)

    def insert_all(self, *args):
        for arg in args:
            self.insert(arg)

    def trav(self):
        node = self
        while node.next:
            print(node.value, end = ' ')
            node = node.next
        print(node.value)

    def remove(self, k):
        p1 = self
        p2 = self

        for i in range(k):
            p2 = p2.next

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        p1.next = p1.next.next

        Linked_list.removed_indexs.append(k)
            




main = Linked_list(3)

main.insert_all(5,3,2,6,7,8,9)
main.trav()
print(f"")
main.remove(5)
print(f"")
main.trav()