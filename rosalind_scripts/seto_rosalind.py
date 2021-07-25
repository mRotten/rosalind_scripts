import argparse


def get_union(a: set, b: set):
    return a | b


def get_intersection(a: set, b: set):
    return a & b


def get_difference(a: set, b: set):
    return a - b


def get_inputs(path):
    with open(path, 'r') as infile:
        raw = infile.read().strip().split("\n")

    superset = set(range(1, int(raw[0]) + 1))

    # Need to validate inputs so I can use eval.
    assert all([x in '0123456789 {},' for x in raw[1]])
    assert all([x in '0123456789 {},' for x in raw[1]])

    set_a, set_b = eval(raw[1]), eval(raw[2])

    return superset, set_a, set_b


def get_subsets(path):
    superset, set_a, set_b = get_inputs(path)
    result = list()
    result.append(get_union(set_a, set_b))
    result.append(get_intersection(set_a, set_b))
    result.append(get_difference(set_a, set_b))
    result.append(get_difference(set_b, set_a))
    result.append(get_difference(superset, set_a))
    result.append(get_difference(superset, set_b))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    parser.add_argument('-o', '--output_path', default=None)
    args = parser.parse_args()
    result = get_subsets(args.input_path)
    if not args.output_path:
        for sset in result:
            print(str(sset))
    else:
        open(args.output_path, 'w').close()
        with open(args.output_path, 'a') as outfile:
            for sset in result:
                outfile.write(str(sset) + "\n")


if __name__ == '__main__':
    main()
