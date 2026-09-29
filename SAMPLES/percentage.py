def percentage(t,nsub):
    p=list()
    for i in t:
        percentage = (i / nsub * 100) * 100
        p.append(percentage)
    return p
