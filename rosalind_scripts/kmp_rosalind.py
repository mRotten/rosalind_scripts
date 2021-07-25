import argparse
from Bio import SeqIO
import time
from random import choice


def compute_failure_array(dna_sequence):
    fa = list()
    for i, nt in enumerate(dna_sequence):
        if i == 0:
            longest = 0
        else:
            full_len = fa[-1] + 1
            prefix = dna_sequence[:full_len]
            suffix = dna_sequence[:i+1][-full_len:]
            longest = longest_suffix_in_prefix(suffix, prefix)
        fa.append(longest)
    return fa


def longest_suffix_in_prefix(suffix, prefix):
    index = 0
    while index >= 0:
        if suffix == prefix:
            return len(suffix)

        # finding the next occurrence of the first nucleotide in dna_sequence
        index = suffix.find(prefix[0], 1)

        # slice the suffix to begin at index
        suffix = suffix[index:]

        # slice the prefix to have the new suffix length
        prefix = prefix[:len(suffix)]

    return 0


def get_input_sequence(path):
    return str(list(SeqIO.parse(path, 'fasta'))[0].seq)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--fasta_path')
    parser.add_argument('-o', '--output_path', default=None)
    args = parser.parse_args()
    seq = get_input_sequence(args.fasta_path)
    fa = compute_failure_array(seq)
    if not args.output_path:
        print(fa)
    else:
        with open(args.output_path, 'w') as outfile:
            outfile.write(" ".join([str(val) for val in fa]) + "\n")


def test():
    start_time = time.time()
    fasta_path = "../rosalind_test_files/kmp_example_file.fasta"
    seq = get_input_sequence(fasta_path)
    fa = compute_failure_array(seq)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(fa)


def time_test():
    seq_lens = [100, 300, 1000, 3000, 10000, 30000, 100000]
    times = list()
    for sl in seq_lens:
        seq = "".join([choice('ACGT') for _ in range(sl)])
        start_time = time.time()
        _ = compute_failure_array(seq)
        times.append(round(time.time() - start_time, 4))

    print("time\tseq len")
    for t, l in zip(times, seq_lens):
        print(f'{t}\t{l}')


if __name__ == '__main__':
    # test()        # tests code functionality, should print the right answer.
    # time_test()   # times code execution on random sequences of increasing size.
    main()
