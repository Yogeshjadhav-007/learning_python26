#In Python, a dictionary is a built-in data type used to store data in key–value pairs.
#It is mutable, and does not allow duplicate keys.
d={1:"python",2:"java",3:"DA",'a':'apple',"fname":"yogesh",1:"SQL"}
print(type(d))
print(d)
print(d[2])
print(d['a'])

# add keys
d={1:"yogesh",2:"vaibhav",3:"eknath"}
print(d)
d[4]="nilesh"
print(d)
# replace key
d[3]="katik"
print(d)
# empty dict
d={}
print(type(d))
print(d)
#hetrogenious datatype
d={'fname':["yogesh","vaibhav","nilesh"],'salary':[10000,20000,30000]}
print(d)
print("**********************************")
print(d['fname'][1])
print(d)