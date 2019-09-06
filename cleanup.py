def cleanUpString(str):
    unicodeEquivalents = {
        '“' : '\"',
        '”' : '\"',
        '’' : '\''
    }
    for key in unicodeEquivalents:
        str = str.replace(key,unicodeEquivalents[key])
    return str
