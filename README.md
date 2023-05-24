# CSE-185-Final-Project
(Work in progress!)

This is our final project for CSE185. It implements a subset of the "sickle" method.
sickle info stuff here!

# Installation Instructions
Installation requires the `biopython` library to be installed. You can install these with `pip`:

For Windows version
```
py -m pip install biopython
```
For Mac version:
```
python3 -m pip install biopython
```
If the install was successful, typing the following code should show a useful message.

For Windows version:
```
py sickle/sickle.py --help 
```
For Mac version:
```
python3 sickle/sickle.py --help
```

# Basic Usage
The basic usage of `sickle` is:
```
sickle [-h] -f FILE -r FILE -o FILE -p FILE [-s FILE] [-t REG] [--version]
```
To run `sickle` on example files of NA12878_child_1.fq (forward) and NA12878_child_2.fq (reverse) (both files in the repository) as test examples:
```
sickle -f example-files/NA12878_child_1.fq -r example-files/NA12878_child_2.fq -t Sanger -o child1.fq -p child2.fq 
```
This should produce two output files child1.fq (forward) and child2.fq (reverse) in the repository, which should looks like:

# Sickle Options
The required input to `sickle` is 
# File format

# Contributors

# Testing
https://biopython.org/docs/1.75/api/Bio.SeqIO.html#submodules 
^ check out the  Bio.SeqIO.QualityIO submodule
