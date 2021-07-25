from Bio import pairwise2
from Bio import SeqIO


def calc_percent_ident(alns):
    best = [(0, 0), (0, 0)]

    seq0_len = len(alns[0][0].replace('-', ''))
    seq1_len = len(alns[0][1].replace('-', ''))

    for i, pair in enumerate(alns):
        idents = 0
        for r0, r1 in zip(pair[0], pair[1]):
            if r0 == r1:
                idents += 1

        if best[0][1] < idents / seq0_len:
            best[0] = (i, idents / seq0_len)
        if best[1][1] < idents / seq1_len:
            best[1] = (i, idents / seq1_len)

    return best


def align(seq1, seq2):
    return pairwise2.align.globalms(str(seq1), str(seq2), 2, -1, -0.5, -0.1)


def get_from_fasta(path):
    seqs = []
    for record in SeqIO.parse(path, 'fasta'):
        seqs.append(record)
    return seqs


def align_and_calc_identity(path, s1_index, s2_index):
    assert type(s1_index) == int and type(s2_index) == int
    recs = get_from_fasta(path)
    alns = align(recs[s1_index].seq, recs[s2_index].seq)
    return calc_percent_ident(alns)
