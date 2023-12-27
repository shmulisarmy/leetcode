class min_stack:
    def __init__(self):
        self.list = []
        self.min_stack = []
        
    def insert(self, num):
        if not self.list:
            matp = num
        else:
            matp = min(num, self.min_stack[-1][0])
        self.list.append(num)
        self.min_stack.append((matp, self.list.index(matp)))
    def remove(self):
        if self.list:
            return self.list.pop(self.min_stack.pop()[1])
        
    def __repr__(self) -> str:
        return f"{self.list}\n{self.min_stack}"
           

stack = min_stack()

print(stack)

stack.insert(5)

print(stack)

stack.insert(3)

print(stack)

stack.insert(7)

print(stack)

stack.insert(2)

print(stack)

print(stack.remove())

print(stack)

print(stack.remove())

print(stack)
