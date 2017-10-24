'''Suppose you want climb a staircase of N steps, and on each step you can take either 1 or 2 steps. 
How many distinct ways are there to climb the staircase?'''

def stair_pattern(num):
        if num <=2: 
           return num
        else: 
           return stair_pattern(num-1)+ stair_pattern(num-2)

print stair_pattern(int(raw_input()))
