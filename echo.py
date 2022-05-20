#!/usr/bin/env python3
"""Using sys.argv for creating echo program."""

import sys

echo = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 \
       else '*** Sorry, nothing to print! ***'
print(echo)
    