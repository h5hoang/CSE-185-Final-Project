import os

# Testing if implementation can take in two files and output another two based on quality type. 
os.system('"py sickle/sickle.py -f example-files/NA12878_child_1.fq -r example-files/NA12878_child_2.fq -t Sanger -o child1.fq -p child2.fq"')