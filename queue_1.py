queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Peek
frontElement = queue[1]
print("Peek: ", frontElement)

# Dequeue
poppedElement = queue.pop()
print("Dequeue: ", poppedElement)

print("Queue after Dequeue: ", queue)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))