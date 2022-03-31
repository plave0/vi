''' 
|A|B|
|C|D|
Zapisati uslov da se u tabeli 2x2 sa poljima A,B,C,D moze postaviti tacno jedan zeton u 
svakom redu
'''

import Formula as f

A, B, C, D = f.vars("A,B,C,D")
formula = (A | B) & ~(A & B) & (C | D) & ~(C & D)

for val in formula.all_valuations_that_interpret_to_true():
    print("Resenje: ")
    print(val)
