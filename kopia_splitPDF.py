import os
import shutil
import PySimpleGUI as sg
from PyPDF2 import PdfFileWriter, PdfFileReader
import glob


def split_pdf(input_file, n_pages, output_name):
    assert os.path.exists(input_file), f'Path {input_file} does not exist!'
    input_pdf = PdfFileReader(open(input_file, "rb"))
    assert input_pdf.numPages >= n_pages, f'Number of pages in one split cannot be grater than number of pages in file!'
    assert n_pages > 0, f'Number of pages cannot be negative or equal to zero'

    i = 0
    file_number = 1
    while True:
        for f in glob.glob( recursive=True):
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


layout = [
    [sg.Text('Wybierz plik do skonwertowania'), sg.FileBrowse('Przeglądaj', file_types=(("Pdf Files", '*.pdf'),), key='input_file')],
    [sg.Text('Podaj ilość stron'), sg.InputText(key='n_pages')],
    [sg.Text('Podaj nazwę wyjściową pliku'), sg.InputText(key='output_name')],
    [sg.OK(), sg.Cancel()]
]
window = sg.Window('Pdf Splitter', layout)

while True:
    event, values = window.read()
    if values['input_file'] != '' and values['n_pages'] != '' and values['output_name'] != '' :
        split_pdf(values['input_file'], int(values['n_pages']), values['output_name'])
        # it uses `key='files'` to access `Multiline` widget
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

    window.close()

    layout = [[sg.Text('Czekaj...')],
              [sg.ProgressBar(500, orientation='h', size=(20, 20), key='progressbar')],
              [sg.Cancel()]]

    window = sg.Window('', layout)
    progress_bar = window['progressbar']

    for i in range(500):
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        progress_bar.UpdateBar(i + 1)
    window.close()

    source = '/Users/arturgolata/Desktop/Programowanie/pythonProjects/projectPDF/'
    destination = '/Users/arturgolata/Desktop/Programowanie/pythonProjects/projectPDF/Output/'

    allfiles = os.listdir(source)
    for fname in os.listdir(source):
        if fname.lower().endswith('.pdf'):
            shutil.move(os.path.join(source, fname), destination)
