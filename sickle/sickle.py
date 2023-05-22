import argparse
from utils import trimmer
#from . import utils as utils
from version import __version__
import os
import sys

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
    parser.add_argument("-s", "--output-single", help = "Output trimmed singles fastq file", \
        metavar="FILE", type=str, required = False)
    parser.add_argument("-t", "--qual-type", help = "Type of quality values (solexa (CASAVA < 1.3), illumina (CASAVA 1.3 to 1.7), sanger (which is CASAVA >= 1.8)) (required)", \
        metavar="REG", type = str, required = False)
    parser.add_argument("--version", help="Print the version and quit", \
		action="version", version = '{version}'.format(version=__version__))

    args = parser.parse_args()

    trimmer(args.forward, args.reverse, args.output_1, args.output_2, args.output_single, args.qual_type)

if __name__ == "__main__":
    main()
