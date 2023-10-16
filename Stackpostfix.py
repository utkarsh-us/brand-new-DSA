"""
**Question: Postfix Expression Evaluation**

You are given a string representing a postfix expression. Implement a Python function to evaluate the expression and return the result.

A postfix expression is an expression in which each operator follows its operands. For example, the infix expression `(3 + 4) * 5` is represented as `3 4 + 5 *` in postfix notation.

You need to implement the `evaluate_postfix(expression)` function that takes a string containing a postfix expression and returns the result as an integer.

The postfix expression will consist of:
- Integers (positive or negative).
- Operators: `+` (addition), `-` (subtraction), `*` (multiplication), and `/` (division).

**Example:**

```python
expression = "3 4 + 5 *"
result = evaluate_postfix(expression)
print(result)  # Output: 35

expression = "5 3 4 * -"
result = evaluate_postfix(expression)
print(result)  # Output: -7
```

**Constraints:**
- The input expression is a valid postfix expression.
- The result will be an integer.
- Assume that the given expression is well-formed and won't produce any division by zero errors.

This question tests your ability to implement a stack to handle complex postfix expression evaluation, considering operator precedence and handling both positive and negative integers."""

# solution

def evaluate_postfix(expression):
    stack = []

    def perform_operation(op, operand1, operand2):
        if op == '+':
            return operand1 + operand2
        elif op == '-':
            return operand1 - operand2
        elif op == '*':
            return operand1 * operand2
        elif op == '/':
            return int(operand1 / operand2)

    operators = set(['+', '-', '*', '/'])
    tokens = expression.split()

    for token in tokens:
        if token not in operators:
            # If the token is an operand, push it onto the stack
            stack.append(int(token))
        else:
            # If the token is an operator, pop the top two elements from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Perform the operation and push the result back onto the stack
            result = perform_operation(token, operand1, operand2)
            stack.append(result)

    # The final result will be at the top of the stack
    return stack[0]

# Example usage:
expression = "3 4 + 5 *"
result = evaluate_postfix(expression)
print(result)  # Output: 35

expression = "5 3 4 * -"
result = evaluate_postfix(expression)
print(result)  # Output: -7


# explaination
"""
1-We define a perform_operation function to perform the specified operations (+, -, *, /) on two operands.

2-We split the input postfix expression into tokens (numbers and operators).

3-We iterate through the tokens in the expression:

If a token is an operand, we convert it to an integer and push it onto the stack.
If a token is an operator, we pop the top two elements from the stack (these will be the two operands for the operator). We then perform the operation using the perform_operation function and push the result back onto the stack.
After processing all tokens, the final result will be at the top of the stack, and we return it.

This solution uses a stack to efficiently handle the evaluation of the postfix expression while adhering to operator precedence and producing the correct result."""




