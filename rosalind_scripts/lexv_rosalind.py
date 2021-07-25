import itertools
import argparse


def get_permutations(a, n):
    permutations = list()
    for i in range(n):
        r1 = itertools.product(a, repeat=i+1)
        r2 = ["".join(x) for x in r1]
        permutations.extend(r2)
    return permutations


def sort_permutations(alphabet, permutations, n):
    perms = [x.ljust(n, " ") for x in permutations]
    alpha = " " + alphabet
    for i in range(n)[::-1]:
        perms.sort(key=lambda x: alpha.find(x[i]))
    return [x.strip(" ") for x in perms]


def self_test():
    truth = ['D', 'DD', 'DDD', 'DDN', 'DDA', 'DN', 'DND', 'DNN', 'DNA', 'DA', 'DAD', 'DAN', 'DAA', 'N', 'ND', 'NDD',
             'NDN', 'NDA', 'NN', 'NND', 'NNN', 'NNA', 'NA', 'NAD', 'NAN', 'NAA', 'A', 'AD', 'ADD', 'ADN', 'ADA', 'AN',
             'AND', 'ANN', 'ANA', 'AA', 'AAD', 'AAN', 'AAA']
    a, n = 'DNA', 3
    p1 = get_permutations(a, n)
    p2 = sort_permutations(a, p1, n)
    for pt, pex in zip(truth, p2):
        print(pt, pex)


def parse_file(path):
    with open(path, 'r') as infile:
        raw = infile.read().strip().split("\n")
    return "".join(raw[0].split(" ")), int(raw[1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    parser.add_argument('-o', '--output_path')
    args = parser.parse_args()
    a, n = parse_file(args.input_path)
    p1 = get_permutations(a, n)
    p2 = sort_permutations(a, p1, n)
    with open(args.output_path, 'w') as outfile:
        outfile.write("\n".join(p2) + "\n")


if __name__ == '__main__':
    main()
