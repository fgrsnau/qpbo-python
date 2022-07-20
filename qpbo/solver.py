from .library import library


class Solver:

    def __init__(self, node_num_max=0, edge_num_max=0):
        self._solver = library.qpbo_create(node_num_max, edge_num_max)

    def __del__(self):
        self.destroy()

    def destroy(self):
        if self._solver:
            library.qpbo_destroy(self._solver)

    def add_node(self, num):
        return library.qpbo_add_node(self._solver, num)

    def get_node_num(self):
        return library.qpbo_get_node_num(self._solver)

    def add_unary_term(self, i, e0, e1):
        library.qpbo_add_unary_term(self._solver, i, e0, e1)

    def add_pairwise_term(self, i, j, e00, e01, e10, e11):
        library.qpbo_add_pairwise_term(self._solver, i, j, e00, e01, e10, e11)

    def merge_parallel_edges(self):
        library.qpbo_merge_parallel_edges(self._solver)

    def get_label(self, i):
        label = library.qpbo_get_label(self._solver, i)

        # The label is negative for the "0.5" state. We map it to None here.
        if label < 0:
            label = None

        return label

    def get_solution(self):
        return [ self.get_label(i) for i in range(self.get_node_num()) ]

    def solve(self):
        return library.qpbo_solve(self._solver)

    def compute_weak_persistencies(self):
        return library.qpbo_compute_weak_persistencies(self._solver)
