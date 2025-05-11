def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def apply_op(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def evaluate(expression):
    values = []  # Stack for numbers
    ops = []     # Stack for operators

    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue

        elif expression[i] == '(':
            ops.append(expression[i])

        elif expression[i].isdigit():
            val = 0
            while i < len(expression) and expression[i].isdigit():
                val = val * 10 + int(expression[i])
                i += 1
            values.append(val)
            continue  # to skip i += 1 at bottom

        elif expression[i] == ')':
            while ops and ops[-1] != '(':
                right = values.pop()
                left = values.pop()
                op = ops.pop()
                values.append(apply_op(left, right, op))
            ops.pop()  # Remove '('

        else:
            # Operator
            while ops and precedence(ops[-1]) >= precedence(expression[i]):
                right = values.pop()
                left = values.pop()
                op = ops.pop()
                values.append(apply_op(left, right, op))
            ops.append(expression[i])

        i += 1

    while ops:
        right = values.pop()
        left = values.pop()
        op = ops.pop()
        values.append(apply_op(left, right, op))

    return values[0]

expr = "3*8-(3-4+1)"
result = evaluate(expr)
print("Result:", result)
