import argparse

aa_mass_dict = {'A': 71.03711,   'C': 103.00919,     'D': 115.02694,     'E': 129.04259,     'F': 147.06841,
                'G': 57.02146,   'H': 137.05891,     'I': 113.08406,     'K': 128.09496,     'L': 113.08406,
                'M': 131.04049,  'N': 114.04293,     'P': 97.05276,      'Q': 128.05858,     'R': 156.10111,
                'S': 87.03203,   'T': 101.04768,     'V': 99.06841,      'W': 186.07931,     'Y': 163.06333}

aa_mass_list = [(mass, aa) for aa, mass in aa_mass_dict.items()]


def get_likely_aa(mass):
    return min(aa_mass_list, key=lambda x: abs(x[0] - mass))[1]


def infer_sequence(spectrum):
    spectrum.sort()
    diff_spec = [spectrum[i] - spectrum[i-1] for i in range(len(spectrum)) if i != 0]
    return [get_likely_aa(dmass) for dmass in diff_spec]


def get_input(path):
    with open(path, 'r') as infile:
        raw = infile.read().strip().split("\n")
    return [float(x) for x in raw]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    args = parser.parse_args()
    spectrum = get_input(args.input_path)
    print("".join(infer_sequence(spectrum)))


if __name__ == '__main__':
    main()
