print("This program doesn't really work.")


def get_score_list(num_list):
    scores = []
    inc_indices = []
    dec_indices = []
    for i, num in enumerate(num_list):
        score = 0
        preceding_index = -1
        for j in range(i):
            if num_list[j] < num and scores[j] > score:
                score = scores[j]
                preceding_index = j
        scores.append(score + 1)
        inc_indices.append(preceding_index)
    return scores, inc_indices, dec_indices


def get_longest_subsequence(sequence, scores, indices):

    max_len = max(scores)         # the length of the maximum length subsequence
    i = scores.index(max_len)     # the index of the last num of the longest subsequence
    subseq = list()

    while i >= 0:
        subseq.insert(0, sequence[i])
        i = indices[i]
    return subseq


test = [18, 93, 81, 12, 97, 64, 83, 38, 76, 4, 26, 29, 59, 30, 70, 90, 87, 92, 24, 84, 0, 95, 27, 6, 20, 43, 37,
        58, 66, 8, 1, 45, 28, 40, 91, 61, 89, 36, 23, 31, 39, 55, 69, 51, 9, 62, 57, 56, 25, 47, 7, 14, 60, 10, 19,
        11, 53, 78]


if __name__ == '__main__':
    s, i, d = get_score_list(test)
    lis = get_longest_subsequence(test, s, i)
    lds = get_longest_subsequence(test, s, d)
    print(s)
    print(i)
    print(lis)