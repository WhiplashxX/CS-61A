#An Environment is a sequence of frames
#A name evaluates to the value bound to that name in the earliest  frame of the current environment in which that name is found
from operator import mul
def square(square):
  return mul(square,square)
square(-2)
#see in https://pythontutor.com/visualize.html#mode=edit
#A function that doesn't explictly return a value will return None
 
