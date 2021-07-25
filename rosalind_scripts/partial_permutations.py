# n objects in an array A
# how many possible permutations of k objects from array N?
# If k == 4:
    # first object: n possibilities.
    # second object: n-1 possibilities.
    # third object: n-2 possibilities.
    # fourth object: n-3 possibilities.

    # total possibilities: n * (n-1) * (n-2) * (n-3).

def num_partial_perms(n, k, mod=1000000):
    total = 1
    for i in range(k):
        total *= (n - i)
    return total % mod
