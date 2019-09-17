def first(n)
    return print('You can travel: (N)orth.')
def second(n)
    return print('You can travel: (N)orth or (S)outh or (E)ast.')
def third(n)
    return print('You can travel: (S)outh or (E)ast.')
def forth(n)
    return print('You can travel: (E)ast or (W)est.')
def fifth(n)
    return print('You can travel: (W)est or (S)outh.')
def sixth(n)
    return print('You can travel: (N)orth.')
def seventh(n)
    return print('Victory!')
def eight(n)
    return print('You can travel: (N)orth or (S)outh.')
def nine(n)
    return print('You can travel: (W)est or (S)outh.')

direction=input('Direction:')

while 1<=n<=9:
    if n==1 and (direction=="N" or direction=='n'):
        first(n)
        direction=input('Direction:')
    elif n==2 and (direction=="N" or direction=='n' or direction=="S" or direction=='s' or direction=="E" or direction=='e'):
        second(n)
        direction=input('Direction:')
    elif n==3 and (direction=="S" or direction=='s' or direction=="E" or direction=='e'):
        third(n)
        direction=input('Direction:')
    elif n==4 and (direction=="E" or direction=='e' or direction=="W" or direction=='w'):
        forth(n)
        direction=input('Direction:')
    elif n==5 and (direction=="W" or direction=='w' or direction=="S" or direction=='s'):
        fifth(n)
        direction=input('Direction:')
    elif n==6 and (direction=="N" or direction=='n')


