#LIST CREATION

a=[1,34,55,6,7,88]
print(a)


#HETEROGENOUS LIST
b=[22,'fidha',24,'fami',24,'mehna']
print(b )

#INSERTING ELEMENT
a[2]=66
print(a)

#INDEXING AND NESTED LIST
c=[[1,2,3],[5,6,7]]
print("NESTED LIST: ",c)
print(c[-1])

#APPEND
d=[1,55,67,88,90,10]
d.append("fidha")
print(d)
d.append(22)
print(d)

#REMOVE
d.remove("fidha")
print(d)
d.remove(d[3])
print("removed using index: ",d)

#POP
e=[6,77,34,56,78,99,20]
print("list before using pop:",e)
e.pop()
print("AFTER POP :",e)

#CLEAR
f=[22,33,44,55,66,77]
print("LIST:",f)
f.clear()
print("cleared the list:",f)

#INDEXING
g=[22,34,61,2,3,4]
print("index of  element:",g.index(3))

#SORT
h=[12,33,3,67,33,88,99,33]
print("COUNT OF ELEMENTS IN AN LIST: ",h.count(33))
h.sort(reverse=True)#DESCENDING ORDER
print("SORTED IN DESCENDING ORDER:",h)
h.sort()
print("SORTED IN ASCENDING ORDER:",h)


#REVERSE
I=[22,33,45,67,20]
print("BEFORE REVERSING",I)
I.reverse()
print("AFTER REVERSE:  ",I)

#COPY LIST
j=[1,66,46,49,10,20]
print("ORIGINAL LIST:",j)
k=j.copy()
print("COPIED LIST :",k)
k.append(56)
print("56 ADDED TO LIST K:",k)
print("ORIGINAL LIST:",j)
j.remove(66)
print("REMOVED THE ELEMENT 66 FROM THE ORIGINAL LIST ",j)

#EXTEND
l=[33,44,56,78,79,90]
print("LIST BEFORE EXTENDING: ",l)
l.extend([20,10,30])
print("LIST AFTER EXTENDING: ",l)


#TUPLE INDEXING AND COUNTING
print("-----------------------------------TUPLE PROBLEMS---------------------------------")
m=(1,3,20,30,40,3,25,65,37,3)
print(type(a))
print(m.count(3))
print(m.index(20))

#TUPLE UNPACKING
print("----TUPLE UNPACKING---")
t=(1,2,3)
print("tuple:",t)
a,b,c=t
print(a,b,c)

#SWAPPING
a=20
b=30
a,b=b,a
print(b,a)
print(a,b)


#TUPLE UNPACKING
r=(1,5,6,7,8,9,2,3,4)
print("ORIGINAL TUPLE: ",r)
a,*b,c=r
print("TUPLE A :",a)
print("TUPLE *B:",*b)#didnt understand
print("TUPLE C: ",c)

#IGNORING THE VALUES
s=(1,2,3)
a,_,c=s
print(s)
print(a,c)

#UNPACKING USING NESTED LIST
u=(1,[2,3])
a,[b,c]=u
print(a,b,c)




