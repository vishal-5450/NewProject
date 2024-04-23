def generate_assembly(expression):
    assembly_code = ""
    assembly_code += "MOV R0, " + expression.split()[0] + "\n"
    assembly_code += "MOV R1, " + expression.split()[2] + "\n"
    if "+" in expression:
        assembly_code += "ADD R0, R1\n"
    elif "-" in expression:
        assembly_code += "SUB R0, R1\n"
    elif "*" in expression:
        assembly_code += "MUL R0, R1\n"
    elif "/" in expression:
        assembly_code += "DIV R0, R1\n"
    return assembly_code

# Example usage:
expression = input("Enter expression (e.g., a + b): ")
assembly_code = generate_assembly(expression)
print("Generated Assembly Code:")
print(assembly_code)
