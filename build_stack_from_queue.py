'''Implement a queue using two stacks'''

Stack1 = []
Stack2 = []

# build a stack using append function
def build_stack(element):
  Stack1.append(element)
  
# push all elements from stack 1 into stack 2, to revers the order
def queue():
  if len(Stack2) == 0:
    if len(Stack1) == 0:
      return 'Cannot dequeue because queue is empty'
    while len(Stack1) > 0: # pop from stack 2
      p = Stack1.pop()
      Stack2.append(p)
  return Stack2.pop()

build_stack('a')
build_stack('b')
build_stack('c')
print queue()
print queue()
print queue()
