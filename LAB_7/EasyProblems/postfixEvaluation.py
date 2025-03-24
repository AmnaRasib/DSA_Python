class PostfixEvaluate:
    def evaluate(self,expression):
        stack=[]
        for token in expression.split():
            if token.isdigit():
                stack.append(int(token))
            else:
                operand2=stack.pop()
                operand1=stack.pop()
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = operand1 / operand2
                
                stack.append(result)  # Push result back to stack

        return stack.pop()  # Final result

# Example usage
expr = "5 2 + 8 *"  # Equivalent to (5 + 2) * 8 = 56
evaluator = PostfixEvaluate()
print("Result:", evaluator.evaluate(expr))