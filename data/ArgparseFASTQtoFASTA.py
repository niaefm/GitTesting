import sys, os
import argparse
from Bio import SeqIO

# Get inputs (Not too sure how this works as I just took this off stackoverflow)
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='name of the file')
parser.add_argument('--verbose','-v', action='store_true', help='Enable Verbose')
parser.add_argument('output','-o', help='output file name')
args = parser.parse_args()

# make fastq
with open(args.filename, "r") as fastq, open(args.output, "w") as fasta:
    for record in SeqIO.parse(fastq, "fastq"):
        SeqIO.write(record, fasta, "fasta")