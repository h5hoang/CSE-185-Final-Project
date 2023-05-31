import sys
from Bio import SeqIO
#import fastq <- not working for some reason but we might not need this at all

#testing to see if library is able to print out fq file!
#for record in SeqIO.parse("example-files/NA12878_child_1.fq", "fastq"):
#    print(record.id)

def trimmer (forward_file, reverse_file, output_forward_file, output_reverse_file, output_single_file, qual_type):
    # reads files
    forward_reads = list(SeqIO.parse(forward_file, "fastq"))
    reverse_reads = list(SeqIO.parse(reverse_file, "fastq"))

    # creating output 
    trimmed_forward_reads = []
    trimmed_reverse_reads = []
    trimmed_single_reads = []

    # iterate over paired-end reads
    for forward_read, reverse_read in zip(forward_reads, reverse_reads):
        # trim paired-end reads
        trimmed_forward_seq, trimmed_forward_qual = trim_helper(forward_read, qual_type)
        trimmed_reverse_seq, trimmed_reverse_qual = trim_helper(reverse_read, qual_type)

        # check if forward and reverse reads pass the minimum length threshold
        if len(trimmed_forward_seq) >= 20 and len(trimmed_reverse_seq) >= 20:
            # create trimmed SeqRecord objects
            trimmed_forward_record = forward_read[0:len(trimmed_forward_seq)]
            trimmed_forward_record.letter_annotations = {}
            trimmed_forward_record.letter_annotations["phred_quality"] = trimmed_forward_qual

            trimmed_reverse_record = reverse_read[0:len(trimmed_reverse_seq)]
            trimmed_reverse_record.letter_annotations = {}
            trimmed_reverse_record.letter_annotations["phred_quality"] = trimmed_reverse_qual

            # add reads onto outputs
            trimmed_forward_reads.append(trimmed_forward_record)
            trimmed_reverse_reads.append(trimmed_reverse_record)
        else:
            # appending trimmed reads to singles
            if output_single_file:
                trimmed_single_record = forward_read if len(trimmed_forward_seq) >= 20 else reverse_read
                trimmed_single_reads.append(trimmed_single_record)

    # SAVEE
    SeqIO.write(trimmed_forward_reads, output_forward_file, "fastq")
    SeqIO.write(trimmed_reverse_reads, output_reverse_file, "fastq")
    SeqIO.write(trimmed_single_reads, output_single_file, "fastq") if output_single_file else None

    # just to make sure process is done
    print("Sickle Trimming process is complete.")

def trim_helper(read, qual_type):
    trimmed_seq = ""
    trimmed_qual = []
    
    # Define quality offset based on the qual_type
    if qual_type.lower() == "sanger":
        qual_offset = 33
    elif qual_type.lower() == "illumina":
        qual_offset = 64
    elif qual_type.lower() == "solexa":
        qual_offset = 64 
    
    # caluculate window size for trimming
    window_size = int(0.1*len(read.seq))
    if window_size < 1:
        window_size = len(read.seq)

    # perform 5_end trimming
    start_index = 0
    end_index = window_size
    rise_index = 0
    # loop over the read to cut at position qual rise above threshold
    while end_index <= len(read.letter_annotations["phred_quality"]):
        window_qual = read.letter_annotations["phred_quality"][start_index:end_index]
        avg_qual = sum(window_qual) / window_size
        # calculate the point of rise
        if avg_qual >= 20:
            rise_index = window_qual.index(min(window_qual))
        # cut what after the point of rise
        if rise_index > 0:
            trimmed_seq = read.seq[rise_index:]
            trimmed_qual = read.letter_annotations["phred_quality"][rise_index:]
            break
        # slide the window
        start_index += 1
        end_index += 1
    
    # perform 3_end trimming
    for i in range(len(trimmed_seq) - 1, -1, -1):
        qual = trimmed_qual[i]

        # Check if quality drops below the threshold
        if qual < 20:
            # Cut the read at the drop position
            trimmed_seq = trimmed_seq[:i]
            trimmed_qual = trimmed_qual[:i]
            break

    return trimmed_seq, trimmed_qual

#for record in SeqIO.parse("example-files/NA12878_child_1.fq", "fastq"):
#    print(record.format("qual"))

