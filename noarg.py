#!/usr/bin/env python2

import os
import sys

if len(sys.argv) != 2:
    exit(1)

prog_name = sys.argv[1]
os.execve(prog_name, [], {})

exit(1)
