#include "qpbo/qpbo.h"

typedef qpbo::QPBO<double> SolverType;

extern "C" {

SolverType* qpbo_create(int node_num_max, int edge_num_max)
{
	return new SolverType(node_num_max, edge_num_max);
}

void qpbo_destroy(SolverType* g)
{
	delete g;
}

int qpbo_add_node(SolverType* g, int num)
{
	return g->AddNode(num);
}

int qpbo_get_node_num(SolverType* g)
{
	return g->GetNodeNum();
}

void qpbo_add_unary_term(SolverType* g, int i, double e0, double e1)
{
	g->AddUnaryTerm(i, e0, e1);
}

void qpbo_add_pairwise_term(SolverType* g, int i, int j, double e00, double e01, double e10, double e11)
{
	g->AddPairwiseTerm(i, j, e00, e01, e10, e11);
}

void qpbo_merge_parallel_edges(SolverType* g)
{
	g->MergeParallelEdges();
}

int qpbo_get_label(SolverType* g, int i)
{
	return g->GetLabel(i);
}

void qpbo_solve(SolverType* g)
{
	g->Solve();
}

void qpbo_compute_weak_persistencies(SolverType* g)
{
	g->ComputeWeakPersistencies();
}

}
