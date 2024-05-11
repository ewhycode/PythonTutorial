var1 = [1,2,3]
var2 = [3, 6, [9,12,5,19]]
var3 = var1 + var2
#print data type
print(type(var2[0]))
print (var2[-1]) #print 3rd in list [9,12..] considered as one list
print (var1)
print (var1 * 3)


for i in var1: #var1
    print(i)

'''above code
can also be written as'''
print(x**2 if x%2==0 else x**3)
y = x**2 if x%2==0 else x**3
print(y)