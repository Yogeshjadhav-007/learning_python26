# set is used to reprsent a group of values just like list and represnt by {}
# insertion order is not preserved
# duplicates are not allowed
# hetrogenious datatype are allowed
#index and slicing are not applicable
# it is mutable
'''
s1={10,20,"yogesh",True,10,10}
print(s1)
s1.add("java")
print(s1)
'''
'''
# empty set
s=set()
print(s)
'''
# frozenset - it is a immutable
s={10,20,40,10}
print(type(s))
print(s)
# converting set into frozenset
fs=frozenset(s)
print(type(s))
print(fs)




