# Introduction To Cryptohack

Of all modern programming languages, Python 3 stands out as ideal for quickly writing cryptographic scripts and attacks.

## ASCII

Let's start with examples :

```python
ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag :")
print("".join(chr(o ^ 0x32) for o in ords))
```

**ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.**

In Python, the `chr()` function can be used to convert an ASCII ordinal number to a character (the `ord()` function does the opposite).

## Hex

Example :

```python
hex = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

print("Here is your flag :")
print(bytes.fromhex(hex).decode())
```

In Python, the `bytes.fromhex()` function can be used to convert hex to bytes. The `.hex()` instance method can be called on byte strings to get the hex representation.

The `.decode()` instance method in Python is used to convert encoded text back into its original string format. It works as the opposite of `.encode()` instance method, which converts a string into a specific encoding format.

## Base64

Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.

Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

Example :

```python
import base64

hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

raw_bytes = bytes.fromhex(hex_string)

base64_encoded = base64.b64encode(raw_bytes)

base64_string = base64_encoded.decode("ascii")

print("Here is your flag :")
print(base64_string)
```

In Python, after importing the base64 module with `import base64`, you can use the `base64.b64encode()` function. Remember to decode the hex first as the challenge description states.Bytes and Big Integers

## Bytes and Big Integers

Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?

The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.

To illustrate :

```python
message : HELLO
ascii bytes : [72, 69, 76, 76, 79]
hex bytes : [0x48, 0x45, 0x4c, 0x4c, 0x4f]
base-16 : 0x48454c4c4f
base-10 : 310400273487 
```

Python's PyCryptodome library implements this with the methods `bytes_to_long()` and `long_to_bytes()`. You will first have to install PyCryptodome and import it with `from Crypto.Util.number import *`.

## XOR

From the XOR course : operators/xor.md

### XOR Starter

```python
from pwn import xor

string = b"label"
nb = 13

print("Here is your flag :")
print(xor(string, nb).decode())

# It is the same as :

string = 'label'
nb = 13

print("Here is your flag :")
print(''.join(chr(ord(s) ^ nb) for s in string))
```

The Python `pwntools` library has a convenient `xor()` function that can XOR together data of different types and lengths. But first, you may want to implement your own function to solve this.

### XOR Properties

```python
from pwn import xor

KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
KEY2_XOR_KEY3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

flag = xor(FLAG_XOR_KEY1_XOR_KEY3_XOR_KEY2, KEY2_XOR_KEY3, KEY1)

print("Here is your flag :")
print(flag.decode())
```

## You either know, XOR you don't

We know that the flag starts with 'crypto{' so we use it to get the beginning of the key.

```python
from pwn import xor

ciphertext_bytes = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

key = xor(ciphertext_bytes[:7], b'crypto{').decode()

print(f"The beginning of the key is : {key}")
```