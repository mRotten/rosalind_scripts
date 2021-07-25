import argparse

mono_masses = {'A': 71.03711,  'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
               'G': 57.02146,  'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406,
               'M': 131.04049, 'N': 114.04293, 'P': 97.05276,  'Q': 128.05858, 'R': 156.10111,
               'S': 87.03203,  'T': 101.04768, 'V': 99.06841,  'W': 186.07931, 'Y': 163.06333}

mass_lookup = [(k, v) for k, v in mono_masses.items()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    args = parser.parse_args()
    spectrum = get_input(args.input_path)
    pairs = get_b_y_ion_pairs(spectrum)
    print(infer_sequence(pairs))


def get_input(path):
    with open(path, 'r') as infile:
        raw = infile.read().strip().split("\n")
    spectrum = [float(x) for x in raw]
    spectrum.sort()
    return spectrum


def infer_sequence(ion_pairs):
    ip0 = ion_pairs[0]
    seq, used = '', [ion_pair_comp(ip0), ]
    for ip1 in ion_pairs[1:]:
        aa = get_likely_aa(ip1[0] - ip0[0])
        if aa and ip1 not in used:
            seq += aa
            used.append(ion_pair_comp(ip1))
            ip0 = ip1
    return seq


def ion_pair_comp(pair):
    return pair[1], pair[0], pair[2]


def get_b_y_ion_pairs(spectrum):
    assert max(spectrum) == spectrum[-1]
    parent_mass = spectrum[-1]
    spec = spectrum[:-1]
    pairs = list()
    for mass in spec:
        comp_mass = get_closest_mass(parent_mass - mass, spec)
        pair = (mass, comp_mass, mass + comp_mass)
        pairs.append(pair)
    return pairs


def get_likely_aa(mass, max_diff=0.03):
    closest = min(mass_lookup, key=lambda x: abs(x[1] - mass))
    if abs(closest[1] - mass) > max_diff:
        return None
    else:
        return closest[0]


def get_closest_mass(target_mass, mass_list):
    return min(mass_list, key=lambda x: abs(x - target_mass))


def test():
    path = "../rosalind_test_files/full_example.txt"
    spectrum = get_input(path)
    pairs = get_b_y_ion_pairs(spectrum)
    print(infer_sequence(pairs))


if __name__ == '__main__':
    # test()
    main()
