from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import os, time, random
import PySimpleGUI as sg
from cleanup import cleanUpString, snakeCase

def DownloadArticles(foldername, articles):

    if not os.path.exists(foldername):
        os.mkdir(foldername)

    numUrls = len(articles)

    for i in range(0, numUrls):
        article = articles[i]
        sg.OneLineProgressMeter('Download Progress', i, numUrls, 'download_meter')

        if i > 0:
            time.sleep(random.uniform(3.0,7.0))

        articleFilePath = os.path.join(foldername, 'article' + str(i + 1) + '_' + snakeCase(article.title) + '.txt')
        f = open(articleFilePath, "w")

        f.write(cleanUpString(article.title) + '\n')
        f.write(article.url + '\n\n')

        try:
            req = Request(article.url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(req).read()

            soup = BeautifulSoup(response, "html.parser")
            pTags = soup.findAll('p')
            for ptag in pTags:
                par = str(ptag.string)
                if par != "None":
                    f.write(cleanUpString(par) + "\n\n")
        except Exception as e:
            f.write("\nSCRAPER ERROR\n" + str(e))
        f.close()

    sg.OneLineProgressMeter('Download Progress', numUrls, numUrls, 'download_meter')
