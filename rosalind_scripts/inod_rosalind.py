

def build_tree(n):
    leaves, internal = 3, 1
    unpaired_leaf = False
    while leaves < n:
        if unpaired_leaf:
            leaves += 1
            unpaired_leaf = False
        else:
            internal += 1
            unpaired_leaf = True
    return internal


def test():
    for n in range(3, 13):
        internal = build_tree(n)
        if internal != n - 2:
            print(f'{n} leaves: {internal}')


if __name__ == '__main__':
    test()


# This essentially demonstrates that an unrooted binary tree with n leaves can be constructed with no fewer
#   than (n - 2) internal nodes.
# I answered the question by subtracting 2 from the input number of leaves.
