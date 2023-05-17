import argparse
from . import utils as utils
from sickle import __version__
import os

def main():
    parser = argparse.ArgumentParser(
        prog = "sickle",
        description = "Command-line script to perform sickle of fastq files"
    )
    
    # Input
    parser.add_argument("-f", "--forward", help="Input paired-ended forward fastq file", \
        metavar="FILE", type=str, required=True)
    parser.add_argument("-r", "--reverse", help="Input paired-ended reverse fastq file", \
        metavar="FILE", type=str, required=True)

    # Output
    parser.add_argument("-o", "--output-1", help="Output forward trimmed fastq file", \
        metavar="FILE", type=str, required=True)
    parser.add_argument("-p", "--output-2", help="Output reverse trimmed fastq file", \
        metavar="FILE", type=str, required=True)
    
    #Other options


    args = parser.parse_args()