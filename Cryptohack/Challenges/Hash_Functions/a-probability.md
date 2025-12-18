# Hash Functions

## Jack's Birthday Hash

Today is Jack's birthday, so he has designed his own cryptographic hash as a way to celebrate.

Reading up on the key components of hash functions, he's a little worried about the security of the `JACK11` hash.

Given any input data, `JACK11` has been designed to produce a deterministic bit array of length 11, which is sensitive to small changes using the avalanche effect.

Using `JACK11`, his secret has the hash value: `JACK(secret) = 01011001101`.

Given no other data of the `JACK11` hash algorithm, how many unique secrets would you expect to hash to have (on average) a 50% chance of a collision with Jack's secret?

Solution :

We have : `2^11 = 2048` hash possibilities.

`P_no_collision = ((M - 1) / M) * ((M - 2) / M) * ... * ((M - n) / M)` where `n` is our number of tries.

Because `n << M` we can approximate to : `P_no_collision = (1 - 1 / M​)^n`

For a porbability of 0.5, this gives us : `n ​≈ 1420` (approximately)

## Jack's Birthday Confusion

The last computation has made Jack a little worried about the safety of his hash, and after doing some more research it seems there's a bigger problem.

Given no other data of the `JACK11` hash algorithm, how many unique secrets would you expect to hash to have (on average) a 75% chance of a collision between two distinct secrets?

**Remember, given any input data, `JACK11` has been designed to produce a deterministic bit array of length 11, which is sensitive to small changes using the avalanche effect.**

Solution :


As we have seen before : `Pno collision ​≈ exp(−(n^2) / 2M​)`

We use this formula to isolate `n` and we find that `n ​≈ 76`

