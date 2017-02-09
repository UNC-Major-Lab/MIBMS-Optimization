#!/usr/bin/env python
import sys

RNASeq_file = open(sys.argv[1], 'U')
kinome_file = open(sys.argv[2], 'U')

geneID2symbol = dict()

for line in kinome_file:
    [uniprot, geneID, geneSymbol] = line.strip().split("\t")
    geneID2symbol[geneID] = geneSymbol
    
print RNASeq_file.readline().strip()

for line in RNASeq_file:
    geneID = line.split("\t")[0]
    if geneID2symbol.has_key(geneID):
        print line.strip()