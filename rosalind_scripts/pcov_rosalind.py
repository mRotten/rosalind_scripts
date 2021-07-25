import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    parser.add_argument('-o', '--output_path')
    args = parser.parse_args()

    seqs = get_input(args.input_path)
    adj_dict = get_adj_dict(seqs)
    contig = assemble_from_dict(adj_dict)

    with open(args.output_path, 'w') as outfile:
        outfile.write(contig + "\n")


def test():
    inpath = "C:\\Users\\mlalonde\\PycharmProjects\\rosalind_problems\\rosalind_test_files\\pcov_example.txt"

    seqs = get_input(inpath)
    adj_dict = get_adj_dict(seqs)
    contig = assemble_from_dict(adj_dict)

    print(contig)


def assemble_from_dict(adj_dict):
    seed = list(adj_dict.keys())[0]
    suffix = adj_dict[seed]
    contig = seed[-1]
    while suffix != seed:
        contig += suffix[-1]
        suffix = adj_dict[suffix]
    return contig


def get_adj_dict(seqs):
    adj_dict = dict()
    for seq in seqs:
        pref, suff = seq[:-1], seq[1:]
        if pref not in adj_dict.keys():
            adj_dict[pref] = suff
    return adj_dict


def get_input(path):
    with open(path, 'r') as infile:
        seqs = infile.read().strip().split("\n")
    return seqs


if __name__ == '__main__':
    main()
    #test()