A = {1, 2, 3}
B = {2, 3, 4}

print("{} ∪ {} is {}".format(A, B, A | B))
print("{} ∩ {} is {}".format(A, B, A & B))
print("{} - {} is {}".format(A, B, A - B))

# the empty set is set()
empty_set = set()
print("∅ ∪ {1,2,3} is", empty_set | A)
