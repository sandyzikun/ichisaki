from .encoder import encode
from .decoder import decode
del base, decoder, encoder

def fencode(filepath: str, outpath:str=None, forcemode:bool=True) -> "FileIOWrapper":
    """
    Encoding a File at the Specified Path.

    Parameters
    ----------
    * filepath: Path of the File to be Encoded;
    * outpath: Path of the Output File, which Loads the Encoded Cipher;
    * forcemode;

    Returns
    -------
    * fout: The Text-IO Wrapper of the Output File.

    See Also
    --------
    `.crypto.fdecode(...)`

    Examples
    --------
    >>> import icsk
    >>> fp = "./speech.txt"
    >>> fl = open(fp, "r")
    >>> print(fl.read())
    Before I talk about the things we human beings like or love, let us make it clear that in different time, places, and conditions, we have different opinions on the same person or the same thing.
    ...
    When I listened this song for the first time, I was programming to learn the algorithm DFS, in short of Depth First Search. It's an algorithm based on the algorithm "recursion" we learnt yesterday. I couldn't process all the details in the program when I deal with the problem related to it. I got tired just like "ryo" used to. I met this song exactly the time I was to give up. With its strength inner, I tried to calm down and rearrange what I learnt. Finally I overcame the problem.
    >>> fl.close()
    >>> fl = icsk.crypto.fencode(fp)
    >>> fl
    <_io.TextIOWrapper name='./speech.txt.mikucrypto' mode='w' encoding='UTF-8'>
    >>> fl.close()
    >>> !cat ./speech.txt.mikucrypto
    icsk3ck9is3k9isci3skc9s3cki93k9cis3ci9k...
    """

    outpath = outpath or (filepath + ".mikucrypto")
    fout = open(outpath, "w" if forcemode else "x")

    with open(filepath, "r") as flin:
        fout.write(encode(flin.read()))
        flin.close()

    return fout

def fdecode(filepath: str, outpath:str=None, forcemode:bool=True) -> "FileIOWrapper":
    """
    Usages are Similar to `.crypto.fencode(...)`.
    """
    outpath = outpath or (filepath + ".txt")
    fout = open(outpath, "w" if forcemode else "x")
    with open(filepath, "r") as flin:
        fout.write(decode(flin.read()))
        flin.close()
    return fout
