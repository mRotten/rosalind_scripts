from Bio import SeqIO
import argparse


def get_p_dist(seq1, seq2):
    assert len(seq1) == len(seq2)
    ham = sum([nt1 != nt2 for nt1, nt2 in zip(seq1, seq2)])
    pdist = round(ham / len(seq1), 5)
    return str(pdist).ljust(7, "0")


def get_inputs(fasta_path):
    return [str(rec.seq) for rec in SeqIO.parse(fasta_path, 'fasta')]


def get_dist_matrix(fasta_path):
    dist_matrix = list()
    sequences = get_inputs(fasta_path)
    for seq1 in sequences:
        row = list()
        for seq2 in sequences:
            row.append(get_p_dist(seq1, seq2))
        dist_matrix.append(" ".join(row))
    return "\n".join(dist_matrix)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_fasta')
    parser.add_argument('-o', '--output_path', default=None)
    args = parser.parse_args()
    dm = get_dist_matrix(args.input_fasta)

    if args.output_path:
        with open(args.output_path, 'w') as outfile:
            outfile.write(dm + "\n")
    else:
        print(dm)


if __name__ == '__main__':
    main()
