# -*- coding: utf-8 -*-

from __future__ import print_function
from string import ascii_lowercase
import random

# P[1...m]
# T[1...n]

def fail_function(p):
    m = len(p)
    fail = [0 for x in range(m)]
    fail[0] = 0
    k = 0
    for q in range(1,m):
        while k > 0 and p[k] != p[q]:
            k = fail[k-1]
        if p [k] == p[q]:
            k = k + 1
        fail[q] = k
    return fail

def kmp_match(t, p):
    n = len(t)
    m = len(p)

    fail = fail_function(p)
    
    q = 0
    for i in range(n):
        while q > 0 and p[q] != t[i]:
            q = fail[q-1]
        if p[q] == t[i]:
            q = q + 1
        if q == m:
            print("pattern starts with shift ", i - m + 1)
            q = fail[q-1]


def gen_alphabet(size):
    return ascii_lowercase[0:size]


def gen_string(size, alphabet):
    body = ""
    for i in range(0, size):
        body+=alphabet[random.randint(0, len(alphabet)-1)]
    return body


def print_table(t, p, fail):
    def print_row(label, array):
        print("| "+label+" ", end="")
        for i in range(len(array)):
            print("| " + str(array[i]) + " ", end="")
        print("|")
    def print_seperator():
        for i in range(len(p)+1):
            print("----", end="")
        print("-")
    print_seperator()
    print_row("P", p)
    print_seperator()
    print_row("S", range(0, len(p)))
    print_seperator()
    print_row("π", fail)
    print_seperator()


def gen_problem(alphabet_length, pattern_length, text_length):
    alphabet = gen_alphabet(alphabet_length)
    p = gen_string(pattern_length, alphabet)
    print("P: " + p)
    t = gen_string(text_length, alphabet)
    print("T: " + t)
    kmp_match(t, p)
    print_table(t, p, fail_function(p))

gen_problem(3, 10, 30)
