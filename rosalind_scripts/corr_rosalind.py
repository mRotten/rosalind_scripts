from Bio import SeqIO
from Bio.Seq import Seq
import argparse


def get_correct_seq(incorrect_seq, correct_sequences):
    for cseq in correct_sequences:
        if sum([nti != ntc for nti, ntc in zip(incorrect_seq, cseq)]) == 1:
            return cseq
        rc_cseq = str(Seq(cseq).reverse_complement())
        if sum([nti != ntc for nti, ntc in zip(incorrect_seq, rc_cseq)]) == 1:
            return rc_cseq


def __get_sequences(path):
    raw_seqs = SeqIO.parse(path, 'fasta')
    for seq in raw_seqs:
        yield seq


def get_correct_incorrect(path):
    inventory = dict()

    for s in __get_sequences(path):
        ss = str(s.seq)
        src = str(s.reverse_complement().seq)

        if ss in inventory.keys():
            inventory[ss] += 1
        elif src in inventory.keys():
            inventory[src] += 1
        else:
            inventory[ss] = 1

    incorrect = [k for k, v in inventory.items() if v == 1]
    correct = [k for k, v in inventory.items() if v > 1]

    return correct, incorrect


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--fasta_path')
    parser.add_argument('-o', '--output_path')
    args = parser.parse_args()

    correct_seqs, incorrect_seqs = get_correct_incorrect(args.fasta_path)

    open(args.output_path, 'w').close()
    with open(args.output_path, 'a') as outfile:
        for iseq in incorrect_seqs:
            cseq = get_correct_seq(iseq, correct_seqs)
            outfile.write(f'{iseq}->{cseq}\n')


def test():
    fasta_path = "../rosalind_test_files/corr_example_file.fasta"
    output_path = "../rosalind_test_files/corr_example_result.txt"

    correct_seqs, incorrect_seqs = get_correct_incorrect(fasta_path)

    open(output_path, 'w').close()
    with open(output_path, 'a') as outfile:
        for iseq in incorrect_seqs:
            cseq = get_correct_seq(iseq, correct_seqs)
            outfile.write(f'{iseq}->{cseq}\n')


if __name__ == '__main__':
    main()
