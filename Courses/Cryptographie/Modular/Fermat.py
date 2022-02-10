'''
Looking at Fermat's theorem
if p is prime, for every integer a:
        pow(a, p) ≡ a mod p
and, if p is prime and a is an integer coprime with p:
        pow(a, p-1) ≡ 1 mod p
So lets check
        pow(273246787654, 65536) mod 65537
Notice that 65536 is exactly 65537-1,
If 273246787654 and 65537 are coprime,
        then the result is one
'''

from math import gcd


if ( gcd(273246787654,65537) == 1 ):
    print(1)