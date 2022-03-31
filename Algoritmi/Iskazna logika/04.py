'''
Dva dvobitna broja se sabiraju i daju rezultat 3.
'''

import Formula as f

A, B, C, D = f.vars("A,B,C,D")

formula = (B | D) & ~(B & D) & (A | C) & ~(A & C)

for val in formula.all_valuations_that_interpret_to_true():
    print("Resenje: ")
    print(f"  {int(val['A'])}{int(val['B'])}") 
    print(f"+ {int(val['C'])}{int(val['D'])}")
    print('----')
    print("  11")


