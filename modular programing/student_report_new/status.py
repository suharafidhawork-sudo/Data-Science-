def status(g):
    s=list()
    for i in g:
        if i=="A"or i=="B" or i=="C":
            s.append("passed")
        else:
            s.append("failed")    
    return(s)     