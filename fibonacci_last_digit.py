# Uses python3
import sys

def pisano_method(n,m):
    Lemma : (a + b ) % m = [(a % m) + (b % m)] % m
    F(i + 2) = F(i) + F(i + 1)
    F(i+2)%m = [F(i) + F(i+1)]%m
    for i = 0:


