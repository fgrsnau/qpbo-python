#!/usr/bin/env python3

import qpbo


def main():
    solver = qpbo.Solver()
    solver.add_node(2)

    solver.add_unary_term(0, 10, 20)
    solver.add_unary_term(1, 25,  5)
    solver.add_pairwise_term(0, 1, 0, 10, 10, 0)

    solver.solve()
    solver.compute_weak_persistencies()

    print(solver.get_solution())


if __name__ == '__main__':
    main()
