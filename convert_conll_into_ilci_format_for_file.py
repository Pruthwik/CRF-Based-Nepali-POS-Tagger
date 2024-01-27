"""Convert CONLL file into ILCI format."""
from argparse import ArgumentParser
import os


def read_lines_from_file(file_path):
    '''
    Read lines from a file.
    
    :param file_path: Path of the input file

    :return lines: Returns lines read from the file
    '''
    with open(file_path, 'r', encoding='utf-8') as file_read:
        return file_read.readlines()


def find_sentences_from_conll_text(lines):
    '''
    Find sentences in conll text.

    :param lines: Lines in conll format
    
    :return sentences: Sentences in conll format
    '''
    temp_tokens, sentences = [], []
    for line in lines:
        line = line.strip()
        if line:
            temp_tokens.append(line)
        else:
            if temp_tokens:
                sentences.append(temp_tokens)
            temp_tokens = []
    if temp_tokens:
        sentences.append(temp_tokens)
        temp_tokens = []
    return sentences


def convert_conll_into_ilci_format(conll_sentences, prefix='nep'):
    '''
    Convert conll sentence into ILCI format.

    :param conll_sentences: Sentences in CONLL format
    
    :return ilci_sentences: Sentences in ILCI format
    '''
    ilci_sentences = []
    for index, conll_sentence in enumerate(conll_sentences):
        ilci_sentence = []
        ilci_sentence = [line.split('\t')[0] + '\\' + line.split('\t')[1] for line in conll_sentence]
        ilci_sentence_text = ' '.join(ilci_sentence)
        sentence_id = prefix + str(index + 1)
        ilci_sentences.append('\t'.join([sentence_id, ilci_sentence_text]))
    return ilci_sentences


def write_lines_to_file(lines, file_path):
    '''
    Write lines to file.

    :param lines: Lines to be written
    :param file_path: File path of the output file
    :return: None
    '''
    header = 'ID\tValue'
    lines = [header] + lines
    with open(file_path, 'w', encoding='utf-8') as file_write:
        file_write.write('\n'.join(lines) + '\n')


def main():
    '''
    Pass arguments and call functions here.

    :param: None
    :return: None
    '''
    parser = ArgumentParser()
    parser.add_argument('--input', dest='inp', help="Add the input path")
    parser.add_argument('--output', dest='out', help="Add the output path")
    parser.add_argument('--prefix', dest='pre', help="Add the prefix which needs to be added before every sentence", default='nep')
    args = parser.parse_args()
    if not os.path.isdir(args.inp):
        lines = read_lines_from_file(args.inp)
        conll_sentences = find_sentences_from_conll_text(lines)
        ilci_sentences = convert_conll_into_ilci_format(conll_sentences, args.pre)
        write_lines_to_file(ilci_sentences, args.out)
    else:
        if not os.path.isdir(args.out):
            os.makedirs(args.out)
        for root, dirs, files in os.walk(args.inp):
            for fl in files:
                input_path = os.path.join(root, fl)
                lines = read_lines_from_file(input_path)
                conll_sentences = find_sentences_from_conll_text(lines)
                ilci_sentences = convert_conll_into_ilci_format(conll_sentences, args.pre)
                output_path = os.path.join(args.out, fl)
                write_lines_to_file(ilci_sentences, output_path)


if __name__ == '__main__':
    main()
