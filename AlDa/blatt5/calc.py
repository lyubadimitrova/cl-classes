import re

class NodeNum:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return self.key
        
class NodeOp:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = self.right = None

    def __str__(self):
        return self.key

class Number:
    def __init__(self, number):
        self.number = int(number)

    def __str__(self):
        return str(self.number)

class Operator:
    def __init__(self, operator):
        self.operator = operator

    def __str__(self):
        return self.operator



def parse(s):
    """
    This function builds the binary tree corresponding to an expression, where each internal node 
    represents an operator (+, -, *, /), each sub-tree represents a left or right operand, 
    and each leaf represents a number. 

    Arguments:
    s -- string, the input expression

    Returns:
    root -- the root node of the tree
    """
    
    fixed = fix(s)

    stack = []
    for token in fixed:
        if token.isdigit():
            stack.insert(0, NodeNum(token, Number(token)))
        else:
            right = stack.pop(0)
            left = stack.pop(0)
            op = NodeOp(token, Operator(token))
            op.right = right
            op.left = left
            stack.insert(0, op)

    root = stack[0]
    return root


def max_depth(node):
    if isinstance(node, NodeNum):
        return 0
    else:
        max_d_left = max_depth(node.left)
        max_d_right = max_depth(node.right)
        max_d = max(max_d_left, max_d_right) + 1
        return max_d

def traverse(root):
    
    thislevel = [root]
    while thislevel:
        nextlevel = []
        indent = 0
        for i in range(thislevel):
            print(' ' * indent)
            print(n.key, end = " ")
            if isinstance(n, NodeOp): 
                nextlevel.append(n.left)
                nextlevel.append(n.right)
        print("\n")
        thislevel = nextlevel


ops = {'*':2, '/':2, '+':1, '-':1}
def fix(s):
    """
    Converts a mathematical expression from infix into postfix notation.
    Algorithm as seen on https://en.wikipedia.org/wiki/Shunting-yard_algorithm#The_algorithm_in_detail.
    
    Arguments:
    s -- string, the input expression

    Returns:
    numbers_queue -- list, tokens in postfix order
    
    """
    numbers_queue = []
    operator_stack = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            numbers_queue.append(s[i])
        if s[i] in ops:
            if operator_stack:
                while operator_stack and operator_stack[0] != "(" and ops[operator_stack[0]] >= ops[s[i]] :
                    numbers_queue.append(operator_stack.pop(0))
            operator_stack.insert(0, s[i])
        if s[i] == "(":
            operator_stack.insert(0, s[i])
        if s[i] == ")":
            while operator_stack[0] != "(":
                numbers_queue.append(operator_stack.pop(0))
            operator_stack.pop(0)
        i += 1
    
    while operator_stack:
        numbers_queue.append(operator_stack.pop(0))

    return numbers_queue

s = '2*4*(3+(4-7)*8)-(1-6)'
#parse(s)
print(fix(s))
p = parse("5+6*3")
traverse(p)



'''
    pot_root = 0

    #par_expr = re.compile("\(([1-9\*\+-\/]*(\([^\(\)]+\))?[1-9\*\+-\/]*)+\)")
    if "(" in s:
        open_par = s.index("(")
        pars = 1
        i = open_par + 1
        while pars != 0:
            if s[i] == ')':
                pars -= 1
            elif s[i] == '(':
                pars += 1
            i += 1
        cl_par = i

    print(s[open_par:cl_par])

    root = NodeOp(fixed[-1], Operator(fixed.pop()))

        if fixed[-1].isdigit():
            root.right = NodeNum(fixed[-1], Number(fixed[-1]))
        if fixed[-1].isdigit() and fixed[-2].isdigit() and not fixed[-3].isdigit():
            root.right = NodeNum(fixed[-1], Number(fixed[-1]))
            root.left = NodeNum(fixed[-2], Number(fixed[-2]))
            return root
        if fixed[-1].isdigit() and not fixed[-2].isdigit():
            root.right = NodeNum(fixed[-1], Number(fixed.pop()))
            root.left = parse_helper(fixed)
            return root
        if not fixed[-1].isdigit() and fixed[-2].isdigit():
            root.right = parse_helper(fixed)
            root.left = NodeNum(fixed[-1], Number(fixed[-1]))
            return root
        if not fixed[-1].isdigit() and not fixed[-2].isdigit():
            root.right = parse_helper(fixed)
            if fixed[-1].isdigit():
                root.left = NodeNum(fixed[-1], Number(fixed[-1]))
            else:
                root.left = parse_helper(fixed)
            return root



        if not fixed:
            return ""

        root = NodeOp(fixed[-1], Operator(fixed.pop()))

        
        if fixed[-1].isdigit() and fixed[-2].isdigit():
            n = fixed.pop()
            root.right = NodeNum(n, Number(n))
            n = fixed.pop()
            root.left = NodeNum(n, Number(n))
            return root
        elif fixed[-1].isdigit():
            n = fixed.pop()
            root.right = NodeNum(n, Number(n))
            root.left = parse_helper(fixed)
            return root
        elif not fixed[-1].isdigit():
            root.right = parse_helper(fixed)
            root.left = parse_helper(fixed)
            return root
'''