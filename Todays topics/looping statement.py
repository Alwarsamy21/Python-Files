# While loop 
#exit the loop when the while condition is False

a = 1
while a<=5:
    print (a)
    a = a + 1
print("loop over")


#exit the loop when a is 5
#With the break statement we can stop the loop even if the while condition is true

a = 0
while a < 10:
  print(a)

  if a == 5:
    break
  a += 1


#for loop (str/list/tuple/set)

#str (it fetches letter by letter)

for i in "it fetches letter by letter":
    print(i)

#list (fetches element by element)

for i in [1, 2.33, "hello", False]:
    print(i)


