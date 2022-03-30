from .base import np, Constants

def strcomp(x: str) -> tuple:
    _r = len(x) % 3
    if _r:
        x += " " * (3 - _r)
    return x, _r

def str2arr(x: str) -> np.ndarray:
    return np.array([ Constants.MAP_CHAR_NUM[each] for each in x ]).reshape((len(x) // 3, 3))

def arrencode(x: np.ndarray) -> np.ndarray:
    return ((x @ Constants.MAT_KEY) % 128).flatten()

def num2cry(x: int) -> str:
    flag = False
    if x >= 64:
        flag = True
        x -= 64
    fnum = x // 24 + 1
    x %= 24
    res = Constants.LIST_ALL[x]
    res = res[ : fnum ] + "*" + res[ fnum : ]
    if flag:
        res = res.replace("*", "3") + "9"
    else:
        res = "3" + res.replace("*", "9")
    return res

def arr2cry(x: np.ndarray, r: int) -> str:
    res = ""
    for each in x:
        res += num2cry(each)
    res = Constants.LIST_ALL[0] + res + ["4ever", "4love", "4star"][r]
    return res

def encode(x: str) -> str:
    x, r = strcomp(x)
    x = str2arr(x)
    x = arrencode(x)
    x = arr2cry(x, r)
    return x
