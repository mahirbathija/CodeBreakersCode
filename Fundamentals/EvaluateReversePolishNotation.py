# create a stack and keep adding ints from the list to it.
# when you come across an operand, pop the last 2 elements in the stack and
# complete the operation and push the result into the stack
# Finally pop the last element and return it.

# PSEUDOCODE

# def evalRPN(self, tokens: List[str]) -> int:
#   stack = []
#   for el in tokens:
#       if el is operand:
#           compute(el, stack.pop(), stack.pop())
#           add result to stack
#       else:
#           add el to stack
#   return stack.pop()

# def compute(el, second, first):
#   convert first and second to int
#   return first el second

import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            if el in ["+", "-", "/", "*"]:
                result = self.compute(el, stack.pop(), stack.pop())
                stack.append(result)
            else:
                stack.append(el)
        return stack.pop()

# checks the operand type and returns the result
    def compute(self, operand, second, first):
        first = int(first)
        second = int(second)
        if operand == '+':
            return first + second
        if operand == '-':
            return first - second
        if operand == '/':
            ans = first / second
            if ans < 0:
                return math.ceil(ans)
            return math.floor(ans)
        if operand == '*':
            return first * second
        