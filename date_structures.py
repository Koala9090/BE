import random
list = [1312,3213,3123,32424,123123]
list.append("i have a nice one")
del list[0]
print(list[::1])
tuple =(99,993,"nfjksd")

print(tuple)



a = {1,2,3,4}
b = {4,5,6,7,8,9,9,4,3,2,10}
print(a)
e=b.difference(a)
print(e)
f= (9 in b)
r = (99 in a)

print(f)
print(r)
l = a.union(b)
print (l)

p = a.intersection(b)
print(p)


fruits = ["pier","bananas","Mango","grapes"]
print(fruits[2])


book = {
    'title' : 'sdasd',
    'author' : 'sadasd',
    'genre' : 'dasdad'
}

genre =book.get('genre','Unknows')
print(f"Genre : {genre}")


random_numbers =[random.randint(1,20) for _ in range(20)]
print(random_numbers)

unique_numbers = set(random_numbers)

print (unique_numbers)
