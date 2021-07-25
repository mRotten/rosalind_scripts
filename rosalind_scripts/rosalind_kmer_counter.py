import argparse
from Bio import SeqIO


def get_kmer_distribution(sequence, word_size):
    kmer_db = make_kmer_db(sequence, word_size)
    kcounts = get_kmer_counts(sequence, kmer_db, word_size)
    return kcounts


def get_sequence_from_fasta(fasta_path):
    file_info = SeqIO.parse(fasta_path, 'fasta')
    seqs = dict()
    for rec in file_info:
        seqs[rec.id] = rec.seq
    return seqs


def make_kmer_db(seq, ws):
    kd = dict()
    for i in range(len(seq) - ws + 1):
        ss = seq[i:i+ws]
        if ss not in kd.keys():
            kd[ss] = 0
        kd[ss] += 1
    return kd


def get_kmer_counts(seq, kd, ws):
    counts = list()
    for i in range(len(seq) - ws + 1):
        counts.append(kd[seq[i:i+ws]])
    return counts


def save_results(counts_list, output_path):
    with open(output_path, 'w') as outfile:
        outfile.write(" ".join([str(c) for c in counts_list]) + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--input_path", help="Fasta file containing the input sequence.", required=True)
    parser.add_argument('-k', "--k_val", help="Size of k (word/window size) for counting.", required=True)
    parser.add_argument('-o', "--output_path", help="Path to output results.", default=None)
    args = parser.parse_args()
