
# lamdba function
li = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
           ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]]
lt = []
from functools import reduce

lst = []
for i in li:
	a = reduce((lambda x,y : (i[0],(x*y)) if x*y > 100 else (i[0],(x*y)+10)),(i[-2],i[-1]))
	lst.append(a)

print(lst)
print("******************************************")
##########################################################

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
           [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
           [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
print
totals = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), orders))
totals = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b, x[1:])],totals))


print(totals)
print("******************************************")
