from newspaper import Article
import os, time, random
import PySimpleGUI as sg

def DownloadArticles(foldername, urls):

    if not os.path.exists(foldername):
        os.mkdir(foldername)

    numUrls = len(urls)

    for i in range(0, numUrls):
        sg.OneLineProgressMeter('Download Progress', i, numUrls, 'download_meter')

        if i > 0:
            time.sleep(random.uniform(3.0,7.0))

        article = Article(urls[i])
        article.build()

        articleFilePath = os.path.join(foldername, 'article' + str(i + 1) + '.txt')
        f = open(articleFilePath, "w")
        f.write(article.text)
        f.close()

    sg.OneLineProgressMeter('Download Progress', numUrls, numUrls, 'download_meter')
