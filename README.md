# ichisaki

A Simple Toolkit for ***FUN***.

```py
>>> import icsk
```

## Crypto

Some ways to encrypt and decrypt text.

### Hill

Functions based on Hill Cipher[^1]:

* Encrypt: `icsk.cipher.hill.encode(x: str) -> str`
* Decrypt: `icsk.cipher.hill.decode(x: str) -> str`

For instance:

```py
>>> icsk.cipher.hill.encode("Sharing the World")
'icsk3isk9c3sci9kcs3ki9k3ics9sck3i9ks3ci9c3iks93s9cik3s9ickc3sik9ci3ks93kc9si3cik9sis3kc9s3kci9s3ick9si3ck9i3kcs94star'

>>> icsk.cipher.hill.decode("icsk3isk9c3sci9kcs3ki9k3ics9sck3i9ks3ci9c3iks93s9cik3s9ickc3sik9ci3ks93kc9si3cik9sis3kc9s3kci9s3ick9si3ck9i3kcs94star")
'Sharing the World'

>>> icsk.cipher.hill.encode("Tell Your World")
'icsk3ikc9s3cik9sic3ks9s3ick93ic9sk3ic9kss3cki93ik9scc3iks93i9csk3si9kc3sci9kk3ics93c9sik3i9csk4ever'

>>> icsk.cipher.hill.decode("icsk3ikc9s3cik9sic3ks9s3ick93ic9sk3ic9kss3cki93ik9scc3iks93i9csk3si9kc3sci9kk3ics93c9sik3i9csk4ever")
'Tell Your World'
```

Or you can choose another mode via modifying `icsk/cipher/hill/conf.py`:

```py
class Constants(object):
    ...
    MODE = 1 # 0
```

And then ...

```py
>>> icsk.cipher.hill.encode("Sharing the World")
'miku3mku9i3kim9uik3um9u3mik9kiu3m9uk3im9i3muk93k9imu3k9miui3kmu9im3uk93ui9km3imu9kmk3ui9k3uim9k3miu9km3iu9m3uik94star'

>>> icsk.cipher.hill.decode("miku3mku9i3kim9uik3um9u3mik9kiu3m9uk3im9i3muk93k9imu3k9miui3kmu9im3uk93ui9km3imu9kmk3ui9k3uim9k3miu9km3iu9m3uik94star")
'Sharing the World'

>>> icsk.cipher.hill.encode("Tell Your World")
'miku3mui9k3imu9kmi3uk9k3miu93mi9ku3mi9ukk3ium93mu9kii3muk93m9iku3km9ui3kim9uu3mik93i9kmu3m9iku4ever'

>>> icsk.cipher.hill.decode("miku3mui9k3imu9kmi3uk9k3miu93mi9ku3mi9ukk3ium93mu9kii3muk93m9iku3km9ui3kim9uu3mik93i9kmu3m9iku4ever")
'Tell Your World'
```

## References

[^1]: CTF Wiki [Hill 密码](https://ctf-wiki.org/crypto/classical/polyalphabetic/#hill)
