# This generates .atoms files for all charge-balanced quaternary compositons for the specified elements and their oxidation states (ions), and a number of anions (Nani)
 
ions = {'Li':1,'Si':4,'Cl':-1,'S':-2}

Nani = 8

#==============================================================================
el = [i for i in ions]
anions = el[-2:]       #['Cl','S']
cations = el[:2]       #['Li', 'Si']

for a1 in range(1, Nani):
    a2 = Nani - a1
    nanions = sum([n * a for n,a in zip([a1, a2], [ions[i] for i in anions])])
    for c1 in range(1, Nani+2):
        for c2 in range(1, Nani+2):
            ncations = sum([n * a for n,a in zip([c1, c2], [ions[i] for i in cations])])
            if ncations != -nanions: continue
            numbers = [c1,c2,a1,a2]
            name = f"{el[0]}{c1}{el[1]}{c2}{el[2]}{a1}{el[3]}{a2}"
            for a,n in zip(el,numbers):
                 print(f"{a} {n} {str(ions[a])}", file=open(f"{name}.atoms","a"))
