import numpy as np
class Constants(object):
    MAT_KEY     = np.array([ 1,  2,   8, 0,  3,   9, 0, 0, 1 ]).reshape((3, 3))
    MAT_KEY_INV = np.array([ 1, 42, 126, 0, 43, 125, 0, 0, 1 ]).reshape((3, 3))
    MAP_CHAR_NUM = dict([ (chr(_), (_ - 32) % 128) for _ in range(128) ])
    MAP_NUM_CHAR = dict([ (_, chr((_ + 32) % 128)) for _ in range(128) ])
    LIST_ALL  = [ "".join([ "icsk"[_] for _ in eachlist ]) for eachlist in [ # All Permutations
                [ 0, 1, 2, 3 ], [ 0, 1, 3, 2 ], [ 0, 2, 1, 3 ], [ 0, 2, 3, 1 ], [ 0, 3, 1, 2 ], [ 0, 3, 2, 1 ],
                [ 1, 0, 2, 3 ], [ 1, 0, 3, 2 ], [ 1, 2, 0, 3 ], [ 1, 2, 3, 0 ], [ 1, 3, 0, 2 ], [ 1, 3, 2, 0 ],
                [ 2, 0, 1, 3 ], [ 2, 0, 3, 1 ], [ 2, 1, 0, 3 ], [ 2, 1, 3, 0 ], [ 2, 3, 0, 1 ], [ 2, 3, 1, 0 ],
                [ 3, 0, 1, 2 ], [ 3, 0, 2, 1 ], [ 3, 1, 0, 2 ], [ 3, 1, 2, 0 ], [ 3, 2, 0, 1 ], [ 3, 2, 1, 0 ],
                ]]