from .conf import Constants

assert len(Constants.MAT_KEY) == 3, "" # TODO: Complete Assertion Messages
for k in range(3):
    assert len(Constants.MAT_KEY[k]) == 3, ""
    for l in range(3):
        assert isinstance(Constants.MAT_KEY[k][l], int), ""
assert isinstance(Constants.BIAS_MAPPING, int), ""

assert Constants.MODE in [0, 1]

Constants.STR_ICSK = [
    "icsk", # "いちさき" / "イチサキ"
    "miku",
    ][Constants.MODE]

assert isinstance(Constants.STR_ICSK, str), ""
assert len(Constants.STR_ICSK) == 4, ""
assert len(set(Constants.STR_ICSK)) == 4, ""
assert not(("3" in Constants.STR_ICSK) or ("9" in Constants.STR_ICSK)), ""

import re

Constants.PATTERN_ALPHABET_ONLY = re.compile(r"[^A-Za-z]")

import numpy as np

Constants.MAT_KEY = np.array(Constants.MAT_KEY)

det_key, det_key_inv = np.linalg.det(Constants.MAT_KEY).astype(int), 1
assert det_key % 2, ""
for k in range(128):
    if (k + 1) * det_key % 128 == 1:
        det_key_inv = k + 1
        break
Constants.MAT_KEY_INV = (np.linalg.inv(Constants.MAT_KEY) * det_key * det_key_inv).astype(int) % 128
del det_key, det_key_inv

Constants.MAP_CHAR_NUM, Constants.MAP_NUM_CHAR = dict(), dict()
for k in range(128):
    Constants.MAP_CHAR_NUM[chr(k)] = (k - Constants.BIAS_MAPPING) % 128
    Constants.MAP_NUM_CHAR[k] = chr((k + Constants.BIAS_MAPPING) % 128)

Constants.LIST_ALL = [ # All Permutation
    [ 0, 1, 2, 3 ],
    [ 0, 1, 3, 2 ],
    [ 0, 2, 1, 3 ],
    [ 0, 2, 3, 1 ],
    [ 0, 3, 1, 2 ],
    [ 0, 3, 2, 1 ],
    [ 1, 0, 2, 3 ],
    [ 1, 0, 3, 2 ],
    [ 1, 2, 0, 3 ],
    [ 1, 2, 3, 0 ],
    [ 1, 3, 0, 2 ],
    [ 1, 3, 2, 0 ],
    [ 2, 0, 1, 3 ],
    [ 2, 0, 3, 1 ],
    [ 2, 1, 0, 3 ],
    [ 2, 1, 3, 0 ],
    [ 2, 3, 0, 1 ],
    [ 2, 3, 1, 0 ],
    [ 3, 0, 1, 2 ],
    [ 3, 0, 2, 1 ],
    [ 3, 1, 0, 2 ],
    [ 3, 1, 2, 0 ],
    [ 3, 2, 0, 1 ],
    [ 3, 2, 1, 0 ],
    ]
for k in range(24):
    idxs = Constants.LIST_ALL[k]
    strnew = ""
    for idx in idxs:
        strnew += Constants.STR_ICSK[idx]
    Constants.LIST_ALL[k] = strnew
