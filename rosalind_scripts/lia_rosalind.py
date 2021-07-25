from math import factorial as fact


def bernoulli_trial(prob_het, n, tot):
    """
    Gives the probability that exactly <n> individuals of a certain type will occur in a population of <tot>.
    :param prob_het: Probability of heterozygous. This is the probability that one individual will be a certain
        type.
    :param n: Number of individuals that must be of a certain type.
    :param tot: Total number of individuals in a population.
    :return: Probability that exactly <n> individuals of a certain type (e.g. heterozygous for both of two alleles
        will be found in a population of <tot> individuals.
    """
    prob = (prob_het ** n) * (1 - prob_het) ** (tot - n)
    perms = fact(tot) / (fact(tot - n) * fact(n))
    return prob * perms


def probability_at_least_n_hets(k, n):
    """
    Generation 0 starts with one AaBb, who mates with a non-familial AaBb to produce two offspring.
    Every generation thereafter, each offspring mates with a non-familial AaBb to produce two offspring.
    This function gives the probability that there will be at least <n> heterozygous family members in
    generation <k>.
    :param k: Generation number. First generation with 1 individual is generation 0.
    :param n: Generation k should contain at least n heterozygous individuals.
    :return: Probability that generation k has at least n heterozygous individuals.
    """
    overall_prob, tot = 0, 2 ** k
    for i in range(n, tot+1):
        overall_prob += bernoulli_trial(0.25, i, tot)
    return overall_prob


def test():
    print(probability_at_least_n_hets(2, 1))


if __name__ == '__main__':
    test()

# Probability of >= 1 het in generation 2:
# Probability of 1 het:
#   0.25 * 0.75 * 0.75 * 0.75 = 0.10547
#   0.75 * 0.25 * 0.75 * 0.75 = 0.10547
#   0.75 * 0.75 * 0.25 * 0.75 = 0.10547
#   0.75 * 0.75 * 0.75 * 0.25 = 0.10547
# Probability of 2 hets:
#   0.25 * 0.25 * 0.75 * 0.75 = 0.03516
#   0.25 * 0.75 * 0.25 * 0.75 = 0.03516
#   0.25 * 0.75 * 0.75 * 0.25 = 0.03516
#   0.75 * 0.25 * 0.25 * 0.75 = 0.03516
#   0.75 * 0.25 * 0.75 * 0.25 = 0.03516
#   0.75 * 0.75 * 0.25 * 0.25 = 0.03516
# Probability of 3 hets:
#   0.25 * 0.25 * 0.25 * 0.75 = 0.01172
#   0.25 * 0.25 * 0.75 * 0.25 = 0.01172
#   0.25 * 0.75 * 0.25 * 0.25 = 0.01172
#   0.75 * 0.25 * 0.25 * 0.25 = 0.01172
# Probability of 4 hets:
#   0.25 * 0.25 * 0.25 * 0.25 = 0.00391
