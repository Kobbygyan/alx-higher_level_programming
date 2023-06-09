#!/usr/bin/python3

import builtins

builtins.__import__("os").write(1, "#pythoniscool\n".encode("UTF-8"))

