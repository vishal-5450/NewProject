operators = {"+": "ADD", "-": "SUB", "*": "MUL", "/": "DIV"}  # Operator mapping

def generate_tac(expression):
  """
  Generates Three-Address Code (TAC) for a simple arithmetic expression.

  Args:
      expression (str): The arithmetic expression (e.g., "a + b * c").

  Returns:
      list: A list of TAC instructions represented as tuples (operator, operand1, operand2, result).
  """
  tac = []
  stack = []

  if len(stack) >= 2:  # Check if there are at least 2 operands before popping
    operand2 = stack.pop()
    operand1 = stack.pop()
    # ... rest of your code
  else:
    raise IndexError("Insufficient operands for operator")

  for token in expression.split():
    if token in operators:
      operand2 = stack.pop()
      operand1 = stack.pop()
      result = f"temp{len(tac)}"  # Generate temporary variable names
      tac.append((operators[token], operand1, operand2, result))
      stack.append(result)
    else:
      stack.append(token)  # Assume token is a variable or constant

  return tac

# Example usage
expression = "a + b * c"
tac = generate_tac(expression)

for op, operand1, operand2, result in tac:
  print(f"{result} := {operand1} {op} {operand2}")