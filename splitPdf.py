import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
import PySimpleGUI as sg
from sys import exit


sg.theme('GreenTan')

if len(sys.argv) == 1:
    fileSourceName = sg.popup_get_file(
        'wybierz plik PDF', 'PDF Splitter', file_types=(("PDF Files", "*.pdf"),))
    if fileSourceName is None:
        sg.popup_cancel('Nie wybrałeś pliku. Koniec programu')
        exit(0)
else:
    fileSourceName = sys.argv[1]

if len(sys.argv) ==1:
    fileOutName = sg.popup_get_folder('Miejsce zapisu pliku',
                                title='Gdzie zapisać',
                                default_path="", ),
    if fileOutName is None:
        sg.popup_cancel('Zakończyć działanie programu?')
        exit(0)
else:
    fileOutName = sys.argv[1]

title = "PyMuPDF display"

layout = [
    [
        sg.Button('Rozdziel'),
    ],
]

window = sg.Window(title, layout,
                   return_keyboard_events=True, use_default_focus=False)

while True:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED:
        break
    elif event == "Rozdziel":
        pdf_file_path = fileSourceName
        file_base_name = pdf_file_path.replace('.pdf', '')
        output_folder_path = os.path.join(os.getcwd(), 'fileOutName')
        pdf = PdfFileReader(pdf_file_path)

        for page_num in range(pdf.numPages):
            pdfWriter = PdfFileWriter()
            pdfWriter.addPage(pdf.getPage(page_num))

            with open(os.path.join(output_folder_path, '{0}_{1}.pdf'.format(file_base_name, page_num+1)),'wb') as f:
                pdfWriter.write(f)
                f.close()
                window.close()

        layout = [[sg.Text('Progres...')],
                  [sg.ProgressBar(500, orientation='h', size=(20, 20), key='progressbar')],
                  [sg.Cancel()]]

        window = sg.Window('Custom Progress Meter', layout)
        progress_bar = window['progressbar']

        for i in range(500):
            event, values = window.read(timeout=10)
            if event == 'Cancel' or event == sg.WIN_CLOSED:
                break
            progress_bar.UpdateBar(i + 1)

        window.close()

