import sys, os
from Bio import SeqIO

# Get inputs (Not too sure how this works as I just took this off stackoverflow)
fq_path = sys.argv[1]
fa_path = sys.argv[2]

# make fastq
with open(fq_path, "r") as fastq, open(fa_path, "w") as fasta:
    for record in SeqIO.parse(fastq, "fastq"):
        SeqIO.write(record, fasta, "fasta")