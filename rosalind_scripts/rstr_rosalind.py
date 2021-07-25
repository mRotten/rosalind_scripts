from math import pow
import argparse


def get_inputs(path):
    with open(path, 'r') as infile:
        raw = infile.read().strip().split("\n")
    tot, gcfrac = raw[0].split(" ")
    tot, gcfrac = int(tot), float(gcfrac)
    seq = raw[1]
    return tot, gcfrac, seq


def calc_prob_one_or_more(num_sequences, gc_fraction, sequence):
    at, gc = (1-gc_fraction)/2, gc_fraction/2
    nt_probs = {'A': at, 'T': at, 'G': gc, 'C': gc}
    prob_of_seq = 1

    for nt in sequence:
        prob_of_seq *= nt_probs[nt]

    prob_not_seq = 1 - prob_of_seq
    overall_prob_not_seq = pow(prob_not_seq, num_sequences)
    overall_prob_seq = 1 - overall_prob_not_seq

    return round(overall_prob_seq, 3)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    args = parser.parse_args()
    tot, gc_frac, seq = get_inputs(args.input_path)
    print(calc_prob_one_or_more(tot, gc_frac, seq))


if __name__ == '__main__':
    main()
