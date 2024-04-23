
def first(prods,nonTer):
    firstSet = set()

    if nonTer not in prods:
        return firstSet
    
    for prod in prods[nonTer]:
        if prod[0].islower() or prod[0]=='':
            firstSet.add(prod[0])
        elif prod[0].isupper():
            firstSet.update(first(prods,prod[0]))

    return firstSet

prod = {
    'S':['Ab','b'],
    'A':['c']
}
nonTer = 'S'
firstSet = first(prod,nonTer)
print(f'First: {firstSet}')