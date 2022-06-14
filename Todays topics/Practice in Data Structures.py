# Data structure

#List 
#List is a collection which is ordered and Changeable. And it allows duplicate members

a = [1, 2.44, "hello", 4, False, 6, 1, 1, 1]
print (a, type(a))

print (a[2])

a[2] = "hello world"
print (a)


#Tuple 
# Tuple is same as List the only difference from Tuple is we cannot change the values in Tuple

a = (1, 2.44, "hello", 4, False, 6, 1, 1, 1)
print (a, type(a))

print (a[2])




#Set
# Set is a collection which is Unordered and unindexed. No duplicate members 
# It is totally opposite to List

a = {1, 2.44, "hello", 4, False, 6, 1, 1, 1}
print (a, type(a))


# Dictionary
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.

Nameandage = {
  "karthik": 26,
  "Deepak": 20,
  "Dinesh": 32
}
print(Nameandage)

# print the "Deepak" age
Nameandage = {
  "karthik": 26,
  "Deepak": 20,
  "Dinesh": 32
}
print(Nameandage["Deepak"])

# print the data type of dictionary
Nameandage = {
  "karthik": 26,
  "Deepak": 20,
  "Dinesh": 32
}
print(type(Nameandage))








