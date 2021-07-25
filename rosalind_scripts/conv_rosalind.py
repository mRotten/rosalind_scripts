from statistics import mode
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    args = parser.parse_args()
    spec1, spec2 = get_inputs(args.input_path)
    offset_list = calculate_optimal_offset(spec1, spec2)
    if not all([x == offset_list[0] for x in offset_list]):
        print(offset_list)
        print("Offsets are not all exactly the same.")
    print(len(offset_list))
    print(offset_list[0])


def get_inputs(path):
    with open(path, 'r') as infile:
        raw = infile.read().strip().split("\n")
    spec1 = [float(x) for x in raw[0].split(" ")]
    spec2 = [float(x) for x in raw[1].split(" ")]
    return spec1, spec2


def calculate_optimal_offset(spec1, spec2):
    mink_diff = list()
    for s1 in spec1:
        for s2 in spec2:
            mink_diff.append(round(s1 - s2, 5))

    # Real MS mass differences are almost never exact, so I'm rounding to 3 sig figs.
    approx_mds = [round(x, 3) for x in mink_diff]
    approx_offset = mode(approx_mds)
    offset_index = [i for i, x in enumerate(approx_mds) if x == approx_offset]
    offsets = [x for i, x in enumerate(mink_diff) if i in offset_index]
    return offsets


if __name__ == '__main__':
    main()
