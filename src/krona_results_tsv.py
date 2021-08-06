#!/usr/bin/env python3

import os
import argparse
import sys
import re

usage = 'krona_results_tsv.py -i -o'
description = 'This program creates input file for krona'

parser = argparse.ArgumentParser(description=description, usage=usage)
parser.add_argument('-i', dest='i', help='path to .tsv file', required=True)
parser.add_argument('-o', dest='o', help='output file name', default="TEST_taxonomy_krona.txt")
args = parser.parse_args()

with open(args.i, "r") as f1, open(args.o, "w") as fout:
#        counter = 0
        for line in f1:
            line=line.rstrip()
            #P1994_103_k141_7697     414004  strain  Cenarchaeum symbiosum A 4       1       1       1.000   -_cellular organisms;d_Archaea;-_TACK group;p_Thaumarchaeota;o_Cenarchaeales;f_Cenarchaeaceae;g_Cenarchaeum;s_Cenarchaeum symbiosum;-_Cenarchaeum symbiosum A

            LS=line.split("\t")
            if LS[2] == "no rank" :
                taxo="unclassified"
            else:
                taxo=re.sub("._","", LS[8])

                taxo=taxo.split(";")
                taxo="\t".join([t for t in taxo if t != "cellular organisms"])
#            counter += 1

            print("{}\t{}".format(1, taxo), file=fout)

#            sys.stdout.write("  queries [{0:9,.0f}]\r".format(counter))
