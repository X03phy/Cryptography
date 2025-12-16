# Primes Part 1

## Inferius Prime

Here is my super-strong RSA implementation, because it's 1600 bits strong it should be unbreakable... at least I think so!

```python
from Crypto.Util.number import *

n = 984994081290620368062168960884976209711107645166770780785733
e = 65537
ct = 948553474947320504624302879933619818331484350431616834086273

p = 848445505077945374527983649411
q = 1160939713152385063689030212503

phi_N = (p - 1) * (q - 1)

d = inverse(e, phi_N)

m = pow(ct, d, n)

print(long_to_bytes(m).decode())

Output:
crypto{N33d_b1g_pR1m35}
```

We used this site : https://www.dcode.fr/prime-factors-decomposition to decompose our n with primes.

That was easy.

## Square Eyes

Resources :
- [Euler's totient](https://cp-algorithms.com/algebra/phi-function.html)

**We know that n is the square of p.**

```python
from Crypto.Util.number import *
import math

n = ...
e = ...
ct = ...

p = int(math.isqrt(n))
phi_N = n - p
d = inverse(e, phi_N)

m = pow(ct, d, n)
print(long_to_bytes(m).decode())

Output :
crypto{squar3_r00t_i5_f4st3r_th4n_f4ct0r1ng!}
```

Eazy peezy