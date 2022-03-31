'''
|A|B|
|C|D|
Tabela 2x2 se boji crvenom ili plavom bojom.
Ako je polje A ofarbano crvenom onda barem jedno od ostalih polja mora biti plavo.
Ako je polje D ofarabno plavom onda barem dva ostala moraju biti crvena.
Ne smeju sva polja biti ofarabana istom bojom.
'''

import Formula as f

A, B, C, D = f.vars("A,B,C,D")

formula = (A >> ( (~B | ~C | ~D) ) ) \
        & (~D >> ( (A & B) | (A & C) | (B & C) ) ) \
        & ~(A & B & C & D) & ~(~A & ~B & ~C & ~D)

for val in formula.all_valuations_that_interpret_to_true():
    print("Resenje: ")
    print(f" {'C' if val['A'] else 'P'} | {'C' if val['B'] else 'P'} ")
    print(f" {'C' if val['C'] else 'P'} | {'C' if val['D'] else 'P'} ")
    
