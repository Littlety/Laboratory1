OPERAND_TO_PRIORITY = {
    '*': 0,
    '/': 0,
    '-': 1,
    '+': 1,
    '(': 2,
    ')': 2,
}


def parse(line):
    output = ""
    stack = []
    str = line.split(' ')
    for s in str:
        if s == "(":
            stack.append(s)
        elif s == ")":
            while stack[-1] != "(":
                output = output + stack[-1] + " "
                stack.pop()
            stack.pop()
        elif s == '+' or s == '-' or s == '*' or s == '/':
            while len(stack) != 0 and OPERAND_TO_PRIORITY[s] >= OPERAND_TO_PRIORITY[stack[-1]]:
                output = output + stack[-1] + " "
                stack.pop()
            stack.append(s)
        else:
            if s[0] == ".":
                output = output + '0'
            output = output + s
            if s[-1] == ".":
                output += '0'
            output += " "
    while len(stack) != 0:
        output = output + stack[-1] + " "
        stack.pop()
    output = output[:-1]
    return output