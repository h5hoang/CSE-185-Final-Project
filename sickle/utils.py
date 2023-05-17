import sys
from Bio import SeqIO
#import fastq <- not working for some reason but we might not need this at all

#testing to see if library is able to print out fq file!
#for record in SeqIO.parse("example-files/NA12878_child_1.fq", "fastq"):
#    print(record.id)

#prints phred scores
for record in SeqIO.parse("example-files/NA12878_child_1.fq", "fastq"):
    print(record.format("qual"))

