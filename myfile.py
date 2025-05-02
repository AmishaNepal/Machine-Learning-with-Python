def computeSI(p,t,r):
    return (p*t*r)/100
def computeCI(p,t,r):
    return p*((1+r/100)**t)-p

if __name__=='__main__':
    pr=float(input('Enter principal'))
    ti=float(input('Enter time in year'))
    ra=float(input('Enter rate'))
    print(f'The SI is {computeSI(pr,ti,ra):.3f}')
    print(f'The CI is {computeCI(pr,ti,ra):.3f}')