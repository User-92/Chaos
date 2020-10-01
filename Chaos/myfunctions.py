import random


def rancolor():
    cd = str(hex(random.randint(1118481, 16777215)))
    g = 0
    bd = "#"
    for k in cd:
        if g < 2:
            pass
        else:
            bd += k
        g += 1
    return bd


def finder_next(x):
    g = 0
    if x > 0:
        while True:
            if x > 2**g:
                g += 1
            else:
                break
    else:
        print("cant be 0 or lower")
        return False
    return [2**g, g]


def weird_shuffle(message):
    x = message
    o = []
    e = []
    ind = []
    gug = 0
    for i in x:
        o.append(i)
    f = len(x) / 2
    if f % 1 == 0:
        o.append(" ")
        gug = 1
    p = len(o)
    for u in range(0, p):
        ind.append(u)
    for ef in range(0, p):
        if max(ind) - ef * 2 < 0:
            break
        e.append(o[max(ind) - ef * 2])
        if min(ind) + 1 + (ef * 2) > max(ind):
            break
        e.append(o[min(ind) + 1 + (ef * 2)])
    zet = ["", p]
    if gug == 1:
        e.remove(e[0])
        zet[0] = " "
        zet[1] = p - 1
    gug = ""
    for ups in range(0, zet[1]):
        gug += e[ups]
    return zet[0] + gug
