# Modular Arithmetic

## Greatest Common Divisor

The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers `(a,b)`.

For `a=12,b=8` we can calculate the divisors of `a: {1,2,3,4,6,12}` and the divisors of b: `{1,2,4,8}`. Comparing these two, we see that `gcd⁡(a,b)=4`.

Now imagine we take `a=11,b=17`. Both `a` and `b` are prime numbers. As a prime number has only itself and `1` as divisors, `gcd⁡(a,b)=1`.

We say that for any two integers `a,b`, if `gcd⁡(a,b)=1` then `a` and `b` are coprime integers.

If `a` and `b` are prime, they are also coprime. If `a` is prime and `b<a` then `a` and `b` are coprime.

**Think about the case for `a` prime and `b>a`, why are these not necessarily coprime?**

There are many tools to calculate the GCD of two integers, but for this task we recommend looking up [Euclid's Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm).

Example :

```python
def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

a = 66528
b = 52920
print(gcd(a, b))

Output :
1512
```

## Extended GCD

Let `a` and `b` be positive integers.

The extended Euclidean algorithm is an efficient way to find integers `u,v` such that

```python
a⋅u + b⋅v = gcd(a,b)
```

**Later, when we learn to decrypt RSA ciphertexts, we will need this algorithm to calculate the modular inverse of the public exponent.**

**Resources :**
- [Extended Euclidean Algorithms](https://www.geeksforgeeks.org/python/python-program-for-basic-and-extended-euclidean-algorithms-2/)
- [Visualization of EEA](https://www.youtube.com/watch?v=YZfPcvbwwvI)

To illustrate :

```python
a, b = 26513, 32321
x0, x1, y0, y1 = 1, 0, 0, 1

while b:
    q = a // b
    a, b = b, a % b
    x0, x1 = x1, x0 - q * x1
    y0, y1 = y1, y0 - q * y1

print("GCD is", a)
print("x =", x0, ", y =", y0)

Output :
GCD is 1
x = 10245 , y = -8404
```

**Knowing that `p,q` are prime, what would you expect `gcd⁡(p,q)` to be? For more details on the extended Euclidean algorithm, check out [this page](https://web.archive.org/web/20230511143526/http://www-math.ucdenver.edu/~wcherowi/courses/m5410/exeucalg.html).**

## Modular Arithmetic 1

Imagine you lean over and look at a cryptographer's notebook. You see some notes in the margin :

```python
4 + 9 = 1
5 - 7 = 10
2 + 3 = 5
```

At first you might think they've gone mad. Maybe this is why there are so many data leaks nowadays you'd think, but this is nothing more than modular arithmetic modulo 12 (albeit with some sloppy notation).

You may not have been calling it modular arithmetic, but you've been doing these kinds of calculations since you learnt to tell the time (look again at those equations and think about adding hours).

Formally, "calculating time" is described by the theory of congruences. We say that two integers are congruent modulo m if `a ≡ b mod m`.

Another way of saying this, is that when we divide the integer `a` by `m`, the remainder is `b`. This tells you that if `m` divides `a` (this can be written as `m∣a`) then `a ≡ 0 mod m`.

Example :

```python
11 ≡ 5 mod 6
8146798528947 ≡ 4 mod 17
```

## Modular Arithmetic 2

We'll pick up from the last challenge and imagine we've picked a modulus `p`, and we will restrict ourselves to the case when `p` is prime.

The integers modulo `p` define a field, denoted `Fp`​.

**If the modulus is not prime, the set of integers modulo `n` define a ring.**

A finite field `Fp`​ is the set of integers `0,1,...,p−1`, and under both addition and multiplication there are inverse elements `b+`​ and `b∗`​ for every element `a` in the set, such that `a + b+ = 0` and `a ⋅ b∗ = 1`.

**Note that the identity element for addition and multiplication is different! This is because the identity when acted with the operator should do nothing: `a+0=a` and `a⋅1=a`.**

**Fermat's Little Theorem.**

Example :

```python
print(pow(273246787654, 65536, 65537))

Output :
1

This can also be proved using FLT.
```

## Modular Inverting

As we've seen, we can work within a finite field `Fp`​, adding and multiplying elements, and always obtain another element of the field.

For all elements `g` in the field, there exists a unique integer `d` such that `g ⋅ d ≡ 1 mod p`.

This is the multiplicative inverse of `g`.

Resources :
- [video1](https://www.youtube.com/watch?v=Pl4FaV5GZvc)
- [video2](https://www.youtube.com/watch?v=shaQZg8bqUM)
- [forum](https://stackoverflow.com/questions/14093417/find-the-inverse-of-a-number-modulo-a-prime)

Examples :

```python
7 ⋅ 8 = 56 ≡ 1 mod 11

d = 3 ^ (-1)

Using our EEA we get :

-4 -> 9 (it has to be positive) (we just had it our modulo which is 13 here)

3 * 9 = 27 ≡ 1 mod 13
```

## Quadratic Residues

We've looked at multiplication and division in modular arithmetic, but what does it mean to take the square root modulo an integer?

For the following discussion, let's work modulo `p = 29`. We can take the integer `a = 11` and calculate `a^2 = 5 mod 29`.

As `a = 11, a^2 = 5`, we say the square root of `5` is `11`.

This feels good, but now let's think about the square root of `18`. From the above, we know we need to find some integer `a` such that `a^2 = 18`.

Your first idea might be to start with `a = 1 ` and loop to `a = p − 1`. In this discussion `p` isn't too large and we can quickly check all options.

Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all `a ∈ Fp∗`​ you never find an `a` such that `a^2 = 18`.

What we are seeing, is that for the elements of `Fp∗`​, not every element has a square root. In fact, what we find is that for roughly one half of the elements of `Fp∗`​, there is no square root.

**We say that an integer `x` is a Quadratic Residue if there exists an `a` such that `a^2 ≡ x mod p`. If there is no such solution, then the integer is a Quadratic Non-Residue.**

In other words, `x` is a quadratic residue when it is possible to take the square root of `x` modulo an integer `p`.

**If `a^2 = x` then `(−a)^2 = x`. So if `x` is a quadratic residue in some finite field, then there are always two solutions for `a`.**

Example :

In the below list there are two non-quadratic residues and one quadratic residue.

Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.

```python
p = 29
ints = [14, 6, 11]

for i in ints:
    found = False
    for j in range(p):
        if (j ** 2 % p) == i:
            print(f'Here is a square root for {i}: {j}')
            found = True
    if not found:
        print(f"{i} has no square root modulo {p}")

Output :
14 has no square root modulo 29
Here is a square root for 6: 8
Here is a square root for 6: 21
11 has no square root modulo 29
```

## Legendre Symbol

In Quadratic Residues we learnt what it means to take the square root modulo an integer. We also saw that taking a root isn't always possible.

In the previous case when `p = 29`, even the simplest method of calculating the square root was fast enough, but as pp gets larger, this method becomes wildly unreasonable.

Lucky for us, we have a way to check whether an integer is a quadratic residue with a single calculation thanks to Legendre. In the following, we will assume we are working modulo a prime `p`.

Before looking at Legendre's symbol, let's take a brief detour to see an interesting property of quadratic (non-)residues.

```
Quadratic Residue * Quadratic Residue = Quadratic Residue
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue 
```

**Want an easy way to remember this? Replace "Quadratic Residue" with `+1` and "Quadratic Non-residue" with `−1`, all three results are the same!**


So what's the trick? The [Legendre Symbol](https://en.wikipedia.org/wiki/Legendre_symbol) gives an efficient way to determine whether an integer is a quadratic residue modulo an odd prime `p`.

Legendre's Symbol: `(a/p) ≡ a^((p−1)/2) mod p` obeys:

```python
(a/p)=1 if a is a quadratic residue and a ≢ 0 mod p
(a/p)=−1 if a is a quadratic non-residue mod p
(a/p)=0 if a ≡ 0 mod p
```

Which means given any integer `a`, calculating `a^((p−1)/2)` mod p is enough to determine if `a` is a quadratic residue.

Example :

Now for the flag. Given the following 1024 bit prime and 10 integers, find the quadratic residue and then calculate its square root; the square root is your flag. Of the two possible roots, submit the larger one as your answer.

```python
p = 10152...
ints = [250818412...]

e = (p-1) // 2
a = 0
for i in ints:
    if pow(i, e, p) == 1:
        a = i
        break

print(pow(a,(p+1)//4,p)) # Gives us the modular square root
```

**So Legendre's symbol tells us which integer is a quadratic residue, but how do we find the square root?! The prime supplied obeys `p = 3 mod 4`, which allows us easily compute the square root. The answer is online, but you can figure it out yourself if you think about Fermat's little theorem.**

## Modular Square Root

In Legendre Symbol we introduced a fast way to determine whether a number is a square root modulo a prime. We can go further: there are algorithms for efficiently calculating such roots. The best one in practice is called Tonelli-Shanks, which gets its funny name from the fact that it was first described by an Italian in the 19th century and rediscovered independently by Daniel Shanks in the 1970s.

All primes that aren't 2 are of the form `p ≡ 1 mod 4` or `p ≡ 3 mod 4`, since all odd numbers obey these congruences. As the previous challenge hinted, in the `p ≡ 3 mod 4` case, a really simple formula for computing square roots can be [derived](https://crypto.stackexchange.com/questions/20993/significance-of-3mod4-in-squares-and-square-roots-mod-n/20994#20994) directly from Fermat's little theorem. That leaves us still with the `p ≡ 1 mod 4` case, so a more general algorithm is required.

In a congruence of the form `r^2 ≡ a mod p`, Tonelli-Shanks calculates `r`.

**Tonelli-Shanks doesn't work for composite (non-prime) moduli. Finding square roots modulo composites is computationally equivalent to integer factorization - that is, it's a hard problem.**

The main use-case for this algorithm is finding elliptic curve coordinates. Its operation is somewhat complex so we're not going to discuss the details, however, implementations are easy to find and Sage has one built-in.

Example :

Find the square root of `a` modulo the 2048-bit prime `p`. Give the smaller of the two roots as your answer.

```python
a = 847...
p = 305...

def legendre(a,p):
    return pow(a, (p-1) // 2,p)

def tonelli(a,p):
    assert legendre(a,p) ==1, "not a quadratic-residue"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1

    if s == 1 :
        return pow(a, (p + 1) // 4, p)

    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break

    c = pow(z, q, p)
    r = pow(a, (q + 1) // 2, p)
    t = pow(a, q, p)

    m = s

    t2 = 0

    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

flag = tonelli(a, p)

print(f'flag : {flag}')
```

## Chinese Remainder Theorem

The Chinese Remainder Theorem gives a unique solution to a set of linear congruences if their moduli are coprime.

This means, that given a set of arbitrary integers `a^i`, and pairwise coprime integers `n^i`, such that the following linear congruences hold:

**
Note "pairwise coprime integers" means that if we have a set of integers `{n^1,n^2,...,n^i}`, all pairs of integers selected from the set are coprime : `gcd(n^i,n^j) = 1`.**

```python
x ≡ a^1 mod n^1
x ≡ a^2 mod n^2
……
x ≡ a^n mod n^n
```

There is a unique solution `x ≡ a mod N` where `N = n^1⋅n^2⋅...⋅n^n`.

In cryptography, we commonly use the [Chinese Remainder Theorem](https://www.youtube.com/watch?v=e8DtzQkjOMQ) to help us reduce a problem of very large integers into a set of several, easier problems.

To illustrate :

Given the following set of linear congruences:

```python
x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17
```

Find the integer `a` such that `x ≡ a mod 935`.

**Starting with the congruence with the largest modulus, use that for `x ≡ a mod p` we can write `x = a + k ⋅ p` for arbitrary integer `k`.**

```python
a1, m1 = 2, 5
a2, m2 = 3, 11
a3, m3 = 5, 17

M = m1 * m2 * m3 # 5 * 11 * 17 = 935

M1 = M // m1 # 935 / 55 = 187
M2 = M // m2 # 935 / 11 = 85
M3 = M // m3 # 935 / 17 = 55

IM1 = 3 # Searching
IM2 = 7 # Searching
IM3 = 13 # Searching

x = a1 * M1 * IM1 + a2 * M2 * IM2 + a3 * M3 * IM3 # x = 6482
x = x % M # x = 872

print(f'The solution is : {x}') # The solution is : 872
```

##  Adrien's Signs

Given code :

```python
from random import randint

a = 288260533169915
p = 1007621497415251
n = [675...]

FLAG = b'crypto{????????????????????}'


def encrypt_flag(flag):
    ciphertext = []
    plaintext = ''.join([bin(i)[2:].zfill(8) for i in flag])
    for b in plaintext:
        e = randint(1, p)
        n = pow(a, e, p)
        if b == '1':
            ciphertext.append(n)
        else:
            n = -n % p
            ciphertext.append(n)
    return ciphertext


print(encrypt_flag(FLAG))
```

The output of this encryption will have a size of len(input) * 8 (1 byte = 8 bits).
It adds `pow(a, e, p)` if the current bit is a 1 or `-pow(a, e, p) % p` if it's a zero.

The problem is that e is an unknown random value, so we cannot brute force this problem.
We need to think and use what we know.

We only know 3 things :
- a : Our number used in our modulo
- p : Odd prime number used as modulo
- n : Our encrypted flag

Let's try using the **Legendre Symbol**.

We will need **Euler’s criterion** :

```
c^((p − 1) / 2) ≡ 1 [p] -> quadratic residue

c^(p − 1) / 2 ≡ −1 [p] -> quadratic non-residue
```

We now have :

```
a = 288260533169915
p = 1007621497415251

a ≢ 0 [p]

and

(a / p) ≡ a ^ ((p − 1) / 2) [p] ≡ 1 [p]
```

So `a` is a quadratic residue modulo `p`, meaning all its powers will be too.

On the opposite, it's inverse `−(a^e)` is a quadratic non-residue modulo p.

This means that we have to check for every bit whether it's a quadratic number (1) or not (0).

Let's decrypt this :

```python
a = 288260533169915
p = 1007621497415251
n = [675...]

e = (p - 1) // 2
bits = ''.join(('1' if pow(c, e, p) == 1 else '0') for c in n)
flag = long_to_bytes(int(bits, 2)).decode()

print(f'The flag is : {flag}')

Output :

crypto{p4tterns_1n_re5idu3s}
```

End of simulation

## Modular Binomials

Rearrange the following equations to get the primes `p, q`

```
N = p ⋅ q
c1 = (2⋅p + 3⋅q)^e1 mod N
c2 = (5⋅p + 7⋅q)^e2 mod N
```

Resources :
- [Modular Binomial Explanation](https://www.ctfrecipes.com/cryptography/general-knowledge/maths/modular-arithmetic/modular-binomial)

Given `N, e1, e2, c1, c2`, we get :

```python
a1, a2 = 2, 5
b1, b2 = 3, 7

q = math.gcd(pow(a2,(-e2 * e1), N) * pow(c2, e1, N) - pow(a1, (-e1 * e2), N) * pow(c1, e2, N), N)
p = N // q

print(f'flag : crypto{{{p}, {q}}}')
```