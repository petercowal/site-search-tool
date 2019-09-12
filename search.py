import PySimpleGUI as sg
import requests, configparser
import constants

def Search(website, keywords, language, numResults):

    if not website:
        raise Exception("Please enter a valid website to search.")
    if not keywords:
        raise Exception("Please enter a valid search keyword.")
    langcode = constants.LANGCODES[language]
    numResults = min(int(numResults), 100)

    # read in API keys from configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        searchID = config['Keys']['CustomSearchID']
        searchKey = config['Keys']['APIKey']
    except:
        raise Exception("Missing API Keys in Configuration File.")

    URL = "https://www.googleapis.com/customsearch/v1"

    items = []
    for i in range(1, numResults, 10):
        sg.OneLineProgressMeter('Search Progress', i, numResults, 'search_meter')
        google_params = {'key':searchKey,
                          'cx':searchID,
                          'q':'site:' + website + ' ' + keywords,
                          'start':i}

        if langcode != "":
            google_params['lr'] = langcode

        r = requests.get(URL, google_params)

        data = r.json()

        if 'items' in data:
            items += data['items']
        else:
            break
    sg.OneLineProgressMeter('Search Progress', numResults, numResults, 'search_meter')
    return items
