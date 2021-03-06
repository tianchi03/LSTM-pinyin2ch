#!/usr/bin/env python3

import sys
import regex
import re

subname = sys.argv[1]

print("parse subtitle file: {}".format(subname), file=sys.stderr)

with open(subname, 'r') as f:
    data = re.split('\n\s*\n', f.read().strip())

    for block in data:
        block = block.split('\n')[2:]
        if len(block) == 0:
            continue
        for line in block:
            senlist = regex.split("[\p{P}<>#=]+", line)
            for sen in senlist:
                sen = sen.strip()
                if sen == '':
                    continue
                if re.search('[a-zA-Z]', sen) is None:
                    print(' '.join(list(sen)))

print("done", file=sys.stderr)
