import math


myvariable=30
ans=myvariable +10
print(ans)

ans1=myvariable **3
print(ans1)

print(list)

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)

names = ['sandy','mandy','candy','fandry','chundy','bunty','fandry']
print(names)
a=names[0]
print(a)
b=names[-1]
print(b)
names.append('landy')
print(names)
names.remove('landy')
print(names)
print(names,numbers)
print(len(numbers))
print(len(names))

print(numbers[4:8])
print(numbers[6:])
print(numbers[:6])
print(names)
print(names[2:3])
print(names[2:4])
print(numbers[::2])
print(numbers[::1])
print(numbers[::3])
print(numbers[1::2])

print(tuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

thistuple = ("apple", "banana", "cherry")
print(thistuple[0])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

else:
    print("No, 'apple' is Not in the fruits tuple")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(yellow)
print(green)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)



histuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

  thistuple = ("apple", "banana", "cherry")
  i = 0
  while i < len(thistuple):
      print(thistuple[i])
      i = i + 1

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

