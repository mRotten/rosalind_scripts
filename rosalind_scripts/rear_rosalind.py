import argparse
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    args = parser.parse_args()
    seq_pairs = __get_input(args.input_path)
    result = list()
    for i, sp in enumerate(seq_pairs):
        print(f'Starting pair {i}...')
        rpl = __get_relative_position_list(sp[0], sp[1])
        result.append(get_reversal_distance(rpl))
    print(" ".join([str(x) for x in result]))


def test():
    begin = time.perf_counter()
    seq_pairs = __get_input("../rosalind_test_files/rear_example.txt")
    seq_pairs.extend(__get_input("/Users/mlalonde/Downloads/rosalind_rear.txt"))
    seq_pairs.extend(__get_input("/Users/mlalonde/Downloads/rosalind_rear_1.txt"))
    result = list()
    for sp in seq_pairs:
        rpl = __get_relative_position_list(sp[0], sp[1])
        result.append(get_reversal_distance(rpl))
    print(" ".join([str(x) for x in result[:5]]))
    print(" ".join([str(x) for x in result[5:10]]))
    print(" ".join([str(x) for x in result[10:]]))
    print(f'{len(seq_pairs)} reversal distances calculated in {round(time.perf_counter() - begin, 1)} seconds.')


def get_reversal_distance(relative_position_list):
    rpl = relative_position_list
    best_revs = [(__get_breaks(rpl), rpl), ]
    rev_count, new_revs = 0, list()

    bp_cutoff = 11
    while not any([len(x[0]) == 0 for x in best_revs]):
        for rev in best_revs:
            new_revs.extend(get_single_reversals(rev[0], rev[1], bp_cutoff))
        rev_count += 1
        best_revs += new_revs
        new_revs = list()
        min_bps = min([len(x[0]) for x in best_revs]) + 1
        print(f'Filtering breakpoints >{min_bps}')
        filt_revs = list(filter(lambda x: len(x[0]) <= min_bps, best_revs))
        best_revs = list()
        for br in filt_revs:
            if br not in best_revs:
                best_revs.append(br)
        bp_cutoff = min_bps - 1
        print(f'...now storing {len(best_revs)} reversals.')

    return rev_count


def get_single_reversals(break_list, rel_pos_list, bp_cutoff):
    reversals, rpl = list(), rel_pos_list
    for i, bp1 in enumerate(break_list):
        for bp2 in break_list[i+1:]:
            rev_subseq = rpl[bp1:bp2]
            rev_subseq.reverse()
            seq = rpl[:bp1] + rev_subseq + rpl[bp2:]
            bpl = __get_breaks(seq)
            if len(bpl) <= bp_cutoff:
                reversals.append((bpl, seq))
    return reversals


# ================ UTILITIES ======================================


def __get_relative_position_list(list1: list, list2: list) -> list:
    """
    Returns the order of list1 relative to list2.
    :param list1: A rearrangement of list2.
    :param list2: A rearrangement of list1.
    :return: The position of each element of list1 in list2.
    """
    return [list2.index(x) for x in list1]


def __get_breaks(pos_list):
    bps = list()

    if pos_list[0] != 0:
        bps.append(0)
    if pos_list[-1] != max(pos_list):
        bps.append(len(pos_list))

    for i, p in enumerate(zip(pos_list[:-1], pos_list[1:]), 1):    # i is the index of the list element after p
        diff = p[1] - p[0]
        if abs(diff) != 1:    # if still increasing or decreasing by 1
            bps.append(i)

    bps.sort()
    return bps


def __get_input(path):
    seq_pairs = list()
    with open(path, 'r') as infile:
        raw = infile.read().strip().split("\n\n")
    for txt in raw:
        seq_pairs.append(tuple([[int(xi) for xi in x.split(" ")] for x in txt.split("\n")]))
    return seq_pairs


if __name__ == '__main__':
    main()
