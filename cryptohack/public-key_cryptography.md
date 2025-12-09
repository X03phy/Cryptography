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

### Documentation :

https://leimao.github.io/article/RSA-Algorithm/

### Course

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

## Private Keys

### Documentation :

https://en.wikipedia.org/wiki/Modular_multiplicative_inverse

### Course

The private key `d` is used to decrypt ciphertexts created with the corresponding public key (it's also used to "sign" a message but we'll get to that later).

The private key is the secret piece of information, or "trapdoor", which allows us to quickly invert the encryption function. If RSA is implemented well, if you do not have the private key the fastest way to decrypt the ciphertext is to factorise the modulus which is very hard to do for large integers.

In RSA, the private key is the **modular multiplicative inverse** of the exponent `e` modulo `ϕ(N)`, Euler's totient of `N`.

```python
p = 857504083339712752489993810777
q = 1029224947942998075080348647219 

e = 65537

phi_N = (p - 1) * (q - 1)

d = pow(e, -1, phi_N)

print('The Private Key value is :', d)

Output :
The Private Key value is : 121832886702415731577073962957377780195510499965398469843281
```

## RSA Decryption

To decrypt RSA, we need the encrypted message `C`, the private key `d` and the modulus `N`.

To illustrate :

```python
N = 882564595536224140639625987659416029426239230804614613279163
e = 65537

d = 121832886702415731577073962957377780195510499965398469843281

C = 77578995801157823671636298847186723593814843845525223303932 

M = pow(C, d, N)
print('The Message is :', M)
```

## RSA Signatures

### Documentation

https://crypto.stackexchange.com/questions/12090/using-the-same-rsa-keypair-to-sign-and-encrypt/12138#12138

### Course

How can you ensure that the person receiving your message knows that you wrote it?

You've been asked out on a date, and you want to send a message telling them that you'd love to go, however a jealous lover isn't so happy about this.

When you send your message saying yes, your jealous lover intercepts the message and corrupts it so it now says no!

We can protect against these attacks by cryptographically signing the message.

Imagine you write a message `M`. You encrypt this message with your friend's public key: `c = m ^ e0 mod N0`​.

To sign this message, you calculate the hash of the message: `H(M)` and "encrypt" this with your private key: `S = H(M) ^ d1 mod N1`​.

In real cryptosystems, it's **best practice to use separate keys** for encrypting and signing messages.

Your friend can decrypt the message using their private key : `m = c ^ d0 mod N`​. Using your public key they calculate `s = S ^ e1 mod N1`​.

Now by computing `H(m)` and comparing it to `s`: `assert H(m) == s`, they can ensure that the message you sent them, is the message that they received! As long as your private key is safe, no one else could have signed this message!

Example :

```python
from hashlib import sha256

N = 15216583654836731...
d = 11175901210643014...
M = "crypto{Immut4ble_m3ssag1ng}"

hash = sha256(M.encode('utf-8')).hexdigest()
hash_int = int(hash, 16)

S = pow(hash_int, d, N)

print('Our signature is :', S)

Output:
13480738404590090...
```
