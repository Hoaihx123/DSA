queue = []
def enqueue():
    data = input('input data:')
    queue.append(data)
    print(queue)
def dequeue():
    if not queue:
        print('queue is empty')
    else:
        queue.pop(0)
        print(queue)
def peek():
    if not queue:
        print('queue is empty')
    else:
        print(queue[0])
while 1:
    print('Choice:\n 1. enqueue\n 2. dequeue\n 3. peek\n 4. quit')
    c = int(input("c="))
    if c==1:
        enqueue()
    elif c==2:
        dequeue()
    elif c==3:
        peek()
    else:
        break

