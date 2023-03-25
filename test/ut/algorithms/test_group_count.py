from algorithms.group_count import group_count


def test_one_node_graph_returns_one_group():
    groups = group_count(["1"])

    assert groups == 1


def test_two_unconnected_graphs_returns_two_groups():
    groups = group_count(["10", "01"])

    assert groups == 2


def test_three_groups_defined_out_of_order_returns_3_groups():
    groups = group_count(["1000","0100","0010","1001"])

    assert groups == 3


def test_two_groups_chained_returns_2_groups():
    groups = group_count(["1100","0110","0010","0001"])

    assert groups == 2
