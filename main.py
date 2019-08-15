import PySimpleGUI as sg
import os
import search, output
# initialize GUI
window_rows = [
    [sg.Text('Website to Search')],
    [sg.InputText('www.example.com', key='website')],
    [sg.Text('Search Keywords')],
    [sg.InputText('', key='keywords')],
    [sg.Text('Number of Results'), sg.InputCombo([10,20,30,50,100],key='numResults')],
    [sg.Text('Output Directory'),sg.InputText('',key='outdir')],
    [sg.FolderBrowse("Select Output Directory", target='outdir'), sg.Button("Run Search",key='search')]
]

window = sg.Window('Site Search Helper Tool', window_rows)

while True:
    event, values = window.Read()
    if event == 'search':
        try:
            items = search.Search(values)
            siteNameAlphaNum = ''.join(a for a in values['website'] if a.isalnum())
            filename = os.path.join(values['outdir'], siteNameAlphaNum + '.xlsx')
            output.WriteToXLS(filename, items)
            sg.Popup('Search successful!', 'Results saved to ' + filename)
        except Exception as e:
            sg.Popup(e)
    elif event is None or event == 'Exit':
        break
    print(event, values)

window.Close()
