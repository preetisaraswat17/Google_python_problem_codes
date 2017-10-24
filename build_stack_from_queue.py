'''Implement a queue using two stacks'''

Stack1 = []
Stack2 = []

# implement enqueue method by using only stacks
# and the append and pop functions
def build_stack(element):
  Stack1.append(element)
  
# implement dequeue method by pushing all elements
# from stack 1 into stack 2, which reverses the order
# and then popping from stack 2
def queue():
  if len(Stack2) == 0:
    if len(Stack1) == 0:
      return 'Cannot dequeue because queue is empty'
    while len(Stack1) > 0:
      p = Stack1.pop()
      Stack2.append(p)
  return Stack2.pop()

build_stack('a')
build_stack('b')
build_stack('c')
print queue()
print queue()
print queue()
