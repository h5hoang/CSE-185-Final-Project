import sys
from Bio import SeqIO

#testing to see if library is able to print out fq file!
#for record in SeqIO.parse("example-files/NA12878_child_1.fq", "fastq"):
#    print(record.id)

for record in SeqIO.parse("example-files/NA12878_child_1.fq", "fastq"):
    print(record.format("qual"))

