import argparse


def get_clusters(node_count, adj_list):
    tree = build_tree(node_count, adj_list)

    clusters, ignore = list(), list()

    for key_node, adjacents in tree.items():
        if key_node in ignore:
            continue
        new_cluster = assemble_cluster(tree, adjacents)
        clusters.append(new_cluster)
        ignore.extend(new_cluster)

    return clusters


def assemble_cluster(tree, adj_list):

    union, new_nodes = list(), list(set(adj_list))

    while len(new_nodes) > 0:
        union += new_nodes
        maybe_new = [x for n in new_nodes for x in tree[n]]
        new_nodes = list(set(maybe_new) - set(union))

    union.sort()

    return union


def build_tree(node_count, adj_list):
    tree = {x: [x] for x in range(1, node_count + 1)}
    for n1, n2 in adj_list:
        tree[n1].append(n2)
        tree[n2].append(n1)
    return tree


def unite(tree, node_list):
    all_nodes = list()
    for node in node_list:
        all_nodes.extend(tree[node])
    return sorted(list(set(all_nodes)))


def get_inputs(path):
    with open(path, 'r') as infile:
        raw1 = infile.read().strip().split("\n")
    node_count = int(raw1.pop(0))
    adj_list = [[int(x[0]), int(x[1])] for x in [adj.split(" ") for adj in raw1]]
    adj_list.sort()
    return node_count, adj_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_path')
    args = parser.parse_args()
    node_count, adj_list = get_inputs(args.input_path)
    clusters = get_clusters(node_count, adj_list)
    print(len(clusters) - 1)


def test():
    tp1 = "./rosalind_test_files/rosalind_tree_1.txt"
    tp2 = "./rosalind_test_files/rosalind_tree_2.txt"
    node_count_1, adj_list_1 = get_inputs(tp1)
    node_count_2, adj_list_2 = get_inputs(tp2)
    clusters1 = get_clusters(node_count_1, adj_list_1)
    clusters2 = get_clusters(node_count_2, adj_list_2)
    return clusters1, clusters2


if __name__ == '__main__':
    main()
    # test()
