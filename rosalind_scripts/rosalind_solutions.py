

def kmer(seq, mer):
    """
    Given a sequence of characters, returns the kmer distribution in that sequence.
    :param seq: Sequence of characters (string).
    :param mer: Integer word size of required kmers.
    :return: String of space-separated numbers representing the kmer distribution in the sequence.
    """
    kfreqs = []
    for i in range(len(seq)- mer + 1):
        kfreqs.append(str(seq.count(seq[i:i+mer])))
    return " ".join(kfreqs)
