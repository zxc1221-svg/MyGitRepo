#map用法
'''numbers=[1,2,3,4,5]

print([x**2 for x in numbers])
=
result=map(lambda x:x**2,numbers)
print(list(result))
==[1,4,9,16,25]
'''


'''
def add_one(x):
    return x+1

numbers=[1,2,3,4,5]
print(list(map(add_one,numbers)))
=[2,3,4,5,6]
'''

#map可以用於多個list
'''
a=[1,2,3]
b=[4,5,6]

result=map(lambda x,y:x+y,a,b)
print(list(result))
=[5,7,9]
'''
