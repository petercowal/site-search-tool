import PySimpleGUI as sg
import os
import search, output, constants, scrape
from article import Article
from cleanup import snakeCase
import time
# initialize GUI
window_rows = [
    [sg.Text('Website to Search')],
    [sg.InputText('www.example.com', key='website')],
    [sg.Text('Search Keywords')],
    [sg.InputText('', key='keywords')],
    [sg.Text('Number of Results'), sg.InputCombo([10,20,30,50,100], key='numResults')],
    [sg.Text('Language'), sg.InputCombo(sorted(list(constants.LANGCODES.keys())), key='language')],

    [sg.Checkbox('Restrict Results to the Past', default=False, key='restrictDates'),
        sg.InputText('1',size=(3,1),key='dateRestrictNum'),
        sg.InputCombo(['Days','Weeks','Months','Years'],key='dateRestrictType')],

    [sg.Checkbox('Automatically Download Articles', default=True, key='downloadArticles')],

    [sg.Text('Output Directory'),sg.InputText('',key='outdir')],
    [sg.FolderBrowse("Select Output Directory", target='outdir'), sg.Button("Run Search", key='search')]
]

window = sg.Window('Site Search Helper Tool', window_rows)

while True:
    event, values = window.Read()
    if event == 'search':
        try:
            if values['restrictDates']:
                dateRestriction = search.DateRestriction(int(values['dateRestrictNum']), values['dateRestrictType'])
            else:
                dateRestriction = None

            items = search.Search(values['website'],
                                values['keywords'],
                                values['language'],
                                values['numResults'],
                                dateRestriction)

            siteNameAlphaNum = values['keywords'] + '_' + snakeCase(values['website'])
            timestring = time.strftime('%Y_%m_%d__%H_%M')
            filename = os.path.join(values['outdir'], siteNameAlphaNum + '_' + timestring + '.xlsx')
            output.WriteToXLS(filename, items)
            sg.Popup('Search successful!', 'Results saved to ' + filename)

            if values['downloadArticles']:
                articleFolder = os.path.join(values['outdir'], siteNameAlphaNum + '_' + timestring)
                articles = []
                for item in items:
                    articles.append(Article(item['title'], item['link']))
                scrape.DownloadArticles(articleFolder, articles)

        except Exception as e:
            sg.PopupError(e)
    elif event is None or event == 'Exit':
        break

window.Close()
