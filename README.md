# `ichisaki`

A Simple Toolkit just for ***FUN***.

## Requirements

Ensure [NumPy](https://numpy.org/) ([NumPy on GitHub](https://github.com/numpy/numpy/)) is installed already before installing `ichisaki`.

One of most simple ways to install [NumPy](https://numpy.org/) is installing it with `conda`:

```sh
$ conda install numpy
```

## Installation

Currently `ichisaki` can be installed with `pip` as following:

```sh
$ pip install ichisaki
```

or [from source](https://github.com/sandyzikun/ichisaki/) like other packages.

## Importation

To access `ichisaki` and its functions import it in your Python code like this:

```py
>>> import icsk
```

## Functions

### Crypto

Functions encrypt and decrypt text based on Hill Cipher[^1]:

* Encrypt: `icsk.crypto.encode(x: str) -> str`
* Decrypt: `icsk.crypto.decode(x: str) -> str`

For instance:

```py
>>> icsk.crypto.encode("Sharing the World")
'icsk3isk9c3sci9kcs3ki9k3ics9sck3i9ks3ci9c3iks93s9cik3s9ickc3sik9ci3ks93kc9si3cik9sis3kc9s3kci9s3ick9si3ck9i3kcs94star'

>>> icsk.crypto.decode("icsk3isk9c3sci9kcs3ki9k3ics9sck3i9ks3ci9c3iks93s9cik3s9ickc3sik9ci3ks93kc9si3cik9sis3kc9s3kci9s3ick9si3ck9i3kcs94star")
'Sharing the World'

>>> icsk.crypto.encode("Tell Your World")
'icsk3ikc9s3cik9sic3ks9s3ick93ic9sk3ic9kss3cki93ik9scc3iks93i9csk3si9kc3sci9kk3ics93c9sik3i9csk4ever'

>>> icsk.crypto.decode("icsk3ikc9s3cik9sic3ks9s3ick93ic9sk3ic9kss3cki93ik9scc3iks93i9csk3si9kc3sci9kk3ics93c9sik3i9csk4ever")
'Tell Your World'
```

## Changelog

### Version 0.0.3

* Renamed API `.cipher.hill` to `.crypto`,
  including its functions `.encode()` & `.decode()`;
* Closed configuration of changing mode;

## References

[^1]: CTF Wiki [Hill 密码](https://ctf-wiki.org/crypto/classical/polyalphabetic/#hill)
