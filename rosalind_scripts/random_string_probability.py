import argparse
import math


def probability_of_nucleotide(nt, gc_frac):
    if nt in ("G", "C"):
        return gc_frac / 2
    else:
        return (1 - gc_frac) / 2


def probability_of_sequence(seq, alphabet_gc_frac):
    log_prob = 0
    for nt in seq:
        log_prob += math.log10(probability_of_nucleotide(nt, alphabet_gc_frac))
    return round(log_prob, 3)


def compute_multiple_probabilities(seq, alphabet_gc_fractions):
    seq_probs = list()
    for agf in alphabet_gc_fractions:
        seq_probs.append(probability_of_sequence(seq, agf))
    return seq_probs


def parse_input_file(path):
    with open(path, 'r') as infile:
        raw = infile.read().strip()
    seq, gc_fracs = raw.split("\n")
    return seq, [float(x) for x in gc_fracs.split(" ")]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    parser.add_argument('-o', '--output_path')
    args = parser.parse_args()
    seq, gc_fracs = parse_input_file(args.input_path)
    probs = compute_multiple_probabilities(seq, gc_fracs)

    with open(args.output_path, 'w') as outfile:
        outfile.write(" ".join([str(x) for x in probs]) + "\n")


if __name__ == '__main__':
    main()
