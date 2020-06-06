def lsystem(axioms, rules, iterations):

    for _ in range(iterations):
        newAxioms = ''

        for axiom in axioms:
            if axiom in rules:
                newAxioms += rules[axiom]
            else:
                newAxioms += axiom

        axioms = newAxioms
    return axioms

rules = { "A" : "ABA" , "B" : "BBB"}
print(lsystem('AB', rules, 0))
# outputs : 'AB'

print(lsystem('AB', rules, 1))
# outputs : 'ABABBB'

print(lsystem('AB', rules, 2))
# outputs : 'ABABBBABABBBBBBBBB'