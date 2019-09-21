class Stack:
    items = []

    def __init__(self, items = []):
        if items != None and len(items) > 0:
            self.items = items
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1] if len(self.items) > 0 else None