import argparse
import os

from PyPDF2 import PdfFileWriter, PdfFileReader


def create_parser():
    # input_file = input("Podaj nazwę pliku: ")
    # n_pages = str(input("Podaj ile stron: "))
    # output_name = input("Podaj nowa nazwę pliku: ")
    parser = argparse.ArgumentParser(description='PDF splitter')
    parser.add_argument('input_file', help='Input file path', type=str)
    parser.add_argument('n_pages', help='Number of pages in one split', type=int)
    parser.add_argument('output_name', help='Output file name', type=str)
    return parser


def split_pdf(input_file, n_pages, output_name):
    assert os.path.exists(input_file), f'Path {input_file} does not exist!'
    input_pdf = PdfFileReader(open(input_file, "rb"))
    assert input_pdf.numPages >= n_pages, f'Number of pages in one split cannot be grater than number of pages in file!'
    assert n_pages > 0, f'Number of pages cannot be negative or equal to zero'
    i = 0
    file_number = 1
    while True:
        if i >= input_pdf.numPages:
            break
        output = PdfFileWriter()
        for j in range(n_pages):
            if i + j >= input_pdf.numPages:
                break
            print(f'Writing pages {i + j}...')
            output.addPage(input_pdf.getPage(i + j))
        with open(f'{output_name}_{file_number}.pdf', "wb") as fopen:
            output.write(fopen)
        i += n_pages
        file_number += 1


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    split_pdf(args.input_file, args.n_pages, args.output_name)