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

