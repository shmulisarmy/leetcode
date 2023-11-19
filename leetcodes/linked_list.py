class link_list:
    def __init__(self, data):
        self.data = data    
        self.next = None

    def insert(self, val):
        if not self.next:
            self.next = link_list(val)

        else:
            self.next.insert(val)

    def trav(self):
        print(self.data)
        if self.next:
            self.next.trav()


    def reverse(self):
        cur_node = self
        next_node = cur_node.next
        while True:
            if not cur_node.next:
                return cur_node
            next_nodes_next_temp = next_node.next
            next_node.next = cur_node
            cur_node = next_node
            next_node = next_nodes_next_temp
                
main = link_list(7)
lst = [1, 4, 7, 4, 9, 2]
for i in lst:
    main.insert(i)
main.trav()
print("")
reverse = main.reverse()

reverse.trav()