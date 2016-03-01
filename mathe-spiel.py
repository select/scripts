def add(rounds=5):
    from random import randint
    import time

    start = time.time()
    bad = False
    for a in range(rounds):
        a=randint(1,9)
        b=randint(1,9)
        c=a+b
        d=raw_input('was ist '+str(a)+' + '+str(b)+' ? ')
        if d == 'x':
            break
        if(int(d) == c):
            print 'Richtig'
        else:
            print 'Leider falsch, das Ergebins ist '+str(a+b)
            bad = True
            break
    if(bad):
        print 'Verloren!!'
    else:
        end = time.time()
        print 'Deine Punkte sind %s'%(int((end - start)*100))

def multi(rounds=5):
    from random import randint
    import time

    start = time.time()
    bad = False
    for a in range(rounds):
        a=randint(2,9)
        b=randint(2,9)
        c=a*b
        d=raw_input('was ist '+str(a)+' * '+str(b)+' ? ')
        if d == 'x':
            break
        if(int(d) == c):
            print 'Richtig'
        else:
            print 'Leider falsch, das Ergebins ist '+str(a*b)
            bad = True
            break
    if(bad):
        print 'Verloren!!'
    else:
        end = time.time()
        print 'Deine Punkte sind %s'%(int((end - start)*100))
