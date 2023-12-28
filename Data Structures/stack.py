class StackUseList:
    stack = []
    def push(self):
        data = input('Input data:')
        self.stack.append(data)
        print(self.stack)
    def pop(self):
        if not self.stack:
            print('stack is empty')
        else:
            self.stack.pop()
            print(self.stack)
    def top(self):
        if not self.stack:
            print('stack is empty')
        else:
            print(self.stack[-1])
    def is_empty(self):
        if not self.stack:
            print('stack is empty')
        else:
            print('stack is not empty')
    def test(self):
        while 1:
            print('Choice option:\n 1. push\n 2. pop\n 3. top\n 4. is empty\n another key for quit')
            option = int(input('Your number:'))
            if option == 1:
                self.push()
            elif option == 2:
                self.pop()
            elif option == 3:
                self.top()
            elif option == 4:
                self.is_empty()
            else:
                break

s = StackUseList()
s.test()
