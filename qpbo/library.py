import ctypes
import os.path


library_path = os.path.join(os.path.split(__file__)[0], 'libqpbo.so')

library = ctypes.CDLL(library_path)

library.qpbo_create.argtypes = [ctypes.c_int, ctypes.c_int]
library.qpbo_create.restype = ctypes.c_void_p

library.qpbo_destroy.argtypes = [ctypes.c_void_p]

library.qpbo_add_node.argtypes = [ctypes.c_void_p, ctypes.c_int]
library.qpbo_add_node.restype = ctypes.c_int

library.qpbo_get_node_num.argtypes = [ctypes.c_void_p]
library.qpbo_get_node_num.restype = ctypes.c_int


library.qpbo_add_unary_term.argtypes = [ctypes.c_void_p, ctypes.c_int,
                                        ctypes.c_double, ctypes.c_double]

library.qpbo_add_pairwise_term.argtypes = [ctypes.c_void_p,
                                           ctypes.c_int, ctypes.c_int,
                                           ctypes.c_double, ctypes.c_double,
                                           ctypes.c_double, ctypes.c_double]

library.qpbo_merge_parallel_edges.argtypes = [ctypes.c_void_p]

library.qpbo_get_label.argtypes = [ctypes.c_void_p, ctypes.c_int]
library.qpbo_get_label.restype = ctypes.c_int

library.qpbo_solve.argtypes = [ctypes.c_void_p]

library.qpbo_compute_weak_persistencies.argtypes = [ctypes.c_void_p]
