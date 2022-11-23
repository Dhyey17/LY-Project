from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np


def wc(string):
    maskarr = np.array(Image.open("Word Cloud Mask.png"))
    cloud = WordCloud(background_color="white", max_words=18, mask=maskarr, stopwords=set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("Word Cloud O.png")


data = open("O.txt").read()
data = data.lower()
wc(data)
