def grade(p) :
    g=list()
    for i in p:
        if i>=90:
            g.append("A")
        elif i<90 and i>=80:
            g.append("B")   
        elif i<80 and i>75:
            g.append("C")   
        else:
            g.append("F") 
    return g  