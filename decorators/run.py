#!/usr/bin/env python3
from .tobeimported import func


@func
def func1():
    print("super")


@func
def func2():
    print("super2")


if __name__ == "__main__":
    func1()
    func2()