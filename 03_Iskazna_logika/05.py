'''
Tri polja se boje crvenom ili plavom. 
Ukoliko je prvo crveno, druga dva moraju biti iste boje.
Ukoliko je drugo crveno, trece mora biti plavo.

A - prvo polje je crveno
B - drugo polje je crveno
C - trece polje je crveno
'''

import Formula as f

A, B, C = f.vars("A,B,C")

formula = (A >> (B == C)) & (B >> (~C))

for val in formula.all_valuations_that_interpret_to_true():
    print("Resenje:")
    print(f"Polje A je {'crveno' if val['A'] else 'plavo'}")
    print(f"Polje B je {'crveno' if val['B'] else 'plavo'}")
    print(f"Polje C je {'crveno' if val['C'] else 'plavo'}")
