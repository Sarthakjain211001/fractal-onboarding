#A set containing odd elements
odd_set = {23, 15, 17, 3, 9}
print(odd_set)

#A set containing even elements
even_set = {28, 10, 32, 100, 8, 96}
print(even_set)

#intersection
intersection_set = odd_set.intersection(even_set)
print(intersection_set)

#union
union_set = odd_set.union(even_set)
print(union_set)

#adding a duplicate element to set
odd_set.add(23)
print(odd_set)