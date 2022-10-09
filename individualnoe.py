#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == '__main__':
    # Определим универсальное множество
    u = set("abcdefghiklmnopqrstuvwxyz")

    a = {"c", "g", "h", "k", "y"}
    b = {"a", "b", "k", "n", "u"}
    c = {"i", "j", "o", "y", "z"}
    d = {"a", "b", "f", "g", "y", "z"}

    x = (a.union(b)).intersection(d)
    print(f"x = {x}")

    na = u.difference(a)
    nc = u.difference(c)
    nb = u.difference(b)

    y = (na.intersection(d)).union(nc.difference(nb))
    print(f"y = {y}")