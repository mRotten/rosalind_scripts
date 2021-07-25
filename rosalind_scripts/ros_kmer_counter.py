import argparse
from Bio import SeqIO


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--fasta_path', help="Path of fasta file with sequence to count kmers", required=True)
    parser.add_argument('-k', '--word_size', help="Size of kmers to count; i.e. the value of k", default=4, type=int)
    parser.add_argument('-o', '--output_path', help="Path to save the result", default=None)
    args = parser.parse_args()
    get_kmer_distribution(args)


def get_kmer_distribution(args):
    seq_dict = {rec.id: rec.seq for rec in SeqIO.parse(args.fasta_path, 'fasta')}
    counts = count_kmers(seq_dict[list(seq_dict.keys())[0]], mer=args.word_size)
    save_results(counts, args.output_path)


def count_kmers(seq: str, mer=4) -> list:
    all4mers = [a + b + c + d for a in 'ACGT' for b in 'ACGT' for c in 'ACGT' for d in 'ACGT']
    count_dict = {x: 0 for x in all4mers}
    for i in range(len(seq)):
        try:
            count_dict[seq[i:i+mer]] += 1
        except KeyError:
            pass
    counts = [count_dict[x] for x in all4mers]
    return counts


def save_results(counts, path):
    counts = " ".join([str(c) for c in counts])
    if not path:
        print(counts)
    with open(path, 'w') as outfile:
        outfile.write(counts + "\n")


if __name__ == "__main__":
    main()
