from Bio import SeqIO
from Bio.Blast import NCBIWWW, NCBIXML
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Fasta')
    parser.add_argument('-i', '--input', help='input fasta file', type=str, required=True)
    parser.add_argument('-o', '--output', help='output fasta file', type=str, required=True)
    parser.add_argument('-e', '--evalue', help='required e-value', type =float, required=True)

    args = parser.parse_args()
    input_file = args.input
    output_file = args.output
    e_value = args.evalue


    with open(input_file, 'r') as input_fasta:
        alignments_dict = {}
        for record in SeqIO.parse(input_fasta, 'fasta'):
            read = str(record.seq)
            results = NCBIWWW.qblast('blastn', 'nt', read, alignments=1, descriptions=1)
            blast_record = NCBIXML.read(results)
            filtered_results = []
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect <= e_value:
                        filtered_results.append('sequence:' + str(alignment.title)+'\nlength:' + str(alignment.length) + '\n e value:' + str(hsp.expect))

            with open(output_file, 'w') as output_result:
                for record in filtered_results:
                    output_result.write(record)
