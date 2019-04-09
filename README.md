Mass decryptor for Eazfuscator.NET Symbol Names Encryption
==========================================================

Performs mass decryption for [encrypted symbols][1] if you know the password.

Usage
-----

	$ python deobf.py obfuscated.cs

Dependencies
------------

 - Python 2.x (tested on 2.7.15)
 - Crypto (Debian/Ubuntu package: `python-crypto`) 
 - PBKDF2 (Debian/Ubuntu package: `python-pbkdf2`)

License
-------

The whole project is available under MIT license, see `LICENSE.txt`.

[1]: https://help.gapotchenko.com/eazfuscator.net/53/advanced-features/symbol-names-encryption
