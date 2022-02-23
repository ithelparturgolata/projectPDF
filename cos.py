import PySimpleGUI as sg
import os

# help(sg.FolderBrowse)
# help(sg.FileBrowse)

layout = [
    [sg.Input(), sg.FileBrowse('FileBrowse')],
    [sg.Input(), sg.FolderBrowse('FolderBrowse')],
    [sg.Submit(), sg.Cancel()],
]

window = sg.Window('Test', layout)

while True:
    event, values = window.read()
    # print('event:', event)
    # print('values:', values)
    print('FolderBrowse:', values['FolderBrowse'])
    print('FileBrowse:', values['FileBrowse'])

    if event is None or event == 'Cancel':
        break

    if event == 'Submit':
        # if folder was not selected then use current folder `.`
        foldername = values['FolderBrowse'] or '.'

        filenames = os.listdir(foldername)

        print('folder:', foldername)
        print('files:', filenames)
        print("\n".join(filenames))

window.close()