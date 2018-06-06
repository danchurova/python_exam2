fromm Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Fasta')
    parser.add_argument('-i', '--input', help='input fasta file', type=str, required=True)
    parser.add_argument('-o', '--output', help='output fasta file', type=str, required=True)

    args = parser.parse_args()
    input_file = args.input
    output_file = args.output


    with open(input_file, 'r') as input_fasta:
        alignments_dict = {}
        for record in SeqIO.parse(input_fasta, 'fasta'):
            read = str(record.seq)
            results = NCBIWWW.qblast('blastn', 'nt', read, format_type='XML', alignments=1, descriptions=1)
            parser = NCBIXML.parse(results)
