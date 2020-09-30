<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>

# Golomb-coding
The Golomb coding is a form of parameterized coding in which integers to be coded are stored as values relative to a constant b.
A positive integer x is represented in two parts:
  1. The first part is a unary representation of q+1, where q is the quotient floor(x/b)
  2. The second part is a special binary representation of the remainder r = x-qb. Note that there are b possible remainders. For example,   if b = 3, the possible remainders will be 0, 1 & 2.
