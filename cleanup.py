import re

def cleanUpString(str):
    unicodeEquivalents = {
        '“' : '\"',
        '”' : '\"',
        '’' : '\''
    }
    for key in unicodeEquivalents:
        str = str.replace(key,unicodeEquivalents[key])
    return str

def snakeCase(str):
    return re.sub("__+", "_", (''.join(a if a.isalnum() else "_" for a in str)).strip('_'))
