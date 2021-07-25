import itertools
import argparse


def get_signed_permutations(n):
    signs = [x for x in itertools.product((-1, 1), repeat=n)]
    position_seed = list(range(1, n+1))
    positions = [x for x in itertools.permutations(position_seed, n)]

    signed_permutations = list()
    for stup in signs:
        for ptup in positions:
            signed_permutations.append([s * p for s, p in zip(stup, ptup)])
    return signed_permutations


def test():
    perms = get_signed_permutations(3)
    print(f"Number of permutations: {len(perms)}")
    for p in perms:
        print(" ".join([str(x) for x in p]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--length', type=int)
    parser.add_argument('-o', '--output_path')
    args = parser.parse_args()

    perms = get_signed_permutations(args.length)
    perms1 = [" ".join([str(x) for x in p]) for p in perms]
    perms2 = "\n".join([p for p in perms1])
    output_text = str(len(perms)) + "\n" + perms2 + "\n"

    with open(args.output_path, 'w') as outfile:
        outfile.write(output_text)


if __name__ == '__main__':
    main()
