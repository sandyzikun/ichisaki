from .base import np, Constants

def cry2num(x: str) -> int:
    flag, fnum = False, 0
    if x[0] == "3":
        x = x[ 1 : ].replace("9", "*")
    else:
        flag = True
        x = x[ : (-1) ].replace("3", "*")
    for k in range(1, 4):
        if x[k] == "*":
            fnum = k - 1
            x = x[ : k ] + x[ (k + 1) : ]
            break
    res = 0
    for k in range(24):
        if x == Constants.LIST_ALL[k]:
            res = k
            break
    res += fnum * 24
    if flag:
        res += 64
    return res

def cry2arr(x: str) -> tuple:
    _r = {
        "4ever": 0,
        "4love": 2,
        "4star": 1,
        }[x[ (-5) : ]]
    return np.array([ cry2num(x[ k * 6 + 4 : k * 6 + 10 ]) for k in range((len(x) - 9) // 6) ]), _r

def arr2str(x: np.ndarray, r: int) -> str:
    x = (x.reshape((len(x) // 3, 3)) @ Constants.MAT_KEY_INV) % 128
    x = "".join(Constants.MAP_NUM_CHAR[each] for each in x.flatten())
    if r:
        x = x[ : (-r) ]
    return x

def decode(x: str) -> str:
    x, r = cry2arr(x)
    x = arr2str(x, r)
    return x
