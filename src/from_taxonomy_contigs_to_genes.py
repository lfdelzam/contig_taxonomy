# /usr/bin/env python3
import argparse
import re
import os
usage= 'python from_taxonomy_contigs_to_genes.py [-i] [-g] [-t]'
description = 'This program extracts the taxonomy annotation from contigs and assigns them to the corresponding representative genes'

parser = argparse.ArgumentParser(description=description, usage=usage)
parser.add_argument ('-i', metavar="contigs taxonomy annotation", dest= 'i', help='path to contigs taxonomy annotation file, e.g., GTDB_Uniprot90.tsv', required = True)
parser.add_argument ('-g', metavar="representative gene or proteins", dest= 'g', help='path to representative gene or protein file, e.g., rep.fasta', required = True)
parser.add_argument ('-t', metavar="output table name", dest= 't', help=' table containing the representative genes and its taxonomy, e.g., genes_taxonomy.tsv', required = True)

args = parser.parse_args()



dir=os.path.dirname(args.t)

def get_taxonomy_annotation(file):
    with open(file, "r") as taxonomy:
        contigs_taxo = {}
        for line in taxonomy:
            line = line.rstrip()
            line = line.split("\t")
            contig = line[0]
            if line[2] == "no rank" :
                taxo="unclassified"
            else:
                taxo=re.sub("._","", line[8])
                taxo=taxo.split(";")
                taxo=";".join([t for t in taxo if t != "cellular organisms"])
            contigs_taxo[contig] = taxo
    return contigs_taxo

def assign_taxonomy_to_genes(contigs_taxo, filein, filetable):
    with open(filein, "r") as fin, open(filetable, "w") as fouttab, open(os.path.join(dir,"non_mmseqs_classifed.txt"), "w") as fe, open(os.path.join(dir,"taxo_unclassifed.txt"), "w") as fu, open(os.path.join(dir,"onlykigdom.txt"), "w") as fk:
        print("#Gene\tassigned_taxonomy", file=fouttab)
        for line in fin:
            line = line.rstrip()
            if line.startswith(">"):
#>co_assembly_k127_1_1 # 2 # 208 # 1 # ID=1_1;partial=11;start_type=Edge;rbs_motif=None;rbs_spacer=None;gc_cont=0.609
                gene = line.split(" ")[0][1:] #co_assembly_k127_1_1
                contig = "_".join(map(str,gene.split("_")[:-1])) #co_assembly_k127_1
                if contig in contigs_taxo:
                    if contigs_taxo[contig] != "unclassified" :
                        if contigs_taxo[contig].find(';') != -1:
                            print(gene+"\t"+contigs_taxo[contig], file=fouttab)
                        else:
                            print(gene+"\t"+contigs_taxo[contig], file=fk)    
                    else:
                        print(gene, contig, file=fu)
                else:
                    print(gene, contig, file=fe)

contigs_taxonomy = get_taxonomy_annotation(args.i)
assign_taxonomy_to_genes(contigs_taxonomy, args.g, args.t)

