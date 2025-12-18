# Brainteasers Part 1

## Successive Powers

The following integers: `588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237` are successive large powers of an integer `x`, modulo a three digit prime `p`.

**The mission**

Finding `p`, `x`, the flag will be `crypto{p,x}`.

**The Solution**

We're given a list of successive modular powers of an element `x` : `{588,665,216,113,642,4,836,114,851,492,819,237}`.

Using that list, we particularly have : `113 ⋅ x ≡ 642 (mod p)` and `114 ⋅ x ≡ 851 (mod p)`.

So, subtracting : `x ≡ 851 − 642 = 209 (mod p)`.

So we've found the value for `x`.

To find `p` just take an equation and replace the value for x : `588 ⋅ 209 ≡ 665 (mod p)` means that `588 ⋅ 209 − 665 ≡ 0 (mod p)`, so : `p | 588 ⋅ 209 − 665 = 122227`.

If you factorize the last number you get: `122227 = 7 ⋅ 19 ⋅ 919`.

The only good candidate is `p = 919`.

It could seems that choosing `113 ⋅ x` and `114 ⋅ x` equations is sort of cheating, a general solution is to select two coprime numbers and with the Extended Eucledian Algorithm one can find out the two integers needed to get the linear comnination to write 1 with the numbers the challenge gave you.

Here is the other solution (code) :

```python
from sympy import isprime, mod_inverse

seq = [588,665,216,113,642,4,836,114,851,492,819,237]

for p in range(101, 1000):
	if not isprime(p):
		continue

	x = (seq[1] * mod_inverse(seq[0], p)) % p

	ok = True
	for i in range(len(seq) - 1):
		if (seq[i] * x) % p != seq[i + 1] % p:
			ok = False
			break

	if ok:
		print(f"crypto{{{p}, {x}}}")
		break
```

It was hard.

## 