import argparse
from Bio import SeqIO


def get_subseq_indices(seq, subseq):
    inds = list()
    lasti = 0
    for char in subseq:
        lasti = seq.find(char, lasti) + 1
        inds.append(lasti)
    return " ".join([str(x) for x in inds])


def get_seqs_from_fasta(path):
    raw = SeqIO.parse(path, 'fasta')
    return [x.seq for x in raw]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--fasta_path', required=True)
    parser.add_argument('-o', '--output_path', required=True)
    args = parser.parse_args()

    seq, subseq = get_seqs_from_fasta(args.fasta_path)
    output = get_subseq_indices(seq, subseq)

    with open(args.output_path, 'w') as outfile:
        outfile.write(output + "\n")


if __name__ == '__main__':
    main()
