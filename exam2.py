from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Fasta')
    parser.add_argument('-i', '--input', help='input fasta file', type=str, required=True)
    parser.add_argument('-a', '--aligned_output', help='output fasta file with contigs aligned with e-value threshold', type=str, required=True)
    parser.add_argument('-na', '--not_aligned_output', help='output fasta file with contigs not aligned with e-value threshold', type=str, required=True)
    parser.add_argument('-e', '--evalue', help='required e-value', type =float, required=True)

    args = parser.parse_args()
    input_file = args.input
    aligned = args.aligned_output
    not_aligned = args.not_aligned_output
    e_value = args.evalue

    def filter(blast_record, record):
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < e_value:
                    with open(aligned, 'w') as aligned_output:
                        SeqIO.write(record, "aligned.fasta","fasta")
                    return
        with open(not_aligned, 'w') as not_aligned_output:
            SeqIO.write(record, "not_aligned.fasta", "fasta")


    with open(input_file, 'r') as input_fasta:
        alignments_dict = {}
        for record in SeqIO.parse(input_fasta, 'fasta'):
            read = str(record.seq)
            results = NCBIWWW.qblast('blastn', 'nt', read, alignments=1, descriptions=1)
            blast_record = NCBIXML.read(results)
            filter(blast_record, record)
