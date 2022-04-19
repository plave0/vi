'''
U igri mines dimenzija 2x3 dobijena je sledeca konfiguracija
|1|A|C|
|1|B|2|
A,B,C su neotvorena polja, a brojevi oznacavaju broj mina u okolnim poljima.
Zapisati u iskaznoj logici uslove koji moraju da vaze.
'''

import Formula as f

A, B, C = f.vars("A,B,C")

formual = (A | B) & ~(A & B) \
        & ~( (A == B) & (B == C) ) \
        & ( (A & B) | (B & C) | (A & C) )

for val in formual.all_valuations_that_interpret_to_true():
    print("Resenje: ")
    for var in val:
        print(f"Na polju {var} {'je mina' if val[var] else 'nije mina'}")

    print()
