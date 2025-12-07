# Public-Key Cryptography

## Modular Exponentiation

All operations in RSA involve **modular exponentiation**.

Modular exponentiation is an operation that is used extensively in cryptography and is normally written like : `2^10 mod 17`

In Python there's a built-in operator for performing this operation : `pow(base, exponent, modulus)`.

Example : 

```python
print("The result is :", pow(101, 17, 22663))

Output :
The result is : 19906
```

In RSA, modular exponentiation, together with the problem of prime factorisation, helps us to build a "**trapdoor function**". This is a function that is easy to compute in one direction, but hard to do in reverse unless you have the right information. It allows us to encrypt a message, and only the person with the key can perform the inverse operation to decrypt it.

## Public Keys

RSA encryption is modular exponentiation of a message with an exponent `e` and a modulus `N` which is normally a product of two primes: `N=p⋅q`.

Together, the exponent and modulus form an RSA "public key" `(N,e)`. The most common value for `e` is `0x10001` or `65537`.

To illustrate :

```python
number_to_encrypt = 12
p = 17
q = 23
N = p * q
e = 65537

print("Ciphertext :", pow(number_to_encrypt, e, N))
```

## Euler's Totient

https://leimao.github.io/article/RSA-Algorithm/

RSA relies on the difficulty of the factorisation of the modulus `N`. If the prime factors can be deduced, then we can calculate the **Euler totient** of `N` and thus decrypt the ciphertext.

Given `N=p⋅q` and two primes, let's calculate Euler's totient `ϕ(N)` :

```python
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

phi = (p - 1) * (q - 1)

print("Euler's Torent ϕ(N) :", phi)

Output:
Euler's Torent ϕ(N) : 882564595536224140639625987657529300394956519977044270821168
```
