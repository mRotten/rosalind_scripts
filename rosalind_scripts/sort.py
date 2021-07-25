# Assumption: each reversal must be productive.
# Update: That's probably a bad assumption. Re-write to store all reversals takes too long.
#   There are 3,628,800 permutations of 10 elements.
# Exhaustive sort finds a shorter reversal distance for example 1.

ex1_path = "C:/Users/mlalonde/PycharmProjects/rosalind/rosalind_test_files/sort_example_1.txt"
ex2_path = "C:/Users/mlalonde/PycharmProjects/rosalind/rosalind_test_files/sort_example_2.txt"


def calc_ham(seq_a, seq_b):
    return sum([a != b for a, b in zip(seq_a, seq_b)])


def reverse_seq_at_locs(seq, locs):
    seq_list = list(seq)
    rev_segment = list(reversed(seq_list[locs[0]:locs[1]]))
    rev_a = seq_list[:locs[0]] + rev_segment + seq_list[locs[1]:]
    return tuple(rev_a)


def want_to_keep(original_seq, reversed_seq, ref_seq):
    before = calc_ham(original_seq, ref_seq)
    after = calc_ham(reversed_seq, ref_seq)
    return after < before


def get_productive_reversals(seq_a, seq_b):
    # This function is producing the correct start and stop values.
    len_a = len(seq_a)
    prod_revs = list()
    assert len_a == len(seq_b)
    for start_loc in range(0, len_a - 1):
        # ends = list()
        for end_loc in range(start_loc + 2, len_a + 1):
            # ends.append(end_loc)
            rev_seq = reverse_seq_at_locs(seq_a, (start_loc, end_loc))
            if want_to_keep(seq_a, rev_seq, seq_b):
                prod_revs.append((rev_seq, (start_loc, end_loc)))
        # print(f'{start_loc}: {ends}')
    return prod_revs


def get_next_reversals(reversal_dict, ref_seq):
    reversal_repo = reversal_dict.copy()
    for seq_a, rev_route in reversal_dict.items():
        result = get_productive_reversals(seq_a, ref_seq)
        for reversed_seq_a, step in result:
            if reversed_seq_a not in reversal_repo.keys():
                reversal_repo[reversed_seq_a] = rev_route + [step]
            # if reversed_seq_a == ref_seq:
            #     return reversal_repo
    return reversal_repo


def sort_exhaustively(seq_a, seq_b):
    reversals = {seq_a: list()}
    sentinel = 0
    while seq_b not in reversals.keys():
        sentinel += 1
        reversals = get_next_reversals(reversals, seq_b)
        print(f'\n{sentinel} reversals computed')
        print(f'storing {len(reversals)} reversal permutations')
    reversal_path = reversals[seq_b]
    return reversal_path


def get_input(path):
    with open(path, 'r') as infile:
        raw_a, raw_b = infile.read().strip("\n").split("\n")
        seq_a, seq_b = tuple(raw_a.split(" ")), tuple(raw_b.split(" "))
    return seq_a, seq_b


def get_test_seqs():
    ex1 = get_input(ex1_path)
    ex2 = get_input(ex2_path)
    return ex1, ex2


def sort_in_order(seq_a, seq_b):
    steps = list()
    while seq_a != seq_b:
        seq_a, step = do_next_reversal(seq_a, seq_b)
        steps.append(step)
    return steps


def do_next_reversal(seq_a, seq_b):
    start = [a == b for a, b in zip(seq_a, seq_b)].index(False)
    end = seq_a.index(seq_b[start]) + 1
    seq_a = list(seq_a)
    rev_segment = list(reversed(seq_a[start:end]))
    return tuple(seq_a[:start] + rev_segment + seq_a[end:]), (start, end)


def test():
    ts = get_test_seqs()
    ex1_seq_a, ex1_seq_b = ts[0]
    ex2_seq_a, ex2_seq_b = ts[1]

    ex1_exh = sort_exhaustively(ex1_seq_a, ex1_seq_b)
    ex1_ord = sort_in_order(ex1_seq_a, ex1_seq_b)

    print("\nExample 1 Exhaustive Sort:")
    print(f"{len(ex1_exh)}")
    for step in ex1_exh:
        print(f'{step[0] + 1} {step[1]}')

    print("\nExample 1 Ordered Sort:")
    print(f"{len(ex1_ord)}")
    for step in ex1_ord:
        print(f'{step[0] + 1} {step[1]}')

    ex2_exh = sort_exhaustively(ex2_seq_a, ex2_seq_b)
    ex2_ord = sort_in_order(ex2_seq_a, ex2_seq_b)

    print("\nExample 2 Exhaustive Sort:")
    print(f"{len(ex2_exh)}")
    for step in ex2_exh:
        print(f'{step[0] + 1} {step[1]}')

    print("\nExample 2 Ordered Sort:")
    print(f"{len(ex2_ord)}")
    for step in ex2_ord:
        print(f'{step[0] + 1} {step[1]}')


if __name__ == "__main__":
    test()


# |----------------------|
# | 9 3 4 8 6 7 5 1 2 10 |
# |----------------------|

# 3 8 10 1 6 2 9 5 4 7    original
# 9 2 6 1 10 8 3 5 4 7    (1, 7)
# 9 3 8 10 1 6 2 5 4 7    (2, 6)
# 9 3 4 5 2 6 1 10 8 7    (3, 9)
# 9 3 4 8 10 1 6 2 5 7    (4, 9)
# 9 3 4 8 6 1 10 2 5 7    (5, 7)
# 9 3 4 8 6 7 5 2 10 1    (6, 10)
# 9 3 4 8 6 7 5 1 10 2    (8, 10)
# 9 3 4 8 6 7 5 1 2 10    (9, 10)
