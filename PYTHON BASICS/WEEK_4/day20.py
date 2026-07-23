# #SET

# a={1,2,3,4,5,6,7,8,9,10,33,"fidha","mithra"}
# b={"fidha","mithra","anagha","mamitha","fidha",1,33,33,4,1,2,3,4,5}
# # print(type(a))
# # print(a)
# # print(b)


# print("ORIGINAL SET A: ",a)
# print("ORIGINAL SET B : ",b)
# #ADD
# a.add("fifi")
# print("AFTER ADDING AN ELEMENT TO THE SET:",a)
# #REMOVE
# b.remove(33)
# print("REMOBING ELEMENTT 33 FROM SET B : ",b)
# #DISCARD
# b.discard("fidha")
# print("DISCARD ELEMENT FROM THE SET B:",b)
# #POP
# print("REMOVED A RANDOM ELEMENT FROMS SET A;",a.pop())

# print("---------------------------------------------------------------------------------------------------------------------------")
# print("SET A: ",a)
# print("SET B: ",b)
# #UNION
# print("UNION OF TWO SETS:",a.union(b))
# #INTERSECTION
# print("INTERSECTION OF TWO ELEMENTS:",a.intersection(b))
# #DIFFERENCE
# print("DIFFERENCE OF 2 SETS:",a.difference(b))
# #SYMMETRIC DIFFERENCE
# print("SYMMETRIC DIFFERENCE: ",a.symmetric_difference(b))

# s1={1,2,3,4,5,6,10,11,12,13}
# s2={1,2,3,4,5,6}
# #SUBSET
# print("CHECK IF SET A IS A SUBSET OF SET B:",s1.issubset(s2))
# #SUPERSET
# print("CHECK SET A IS A SUPER SET OF B: ",s1.issuperset(s2))
# #IS DISJOINT SET
# print("CHECK DISJOINT SET: ", s1.isdisjoint(s2))
# #UPDATE
# s2.update([7,8])
# print("UPDATE SET 2:",s2)
# #INTERSECTION UPDATE
# c1={1,2,3}
# c2={2,3,4}
# c1.intersection_update(c2)
# print("INTERSECTION UPDATE:",c1)
# #SYMMETRIC DIFFERENCE
# s1.symmetric_difference_update(s2)
# print("SYMMETRIC DIFFERENCE UPDATE:",s1)
# #DIFFERENCE UPDAT
# s1.difference_update(s2)
# print("DIFFERENCE UPDATE:",s1)

# c=[1,2,3,4,6,9,3]
# d=set(c)#TO FIND TH E UNQUE ELEMENTS
# print(d)

# #------------------------------------------------DICTIONARY---------------------------------------------------------------------
# #CREATING THE DICTIONARY USING 5 METHODS
# #FIRST METHOD
# a={ "fidha":33,"riri":22,"fifi":34}
# print(a)
# #METHOD 2
# b=dict(fidha=22,riri=19)
# print(b)
# #METHOD 3
# c=dict([(1,2),(4,5)])
# print(c)
# #METHOD 4
# d=dict(((1,2),(6,8)))
# print(d)
# key=[1,2,3]
# values=[10,20,30]
# e=dict(zip(key,values))
# print(e)

# d1=dict(fifi=22,riri=18,mehna=24,fami=24)
# print(d1)
# print("RETREIVING VALUES USING GET:",d1.get("fifi"))
# print("all keys:",d1.keys())
# print("all values:",d1.values())
# print("all items:",d1.items())
# d1.update({"zoya":5})
# print(d1)
# d1.popitem()
# print(d1)
# keyss=["a","b","c"]
# c=dict.fromkeys(keyss,30)
# print(c)


