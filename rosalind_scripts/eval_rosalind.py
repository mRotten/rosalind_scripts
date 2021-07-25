import argparse


def calc_seq_prob(seq, gc_frac):
    prob = 1
    at_prob = (1 - gc_frac) / 2
    gc_prob = gc_frac / 2
    for nt in seq:
        if nt in 'AT':
            prob *= at_prob
        else:
            prob *= gc_prob
    return prob


def calc_sseq_prob(subseq: str, seq_len: int, gc_frac: float):
    sseq_count = seq_len - len(subseq) + 1
    return round(sseq_count * calc_seq_prob(subseq, gc_frac), 3)


def get_inputs(path):
    with open(path, 'r') as infile:
        raw = infile.read().strip().split("\n")
    n = int(raw[0])
    subseq = raw[1]
    gc_fracs = [float(x) for x in raw[2].split(" ")]
    return n, subseq, gc_fracs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    args = parser.parse_args()
    seq_len, subseq, gc_fracs = get_inputs(args.input_path)
    probs = list()
    for gcf in gc_fracs:
        probs.append(calc_sseq_prob(subseq, seq_len, gcf))
    print(" ".join([str(x) for x in probs]))


if __name__ == '__main__':
    main()
