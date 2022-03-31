'''
Date su dve kutije A,B robot mora da stavi objekat u tacno jednu od njih.
'''

import Formula as f

A, B = f.vars("A,B")
formula = (A | B) & ~(A & B)

for valuation in formula.all_valuations_that_interpret_to_true():
    print("Resenje: ")
    for var in valuation:
        print(f"Objekat {'je' if valuation[var] else 'nije'} u kupiji {var}")


