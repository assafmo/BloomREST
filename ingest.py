#!/usr/bin/env python
from pybloomfilter import BloomFilter
import os.path
import sys

# cat <values_file> | ./ingest.py <bloom_file> <max_items> <error_rate>

bloomFilePath = sys.argv[1]
if os.path.isfile(bloomFilePath):
    bf = BloomFilter.open(bloomFilePath)
else:
    maxItems = int(sys.argv[2])
    errorRate = float(sys.argv[3])
    bf = BloomFilter(maxItems, errorRate, bloomFilePath)

valuesBuffer = []
for line in iter(sys.stdin.readline, ''):
    valuesBuffer.append(unicode(line.rstrip('\n')))
    if len(valuesBuffer) > 100000:
        bf.update(valuesBuffer)
        valuesBuffer = []

bf.update(valuesBuffer)
bf.sync
