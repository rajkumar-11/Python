from itertools import permutations,combinations_with_replacement

perm=permutations([1,2,3],2)

for i in list(perm):
    print(i)

combinations=combinations_with_replacement([1,2,3],2)
print("These are the combinations")

for i in list(combinations):
    print(i)