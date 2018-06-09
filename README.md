# python_exam2
2nd exam on python course in Bioinformatics Institute

### exam2.py is used for blast via Biopython and filter contigs according to e-value threshold. 

Generates two files: one with aligned contigs with desirable e-value and another one with contigs that did not aligned with this e-value.

Usage:
``` python3 exam2.py -i [input_fasta] -a [output_fasta_for_aligned_contigs] -na [output_fasta_not_aligned_contigs] -e [e-value threshold] ```
