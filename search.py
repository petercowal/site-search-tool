import requests, configparser

def Search(params):

    website = params['website']
    keywords = params['keywords']
    numResults = int(params['numResults'])

    # read in API keys from configuration file
    config = configparser.ConfigParser()
    config.read('config.ini')

    try:
        searchID = config['Keys']['CustomSearchID']
        searchKey = config['Keys']['APIKey']
    except:
        raise Exception("Missing API Keys in Configuration File")

    URL = "https://www.googleapis.com/customsearch/v1"

    items = []
    for i in range(1, min(numResults, 100), 10):
        params = {'key':searchKey,
                  'cx':searchID,
                  'q':'site:' + website + ' ' + keywords,
                  'start':i}

        r = requests.get(URL, params)

        data = r.json()

        if 'items' in data:
            items += data['items']
        else:
            break

    return items
