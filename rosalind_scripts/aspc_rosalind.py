import argparse
from scipy.special import comb
# Given n exons in a transcript, how many splice variants can we make with at least m exons?


def compute_num_splice_vars(n, m, mod=1000000):
    count = 0
    for i in range(m, n+1):
        count += comb(n, i, exact=True) % mod
    return count % mod


def get_inputs(path):
    with open(path, 'r') as infile:
        n, m = [int(x) for x in infile.read().strip().split(" ")]
    return n, m


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    args = parser.parse_args()
    n, m = get_inputs(args.input_path)
    print(compute_num_splice_vars(n, m))


def test():
    print(compute_num_splice_vars(6, 3))


if __name__ == '__main__':
    # test()
    main()
