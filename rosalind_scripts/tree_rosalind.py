import argparse


def group_adj_list(adj_list):
    clusters = []
    for p1, p2 in adj_list:
        match = False
        for cl in clusters:
            if p1 in cl or p2 in cl:
                cl.extend([p1, p2])
                match = True
        if not match:
            clusters.append([p1, p2])
    for i, cl in enumerate(clusters):
        clusters[i] = list(set(cl))
    return clusters


def add_lone_nodes(node_count, clusters):
    nodes = list(range(1, node_count+1))
    for cl in clusters:
        for n in cl:
            if n in nodes:
                _ = nodes.pop(nodes.index(n))
    for n in nodes:
        clusters.append([n])
    return clusters


def parse_input_file(path):
    with open(path, 'r') as infile:
        raw = infile.read()
    adj_list1 = raw.strip().split("\n")
    node_count = int(adj_list1.pop(0))
    adj_list2 = [[int(x) for x in y.split(" ")] for y in adj_list1]
    return node_count, adj_list2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    args = parser.parse_args()
    nc, al = parse_input_file(args.input_path)
    adj_clusters = group_adj_list(al)
    print(adj_clusters)
    clusters = add_lone_nodes(nc, adj_clusters)
    print(len(clusters) - 1)


def test():
    node_count = 10
    adj_list = [[1, 2], [2, 8], [4, 10], [5, 9], [6, 10], [7, 9]]
    adj_clusters = group_adj_list(adj_list)
    clusters = add_lone_nodes(node_count, adj_clusters)
    print(len(clusters) - 1)


if __name__ == '__main__':
    main()
    # test()
