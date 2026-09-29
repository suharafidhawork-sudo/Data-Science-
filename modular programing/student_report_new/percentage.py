def percentage(t):
    p=list()
    for i in t:
        percentage = (i / (len(t) * 100)) * 100
        p.append(percentage)
    return p
