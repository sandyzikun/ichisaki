# `ichisaki`

A Simple Toolkit just for ***FUN***.

## Requirements

Ensure [NumPy](https://numpy.org/) ([NumPy on GitHub](https://github.com/numpy/numpy/)) is installed already before installing `ichisaki`.

One of most simple ways to install [NumPy](https://numpy.org/) is installing it with `conda`:

```sh
$ conda install numpy
```

## Installation

Currently the latest version of `ichisaki` can be installed with `pip` as following:

```sh
$ pip install ichisaki --upgrade
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
* File Encrypt: `icsk.crypto.fencode(filepath: str, outpath:str=None, forcemode:bool=True) -> "FileIOWrapper"`
* File Decrypt: `icsk.crypto.fdecode(filepath: str, outpath:str=None, forcemode:bool=True) -> "FileIOWrapper"`

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

```py
>>> fp = "./speech.txt"

>>> fl = open(fp, "r")

>>> print(fl.read())
Before I talk about the things we human beings like or love, let us make it clear that in different time, places, and conditions, we have different opinions on the same person or the same thing.

Okay, I'm now talking about the thing I like most when I was coding in the lab of my high school, 4 years before.

It's a song called "ODDS&ENDS" written by the artist "ryo" who belongs to an acg producing group called "supercell", telling a story between him and a virtual singer called Hatsune Miku.

Their story lasts from fourteen years ago. He, the artist called "ryo", was once an ordinary and obscure composer. Nobody was willing to sing his song, nobody support him and his artworks. His song could be never used or sung until he met the VOCALOID program and a diva called Hatsune Miku in it. Through his great efforts, their song became popular quickly.

This was the beginning of their story. Nevertheless the artist "ryo" got bored with Miku, even he once lost his original intention of producing songs. Finally he recalled the hard time with Miku and composed the song for her, showing his gratitude.

When I listened this song for the first time, I was programming to learn the algorithm DFS, in short of Depth First Search. It's an algorithm based on the algorithm "recursion" we learnt yesterday. I couldn't process all the details in the program when I deal with the problem related to it. I got tired just like "ryo" used to. I met this song exactly the time I was to give up. With its strength inner, I tried to calm down and rearrange what I learnt. Finally I overcame the problem.

>>> fl.close()

>>> fl = icsk.crypto.fencode(fp)

>>> fl
<_io.TextIOWrapper name='./speech.txt.mikucrypto' mode='w' encoding='UTF-8'>

>>> fl.close()

>>> !cat ./speech.txt.mikucrypto
icsk3ck9is3k9isci3skc9s3cki93k9cis3ci9ks3i9cskcks3i9ick3s9k3cis9ki3sc93iks9cc3ksi93k9sic3ic9ksi3sck9ick3s93kc9isk3cis93sk9icikc3s9c3sik9ci3ks93kc9sik3cis93i9cskick3s9s3cik9ick3s9i3sck93i9csk3i9ksck3cis93i9cskic3sk9ik3sc9s3ikc9ik3sc9sck3i93i9cskc3isk93k9scic3ski9sic3k9s3ikc9k3isc93sc9iksi3ck9c3ski9isk3c93ics9k3i9cskkc3si93ic9ks3i9csksi3ck9cks3i9k3sic9cks3i93sk9ci3i9csksi3ck9ick3s9k3cis93sk9iciks3c9k3isc93sc9iksi3kc9i3cks9ck3si9ics3k93i9cskis3kc9si3kc93i9cskc3ski93sc9kii3ksc9s3ikc9i3skc93i9csksic3k93sic9ki3cks9sci3k9sic3k9c3ski9sic3k93c9iski3kcs9ck3si9cik3s9c3isk9is3kc9ks3ci9i3ksc9ikc3s93cki9s3i9csksic3k93sik9cs3ikc9sk3ci9cs3ki93i9cskics3k93ik9csi3cks9c3ksi93sk9ick3isc9c3kis93i9kcsi3cks9kc3is93c9kis3i9cskc3ski93ki9css3cik9sk3ic93ik9sck3cis93i9skc3i9csks3cik93k9csisc3ki93i9csk3i9ksck3cis93i9cskic3sk9c3ski9k3sic9cks3i93ik9sci3kcs9ck3si9cik3s9c3isk9is3kc9ks3ci9i3ksc9ikc3s93cki9s3i9cskkc3si93k9scic3ski9sic3k9s3cki9s3cki93c9sik3c9ski3i9cskkc3si93k9csi3i9csksic3k93sic9ki3ksc93c9kiscks3i9i3cks9sk3ci93i9sck3i9cskics3k93k9csik3ics93ik9scc3kis9s3cik93ik9cs3sck9ik3ics93si9cksi3ck9c3sik9ci3ks93kc9sik3isc9sk3ci93ks9ici3ksc93c9kissic3k9c3sik9ki3sc93ci9ksc3iks93csi9k3cs9ikki3cs9cs3ki9i3sck9i3cks93s9ikc3iks9c3i9cskcks3i9csi3k9s3ikc93is9ck3cis9ks3cki93ck9si3c9iksk3cis9ki3sc93iks9cc3ksi9ick3s93cik9sc3iks93s9cikcsk3i9i3sck9ick3s93kc9isk3cis93sk9icikc3s9c3sik9ci3ks93kc9sik3cis93i9cskick3s9s3cik9ick3s9ks3ci93sk9cik3ics93k9cisc3ski9isk3c93ics9k3i9csksc3ki93i9kcsk3isc93ck9is3s9ickk3sci93c9isk3i9kscs3cik93ik9cs3ic9ks3i9csk3i9kscs3kic9k3isc93sc9ikis3kc9s3cki9ki3cs93si9kcs3cik9ick3s9ks3ci9c3ski9sic3k93c9iskk3cis93i9cskkc3si93i9csksi3ck9kc3si9i3sck93i9kcsci3ks9c3isk93s9icksik3c9ic3ks93isc9k3s9kicc3ski9sc3ki93s9cki3i9cskcsk3i93ks9icc3sik9sik3c9k3sic9s3ick93sic9ks3ick93k9cis3sk9iccsk3i9i3ksc9s3ikc9i3skc9k3isc93sc9ikis3ck9i3ksc9ik3cs9kc3si9k3ics9isk3c93c9ksiki3cs93k9ics3isk9ck3cis93sik9c3isc9k3i9cski3skc9c3ski9k3isc93k9isc3kc9sic3iks93s9cikcks3i9i3cks9sc3ik93i9cski3ksc9k3sic93s9ick3i9sck3s9kciis3kc93si9ckcs3ki9ick3s93si9kck3cis9ki3cs93isk9ckc3is93ki9csk3sci93si9ckck3si9k3cis93si9ckic3ks9s3cik93ik9cs3isc9kic3ks93isc9k3ik9csc3sik9ci3ks93kc9sii3cks9csi3k93sci9kc3ski93c9ksi3c9iks3i9csk3c9isksi3ck9ic3ks93ci9ks3s9kci3i9csk3i9ksck3sci9s3cki93ci9sk3cki9si3ksc9ks3ic93ck9sis3cik9ick3s9i3sck93i9csksic3k9i3skc93i9cski3skc93k9sci3i9cski3skc93s9ickc3iks93s9cik3c9sikk3ics93s9kci3is9kck3csi9isk3c9s3ick9s3cik9ick3s9ks3ci9c3iks93i9kcssk3ci9k3csi93is9ckcsi3k9i3skc9c3ski93kc9sis3ick9sc3ki93s9kci3i9csk3c9isksi3kc9k3csi93is9ck3sik9ck3ics9kc3si93ics9ks3ick9sic3k93s9cik3s9ick3ic9sk3ikc9si3ksc9ks3ic93cs9ikc3ski9sic3k9s3ikc93i9cski3skc9c3ski9k3isc93ck9isis3kc9k3ics93ks9ci3ick9si3sck9k3isc9s3kci9k3sci9sik3c9ki3cs9s3cik93ik9cs3csi9kc3ski9csk3i9sik3c9i3cks9kc3is93c9kis3i9cski3skc9c3ski9k3sic93c9iks3k9isck3cis93sc9kici3sk9s3ick93ic9sk3isk9cc3ski9sic3k9s3ikc9i3ksc93i9csk3c9kisi3skc9c3ski93kc9sis3ick9sc3ki93s9kci3i9cskcsi3k93sk9cik3cis93cs9kics3ik9s3cik9ki3sc9ik3sc93kc9si3iks9ci3kcs9k3csi9k3cis93s9kicki3cs9ics3k9kc3is9i3ksc9si3kc93c9ksi3i9cskcsk3i93sck9is3cki93k9cis3isk9c3i9csksi3ck9kc3si9k3isc93ck9isci3ks93i9cskk3ics9c3sik9s3cki93i9ksc3kc9sic3isk9csk3i9s3ick9k3ics93cs9ikc3ski9i3ksc9ikc3s9sc3ik9ic3ks93i9ckscis3k9k3ics93ik9sccks3i9i3cks9k3sci9k3sic93s9cik3ik9cs3ic9ski3ksc93ks9ic3k9cisk3cis93i9cskkc3si93i9cski3skc93is9kck3cis93i9skc3i9kcsk3cis93sk9icck3si9i3cks9sc3ik93i9cski3ksc9k3sic93s9ick3i9sckcki3s9c3ksi9s3cki93si9ck3k9sic3i9csk3i9kscs3kic9k3isc93sc9iksc3ki9s3cik9si3kc93s9kic3i9cski3skc93k9sci3i9cskkc3si93ic9ksi3kcs9ck3si9sck3i9i3cks9csi3k9i3skc93i9cski3skc93k9scii3kcs93c9sikks3ci9i3sck9sik3c93sci9kk3csi93cs9iks3cki93i9cskc3ski93ki9css3ikc93c9kis3c9iksk3isc9iks3c9k3sci93s9cik3ik9cs3ci9sks3cki9si3ck93ic9ksi3kcs93k9isci3cks9k3sci9ick3s9k3cis93i9csk3i9kscic3sk9s3ick9sic3k9k3csi9s3cik9ick3s9ks3ci9k3cis93k9csisc3ki9k3isc93i9ckscik3s9c3iks93s9cik3i9cskc3ski93c9ksi3isk9ck3isc93k9isc3kc9sic3iks93isc9k3si9cks3cik93c9skicsk3i9s3cki9ki3cs93iks9c3i9cskcsk3i9i3csk9s...
```

## Changelog

### Version 0.0.8

* Added API for File Encoding (`.crypto.fencode(...)`) and Decoding (`.crypto.fdecode(...)`);

### Version 0.0.3

* Renamed API `.cipher.hill` to `.crypto`,
  including its functions `.encode()` & `.decode()`;
* Closed configuration of mode changing;

## References

[^1]: CTF Wiki [Hill 密码](https://ctf-wiki.org/crypto/classical/polyalphabetic/#hill)
