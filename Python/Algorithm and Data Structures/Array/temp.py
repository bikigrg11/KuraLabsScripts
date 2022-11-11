from queue import Queue


ab = [1,2,3,4]

ab.append(7)
ab.insert(0,5)
ab.pop()

queue = Queue()
queue.put(1)
print(queue.empty())

queue.get()

print(ab)