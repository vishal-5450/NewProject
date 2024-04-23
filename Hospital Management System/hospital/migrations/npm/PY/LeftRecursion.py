def remove_left_recursion(productions):
    new_productions = {}
    non_terminals = list(productions.keys())

    for A in non_terminals:
        alpha = []
        beta = []
        
        for production in productions[A]:
            if production.startswith(A):
                alpha.append(production[1:])
            else:
                beta.append(production)

        if alpha:
            A_prime = A + "'"
            new_productions[A_prime] = [a + A_prime for a in alpha] + ['']
            new_productions[A] = [b + A_prime for b in beta]
        else:
            new_productions[A] = productions[A]

    return new_productions

# Example usage
if __name__ == "__main__":
    # Define your grammar rules
    productions = {
          'A': ['Ab', 'Aa', 'c']
    }

    # Remove left recursion
    new_productions = remove_left_recursion(productions)

    # Print the modified grammar
    for non_terminal, productions in new_productions.items():
        print(non_terminal, "->", " | ".join(productions))
