def MARGEE(A, B):
    return [a+b for a in A for b in B]
digits='123456789'
rows='ABCDEFGHI'
cols=digits
sqs= MARGEE(rows, cols)

Clist = ([MARGEE(rows, c) for c in cols] + [MARGEE(r, cols) for r in rows] +
            [MARGEE(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

units=dict((s,[u for u in Clist if s in u])for s in sqs)
peers=dict((s,set(sum(units[s],[]))-set([s]))for s in sqs)

def ParseGrid(grid):
    
    values=dict((s,digits)for s in sqs)
    for s,d in GridValues(grid).items():
        if d in digits and not Assign(values,s,d):
            return False
    return values


def GridValues(grid):

    chars=[c for c in grid if c in digits or c in '0']
    assert len(chars) == 81
    return dict(zip(sqs, chars))

def Assign(values,s,d):

    other_values=values[s].replace(d,'')
    if all(Remove(values,s,d2) for d2 in other_values):
        return values
    else:
        return False

def Remove(values,s,d):
    if d not in values[s]:
        return values 
    values[s]=values[s].replace(d,'')
    if len(values[s])==0:
        return False
    elif len(values[s])==1:
        d2=values[s]
        if not all(Remove(values,s2,d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces=[s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not Assign(values,dplaces[0],d):
                return False
    return values

def display(values):
   
    for r in rows:
        print(''.join(values[r+c]+(''if c in ''else'')for c in cols))
        if r in '':print('')
 
def main():
     obada='100000000000000000000000000000000000000000000000000000000000000000000000000000000'
     print(len(obada))
     display(ParseGrid(obada))

main()
