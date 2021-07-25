import argparse
from Bio.Seq import Seq


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    parser.add_argument('-o', '--output_path', default=None)
    args = parser.parse_args()
    array = get_input(args.input_path)
    adj_list = get_adjacency_list(array)
    save_results(args.output_path, adj_list)


def test():
    inpath = "C:/Users/mlalonde/PycharmProjects/rosalind_problems/rosalind_test_files/dbru_example.txt"
    outpath = "C:/Users/mlalonde/PycharmProjects/rosalind_problems/rosalind_test_files/dbru_example_output.txt"
    array = get_input(inpath)
    adj_list = get_adjacency_list(array)
    save_results(outpath, adj_list)


def get_input(path):
    with open(path, 'r') as infile:
        raw = infile.read().strip().split("\n")
    return [Seq(x) for x in raw]


def get_adjacency_list(seq_list):
    adj_list = list()
    for seq in seq_list:
        fwd, rev = get_seq_adjacents(seq)
        if fwd not in adj_list:
            adj_list.append(fwd)
        if rev not in adj_list:
            adj_list.append(rev)
    adj_list.sort()
    return adj_list


def get_seq_adjacents(seq):
    seq_rc = seq.reverse_complement()
    return [(seq[:-1], seq[1:]), (seq_rc[:-1], seq_rc[1:])]


def save_results(path, result):
    open(path, 'w').close()
    with open(path, 'a') as outfile:
        for pref, suff in result:
            outfile.write(f'({pref}, {suff})\n')


if __name__ == '__main__':
    main()
    #test()
