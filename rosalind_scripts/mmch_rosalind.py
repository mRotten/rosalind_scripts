from math import prod
from Bio import SeqIO
import argparse


def compute_num_max_matchings(seq):

    au = [seq.count('A'), seq.count('U')]
    gc = [seq.count('G'), seq.count('C')]

    min_au, max_au = min(au), max(au)
    min_gc, max_gc = min(gc), max(gc)

    au_iter = range(max_au - min_au + 1, max_au + 1)
    gc_iter = range(max_gc - min_gc + 1, max_gc + 1)

    num_au = prod(au_iter)
    num_gc = prod(gc_iter)

    return num_au * num_gc


def get_seq_from_fasta(path):
    return str(list(SeqIO.parse(path, 'fasta'))[0].seq)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--fasta_path')
    args = parser.parse_args()
    seq = get_seq_from_fasta(args.fasta_path)
    print(compute_num_max_matchings(seq))


tests = {'AAAUUGGGCC': 36,
         'AAAUUGGC': 12,
         'AUUUGCC': 6,
         'AUUUGCCCC': 12,
         'AUUU': 3,
         'AAUUU': 6,
         'AAUUUU': 12,
         'AAUUUUU': 20}

for test_seq, known_count in tests.items():
    assert compute_num_max_matchings(test_seq) == known_count


if __name__ == '__main__':
    main()
