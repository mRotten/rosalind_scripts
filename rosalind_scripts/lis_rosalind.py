
def get_longest_subset(array: list, inc_dec: str) -> list:
    scores = get_scores(array, inc_dec)
    subset = get_subset(array, scores)
    return subset


def get_scores(array: list, inc_dec: str) -> list:
    scores = list()
    for ael in array:

        if inc_dec == 'decreasing':
            all_prec = [scores[i] if array[i] > ael else 0 for i in range(len(scores))]
        else:
            all_prec = [scores[i] if array[i] < ael else 0 for i in range(len(scores))]
        all_prec.append(0)

        scores.append(max(all_prec) + 1)

    return scores


def get_subset(array: list, scores: list) -> list:
    next_score = max(scores)
    sequence = list()
    for sc, ael in zip(scores[::-1], array[::-1]):
        if sc == next_score:
            sequence.insert(0, ael)
            next_score -= 1
    return sequence


def rosalind(text: str):
    array = [int(x) for x in text.split(" ")]
    inc = get_longest_subset(array, 'increasing')
    print(" ".join([str(x) for x in inc]))
    dec = get_longest_subset(array, 'decreasing')
    print(" ".join([str(x) for x in dec]))


if __name__ == '__main__':
    test_ar1 = [16, 13, 4, 17, 5, 10, 14, 18, 7, 13]
    test_ar2 = [24, 9, 1, 35, 12, 21, 4, 36, 5, 27]
    test_st1 = "16 13 4 17 5 10 14 18 7 13"
    test_st2 = "24 9 1 35 12 21 4 36 5 27"
    rosalind(test_st1)
    rosalind(test_st2)

# lis test 1: [4, 5, 10, 14, 18]
# lds test 1: [16, 13, 10, 7]
# lis test 2: [1, 4, 5, 27]
# lds test 2: [35, 21, 5]
