# CSE-185-Final-Project
This is our final project for CSE185. It implements a version of the Sickle implentation done by Nikhil Joshi, UC Davis Bioinformatics Core (https://github.com/najoshi/sickle/tree/master), but in python. Our version only allows for paired-end trimming as it inputs two fastq files and outputs two trimmed fastq files where these files are trimmed based on the quality of the reads inputted. 

# Installation Instructions
1. Clone the Repository into your IDE (we used VSCode)
```
git clone https://github.com/h5hoang/CSE-185-Final-Project
```

2. Setup Installation

For Windows version:
```
py setup.py install    
```
For Mac version:
```
python3 pip install biopython
```

3. Usage of our sickle implementation requires the `biopython` library to be installed. You can install these with `pip`:

For Windows version:
```
py pip install biopython
```
For Mac version:
```
python3 pip install biopython
```

4. If the install was successful, typing the following code should show a useful message.

For Windows version:
```
py sickle/sickle.py --help 
```
For Mac version:
```
python3 sickle/sickle.py --help
```

# Sickle Options
The required inputs to `sickle` are: 
- -f [FORWARD FILE]: Foward fastq file
- -r [REVERSE FILE]: Reverse fastq file
- -t [QUALITY TYPE]: Quality type, i.e. Sanger, Illumina and Solexa
- -o [TRIMMED PE FOWARD FILE]: Generated output PE forward fastq file
- -p [TRIMMED PE REVERSE FILE]: Generated output PE reverse fastq file

# Basic Usage
The basic usage of `sickle` is:
```
py sickle/sickle.py -f [FORWARD FILE] -r [REVERSE FILE] -t [QUALITY TYPE] -o [TRIMMED PE FOWARD FILE] -p [TRIMMED PE REVERSE FILE] 
```
To run `sickle` on example files of NA12878_child_1.fq (forward) and NA12878_child_2.fq (reverse) (both files in the repository) as test examples in the terminal:
```
py sickle/sickle.py -f example-files/NA12878_child_1.fq -r example-files/NA12878_child_2.fq -t Sanger -o child1.fq -p child2.fq
```
This should produce two output files child1.fq (forward) and child2.fq (reverse) in the repository, which should looks the same like the files in example-outputs.

# File format
The output file format should be fastq file, details can be seen:

https://maq.sourceforge.net/fastq.shtml

# Contributors
Kathy Gu, Pinyi Wang, Hanson Hoang
We drew inspiration from Nikhil Joshi, UC Davis Bioinformatics Core: https://github.com/najoshi/sickle/tree/master

# Testing
testing commands are in sickle/test-utils.py
simply run test-utils.py to get the trimmed outputs for the files in the folder, example-files.  

# References
Biopython SeqIO submodule: https://biopython.org/docs/1.75/api/Bio.SeqIO.html#submodules 
Official Sickle Implementation: https://github.com/najoshi/sickle/tree/master
