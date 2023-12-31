import argparse
from Bio import SeqIO

# Get inputs (Not too sure how this works as I just took this off stackoverflow)
parser = argparse.ArgumentParser(description='Store Input Output of the files we need')
parser.add_argument('input', help='fastq file as input')
parser.add_argument('output', help='fasta file as output')
args = parser.parse_args()

# make fastq
for record in SeqIO.parse(args.input, "fastq"):
        SeqIO.write(record, args.output, "fasta")
