# Assumption: each reversal must be productive.
# Update: That's probably a bad assumption.
#   Re-write to store all reversals takes too long b/c there are 3,628,800 permutations of 10 elements.
#   Code to sort in order (sort element 1, then element 2, etc.) works. However, it finds a suboptimal
#       solution (longer reversal distance) for example 1.
#   Exhaustive sorting example 3 gives endless loop.
#

import argparse

test_seq_paths = ["C:/Users/mlalonde/PycharmProjects/rosalind/rosalind_test_files/sort_example_1.txt",
                  "C:/Users/mlalonde/PycharmProjects/rosalind/rosalind_test_files/sort_example_2.txt",
                  "C:/Users/mlalonde/PycharmProjects/rosalind/rosalind_test_files/sort_example_3.txt"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="Path to input file containing two sequences delimited by spaces, "
                        "wherein the first sequence will be sorted into the second sequence.")
    args = parser.parse_args()
    seq_a, seq_b = get_input(args.input_path)
    result = sort_a_into_b(seq_a, seq_b)
    report_result(result)


def calc_ham(seq_a, seq_b):
    return sum([a != b for a, b in zip(seq_a, seq_b)])


def reverse_seq_at_locs(seq, locs):
    seq_list = list(seq)
    rev_segment = list(reversed(seq_list[locs[0]:locs[1]]))
    rev_a = seq_list[:locs[0]] + rev_segment + seq_list[locs[1]:]
    return tuple(rev_a)


def closer_than_before(original_seq, reversed_seq, ref_seq):
    before = calc_ham(original_seq, ref_seq)
    after = calc_ham(reversed_seq, ref_seq)
    return after < before


def get_productive_reversals(seq_a, seq_b):
    len_a = len(seq_a)
    prod_revs = list()
    assert len_a == len(seq_b)
    for start_loc in range(0, len_a - 1):
        for end_loc in range(start_loc + 2, len_a + 1):
            rev_seq = reverse_seq_at_locs(seq_a, (start_loc, end_loc))
            if closer_than_before(seq_a, rev_seq, seq_b):
                prod_revs.append((rev_seq, (start_loc, end_loc)))
    return prod_revs


def get_next_reversals(reversal_dict, ref_seq):
    reversal_repo = reversal_dict.copy()
    for seq_a, rev_route in reversal_dict.items():
        result = get_productive_reversals(seq_a, ref_seq)
        for reversed_seq_a, step in result:
            if reversed_seq_a not in reversal_repo.keys():
                reversal_repo[reversed_seq_a] = rev_route + [step]
    return reversal_repo


def sort_a_into_b(seq_a, seq_b):
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


def test():
    test_seqs = [get_input(p) for p in test_seq_paths]
    for seq_a, seq_b in test_seqs:
        result = sort_a_into_b(seq_a, seq_b)
        report_result(result)


def report_result(result):
    print("Here is the number of steps and each step required to sort the "
          "first sequence into the second sequence:")
    print(f"{len(result)}")
    for step in result:
        print(f'{step[0] + 1} {step[1]}')


if __name__ == "__main__":
    test()
    # main()
