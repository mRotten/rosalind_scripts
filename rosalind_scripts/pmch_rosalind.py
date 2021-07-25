from math import factorial as fact


def compute_perfect_pairings(seq):
    # Assume the number of 'A's == number of 'U's.
    return fact(seq.count('A')) * fact(seq.count('G'))


# every A can pair with every U
# every G can pair with every C
# A1, A2, A3, U1, U2, U3:
#   A1:U1
#       A2:U2, A3:U3
#           G1:C1, G2:C2
#           G1:C2, G2:C1
#       A2:U3, A3:U2
#           G1:C1, G2:C2
#           G1:C2, G2:C1
#   A1:U2
#       A2:U1, A3:U3
#           G1:C1, G2:C2
#           G1:C2, G2:C1
#       A2:U3, A3:U1
#           G1:C1, G2:C2
#           G1:C2, G2:C1
#   A1:U3
#       A2:U1, A3:U2
#           G1:C1, G2:C2
#           G1:C2, G2:C1
#       A2:U2, A3:U1
#           G1:C1, G2:C2
#           G1:C2, G2:C1
